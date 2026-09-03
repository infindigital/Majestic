# Design Notes — Majestic Excalibur static rebuild

A concise record of the design system so the site stays consistent and easy to
extend. All tokens live in `css/base.css` under `:root`.

## Identity direction

"Majestic" → deep royal navy. "Excalibur" → a golden blade. The palette pairs a
**midnight-navy** base with a **refined gold** accent to read premium,
authoritative, and trustworthy — the tone expected of an international energy &
commodity trading house.

## Color tokens

| Token             | Value     | Use                                    |
|-------------------|-----------|----------------------------------------|
| `--navy-900`      | `#081627` | Footer, deepest sections               |
| `--navy-800`      | `#0b1e34` | Header, hero base                      |
| `--navy-700`      | `#123152` | Panels on navy                         |
| `--navy-600`      | `#1a4270` | Hover / borders on navy                |
| `--gold-500`      | `#c9a227` | Primary accent, buttons, rules         |
| `--gold-400`      | `#d8b24a` | Hover accent                           |
| `--gold-300`      | `#e6c876` | Highlights on dark                     |
| `--ink`           | `#0e1b2c` | Body headings on light                 |
| `--muted`         | `#5c6b7e` | Secondary text                         |
| `--line`          | `#e6eaf0` | Hairlines, card borders                |
| `--bg`            | `#ffffff` | Page background                        |
| `--bg-alt`        | `#f5f7fa` | Alternating section background         |

## Type

- **Headings/UI display:** Poppins (600/700) — geometric, confident.
- **Body/UI:** Inter (400/500/600) — highly legible at all sizes.
- Loaded from Google Fonts with `display=swap` and a full system fallback stack
  so text renders instantly and the site still works offline.
- Fluid type via `clamp()` — scales smoothly desktop → mobile.

## Layout

- Container max-width `1200px`, gutter `clamp(1rem, 4vw, 2.5rem)`.
- Section vertical rhythm `clamp(3.5rem, 8vw, 7rem)`.
- 12-col mental model built with CSS grid `auto-fit/minmax` for card rows.

## Motion

- Scroll-reveal via `IntersectionObserver` (`js/reveal.js`), disabled when the
  user prefers reduced motion.
- Animated stat counters (`js/counters.js`), also reduced-motion aware.
- Hover: subtle lift + gold underline; 150–250ms ease transitions.

## Assets

All media lives under `image/` with descriptive names; logos are SVG (crisp,
tiny, themeable). Photographic slots use tasteful SVG **placeholders** meant to
be replaced with real photography — see `image/README.md`.

## Accessibility & SEO

- Landmarks (`header/nav/main/footer`), skip link, visible focus states.
- One `<h1>` per page, ordered headings, descriptive `alt`, ARIA on the menu.
- Per-page `<title>`, meta description, canonical, Open Graph/Twitter, and
  `application/ld+json` Organization schema. `robots.txt` + `sitemap.xml`.
