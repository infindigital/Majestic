# Majestic Excalibur Oil & Gas Trading LLC — Website

A static marketing website (plain HTML/CSS/JS) for Majestic Excalibur Oil & Gas
Trading LLC, a global energy and commodity trading company.

## Pages

| Page | File |
|------|------|
| Home | `index.html` |
| About Us | `about.html` |
| Services | `services.html` |
| Contact | `contact.html` |
| Petroleum Products Trading | `petroleum.html` |
| Lubricants and Greases | `lubricants.html` |
| Bitumen and Asphalt Products | `bitumen.html` |
| LNG and LPG Supply | `lng-lpg.html` |
| Coal Supply | `coal-supply.html` |
| Crude Oil Trading | `crude-oil.html` |
| Agricultural and Chemical Commodities | `agricultural-chemical.html` |

## Structure

```
.
├─ index.html, about.html, services.html, contact.html, <product>.html
├─ assets/
│  ├─ css/style.css        # design system + all components
│  ├─ js/main.js           # mobile nav, dropdown, FAQ accordion, forms
│  └─ images/              # cleaned/renamed photos used by the site + logo
├─ image/                  # original brand/design source assets
├─ reference/              # design mockups (not served — reference only)
└─ tools/build_pages.py    # regenerates the HTML pages from shared templates
```

## Local preview

```bash
python3 -m http.server 8099
# open http://127.0.0.1:8099/index.html
```

## Editing

Header, footer and repeated sections are shared. To keep every page consistent,
edit the content/templates in `tools/build_pages.py` and regenerate:

```bash
python3 tools/build_pages.py
```

Styling lives entirely in `assets/css/style.css`. The site is fully responsive
and uses the Poppins web font (loaded from Google Fonts) with a system-font
fallback.

## Notes

- Contact and consultation forms are client-side only (no backend); wire them to
  an email service or form handler before going live.
- `reference/` contains large design mockups kept for reference and is not part
  of the served site.
