# Majestic Excalibur — Oil &amp; Gas Trading LLC

A high-fidelity, **fully static** corporate website for Majestic Excalibur Oil &amp;
Gas Trading LLC — a global energy and commodity trading company. Built with
**HTML5, CSS3 and vanilla JavaScript only** (no frameworks, no build step) and
engineered to be responsive, accessible, SEO-friendly and production-ready.

> **How this rebuild was produced.** The reference site
> (`https://majesticexcalibur.com/`) was not directly reachable from the build
> environment (network egress policy). The content, structure and product
> catalogue were reconstructed from publicly indexed data and rewritten as
> original copy, then implemented with a premium **navy + gold** identity that
> matches the "Majestic Excalibur" brand. Imagery is provided as tasteful,
> clearly-labelled **SVG placeholders** — drop in the real photography and
> confirm the contact details to make it 1:1. See `reference/` for the full
> content inventory and design notes.

---

## Pages

| File            | Purpose                                                        |
|-----------------|----------------------------------------------------------------|
| `index.html`    | Home — hero, capabilities, product highlights, stats, process  |
| `about.html`    | About — who we are, mission/vision/values, differentiators     |
| `products.html` | Products — full catalogue with anchored entries + specs        |
| `services.html` | Services — capabilities, process workflow                      |
| `contact.html`  | Contact — info tiles, validated enquiry form, map slot         |
| `404.html`      | Friendly not-found page                                        |

## Project structure

```
.
├── index.html · about.html · products.html · services.html · contact.html · 404.html
├── css/
│   ├── base.css          Design tokens (:root), reset, typography, utilities
│   ├── layout.css        Header/nav, hero, page headers, footer
│   ├── components.css    Buttons, cards, forms, stats, accordions, etc.
│   └── responsive.css    Tablet & mobile breakpoints + print styles
├── js/
│   ├── main.js           Mobile nav, sticky header, back-to-top, accordions, year
│   ├── reveal.js         Scroll-reveal via IntersectionObserver
│   ├── counters.js       Animated statistic counters
│   └── contact-form.js   Accessible client-side form validation
├── image/                All media (see image/README.md) — logos, hero, backgrounds…
├── video/                Optional hero/background video assets
├── reference/            Content inventory + design notes for this rebuild
├── robots.txt · sitemap.xml · site.webmanifest
└── .gitignore
```

## Design system (at a glance)

- **Palette:** midnight navy (`--navy-900…600`) + refined gold (`--gold-500…300`).
- **Type:** Poppins (headings) + Inter (body), loaded from Google Fonts with a
  full system fallback stack and fluid `clamp()` sizing.
- **Tokens:** all colours, spacing, radius, shadow and motion values live as CSS
  custom properties in `css/base.css` — change the brand in one place.
- Full rationale in [`reference/design-notes.md`](reference/design-notes.md).

## Running locally

It's a static site — no dependencies. Either open `index.html` directly, or
serve the folder (recommended, so absolute paths and the manifest resolve):

```bash
# Python 3
python3 -m http.server 8080
# or Node
npx serve .
```

Then visit `http://localhost:8080`.

## Deploying

Upload the repository root to any static host — **GitHub Pages, Netlify, Vercel,
Cloudflare Pages, S3 + CloudFront**, or classic shared hosting. No server-side
runtime is required.

## Making it production-final (checklist)

1. **Contact details** — replace the placeholder phone/email/address in every
   page footer and in `contact.html` (search for `+971 (0)0 000 0000` and
   `info@majesticexcalibur.com`).
2. **Real imagery** — see [`image/README.md`](image/README.md) to swap the SVG
   placeholders for photography.
3. **Contact form endpoint** — the form validates client-side and simulates a
   send. Wire `submitForm()` in `js/contact-form.js` to a real endpoint, e.g.
   [Formspree](https://formspree.io) (`fetch('https://formspree.io/f/XXXX', …)`)
   or your own API.
4. **Map** — replace the map placeholder in `contact.html` with a Google Maps
   `<iframe>` (Google Maps → Share → Embed a map).
5. **Domain** — the canonical URLs, `sitemap.xml` and `robots.txt` already point
   at `https://majesticexcalibur.com/`; update if the domain differs.
6. **Social links** — set the real profile URLs on the footer social icons
   (currently `#`).
7. *(Optional)* Minify/concatenate CSS &amp; JS and add a raster `favicon.png`
   for legacy browsers.

## Accessibility &amp; SEO

- Semantic landmarks, a skip link, keyboard-visible focus, and ARIA on the menu,
  accordions and form.
- One `<h1>` per page, logical heading order, descriptive `alt` text.
- Per-page `<title>` + meta description + canonical, Open Graph/Twitter cards,
  JSON-LD Organization schema, `robots.txt` and `sitemap.xml`.
- Respects `prefers-reduced-motion` (animations and smooth scroll are disabled).

## Browser support

Evergreen browsers (Chrome, Edge, Firefox, Safari). Uses CSS Grid, custom
properties and `IntersectionObserver`; JS degrades gracefully where APIs are
unavailable.

---

© Majestic Excalibur Oil &amp; Gas Trading LLC. Code scaffold provided as a
static site starter.
