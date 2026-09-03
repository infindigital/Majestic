# Image & media assets

All site media lives here, grouped by purpose. Filenames are descriptive so
assets are easy to find, replace, or update.

```
image/
├── logos/          Brand marks (SVG — scalable, tiny, themeable)
│   ├── majestic-excalibur-logo.svg        full color, for light backgrounds
│   ├── majestic-excalibur-logo-light.svg  for dark (header/footer) backgrounds
│   └── favicon.svg                         emblem only (browser tab icon)
├── hero/           Large hero artwork
│   └── home-hero.svg                       homepage hero backdrop
├── backgrounds/    Section textures & banners
│   ├── page-header.svg                     interior page header backdrop
│   └── energy-grid.svg                     tiling texture over navy sections
├── about/          About-page imagery
│   └── company-overview.svg
├── products/       Product photography (drop real photos here)
├── team/           Leadership / team photography
└── icons/          Extra icon files (most UI icons are inline SVG in the HTML)
```

## Replacing placeholders with real assets

The `.svg` files above are **tasteful placeholders** so the site renders
complete out of the box. To use real photography:

1. Add your image (e.g. `home-hero.jpg`, ideally ~1920px wide, compressed) to
   the matching folder.
2. Update the reference in the HTML/CSS:
   - Home hero: `css/base.css` → `.hero` background, or the `<img>` in
     `index.html`.
   - Product cards: add `<img src="image/products/your-photo.jpg" …>` inside
     each `.product-card` in `products.html` / `index.html`.
3. Keep the same aspect ratio where possible to avoid layout shift, and always
   set a descriptive `alt` attribute.

**Tips:** prefer `.webp`/`.avif` with a `.jpg` fallback for photos; keep SVG for
logos and icons; run images through an optimizer (e.g. Squoosh) before commit.
