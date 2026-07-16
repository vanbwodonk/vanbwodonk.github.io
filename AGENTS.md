# vanbwodonk.github.io

GitHub Pages site — Jekyll Chirpy blog + RP2040/RP2350 PIO Simulator.

## Project Structure

```
./
  _config.yml              # Jekyll Chirpy theme config
  index.html               # Home page
  _data/
    contact.yml            # GitHub, Twitter, Email, RSS
    share.yml              # Twitter/Facebook/Telegram share buttons
  _posts/
    2026-07-16-hello-world.md   # First post
  _tabs/
    about.md               # About page (placeholder)
    archives.md            # Post archives
    categories.md          # Post categories
    tags.md                # Post tags
  .github/workflows/
    pages-deploy.yml       # GitHub Actions: build + deploy
  .devcontainer/           # VS Code remote container (Jekyll 2-bullseye)
  tools/
    run.sh                 # Jekyll dev server
    test.sh                # Production build + html-proofer
    pio_sim/               # PIO Simulator (see tools/pio_sim/AGENTS.md)
```

## Blog

Jekyll **Chirpy** theme hosted on GitHub Pages. Author: Arif Darmawan (vanbwodonk).
CI/CD: `pages-deploy.yml` — Ruby 3.4, `bundle exec jekyll build`, html-proofer test, deploy-pages.

### Completed
- [x] Initial site scaffold (Chirpy starter)
- [x] Hello World post (2026-07-16)

### Planned / Ideas
- [ ] Write more blog posts
- [ ] Customize about page
- [ ] Add avatar / social preview image
- [ ] Configure analytics (Google / Umami / etc.)
- [ ] Enable comments (utterances / giscus)

## PIO Simulator

See `tools/pio_sim/AGENTS.md` for full details.

Three-layer client-side JS app (no framework, no build): assembler → emulator → UI.
Simulates RP2040/RP2350 PIO state machines in the browser.

### Known Limitations
- `out exec` / `mov exec` (instruction injection) — not implemented
- IRQ `rel` modifier — not implemented
- Assembler-side side-set bit-width vs delay max check — not implemented

## CPAL

<!-- Append project-wide context here as work progresses -->
- Blog based on Chirpy starter template
- PIO simulator originally Japanese (by ice458), translated to English
- PIO instruction set accuracy matches RP2040/RP2350 datasheets
