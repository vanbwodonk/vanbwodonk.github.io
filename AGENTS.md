# vanbwodonk.github.io

GitHub Pages site — RP2040/RP2350 PIO Simulator (by ice458).

## Project Structure

```
./
  AGENTS.md               ← this file
  tools/pio_sim/
    index.html             # Single-page app (Japanese → English translated)
    main.js                # UI glue, canvas timing chart, GPIO interaction
    style.css              # Dark editor + responsive layout
    pio_assembler.js       # PIO assembly parser → instruction objects
    pio_emulator.js        # PIO state machine simulator
    pdf2md.py              # RP2350 datasheet PDF → Markdown converter
    PIO.png                # OG image
```

## Architecture

Three-layer client-side JS app (no framework, no build):

| Layer | File | Role |
|-------|------|------|
| Assembler | `pio_assembler.js` | Two-pass: labels/directives → JMP/WAIT/IN/OUT/PUSH/PULL/MOV/IRQ/SET + side-set + delay |
| Emulator | `pio_emulator.js` | Full SM: registers, 4-deep FIFOs, 2-FF input sync, history, wrap, IRQ wait |
| UI | `main.js` | DOM bindings, canvas timing chart, breakpoints, GPIO click interaction, localStorage |

## Key Details

- **Instructions**: JMP (all conds), WAIT (gpio/pin/irq), IN/OUT (pins/x/y/null/isr/osr), PUSH/PULL (block/noblock/ifull/ifempty), MOV (invert `~` / reverse `::`), IRQ (clear/wait), SET, NOP
- **Fidelity**: 2-FF input synchronizer with per-pin bypass, wrap (JMP bypasses wrap, MOV/OUT PC uses pcOverride), autopush/pull with 0=32 threshold
- **Config**: OUT/SET/SIDESET/IN base pins, JMP PIN, shift dirs, autopush/pull thresholds, MOV STATUS N, X/Y init values
- **UI**: X/Y init inputs with Update button (like TX/RX FIFO), below Interrupts section — only applied on click
- **Analytics**: GTM (GTM-MMZ5XH4V) with EEA geo-consent override
- **Unsupported**: `out exec` / `mov exec`, IRQ `rel` modifier, assembler side-set width vs delay check
- **No server**: pure client-side, nothing leaves the browser

## Completed Work

- [x] Learned codebase structure and all source files
- [x] Translated all Japanese text to English (index.html, pdf2md.py)
- [x] Added X/Y register init values with Update button below IRQ section

## CPAL

<!-- Keep this section for project memory; append to it as work progresses -->
- UI originally Japanese by ice458, translated to English
- PIO instruction set accuracy matches RP2040/RP2350 datasheets
