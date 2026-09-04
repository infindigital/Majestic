#!/usr/bin/env python3
"""
Static site generator for Majestic Excalibur Oil & Gas Trading LLC.
Emits plain HTML files (index.html, about.html, services.html, contact.html
and 7 product pages) that use assets/css/style.css + assets/js/main.js.

Run from repo root:  python3 tools/build_pages.py
"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMPANY = "Majestic Excalibur Oil &amp; Gas Trading LLC"
PHONE = "+971 4 575 0081"
EMAIL = "info@majesticexcalibur.com"
ADDRESS = "POST BOX DXB No94422"

# ---- Services used in nav dropdown + footer + services page ----
SERVICES = [
    ("Petroleum Products Trading", "petroleum.html"),
    ("Lubricants and Greases", "lubricants.html"),
    ("Bitumen and Asphalt Products", "bitumen.html"),
    ("LNG and LPG Supply", "lng-lpg.html"),
    ("Coal Supply", "coal-supply.html"),
    ("Crude Oil Trading", "crude-oil.html"),
    ("Agricultural and Chemical Commodities", "agricultural-chemical.html"),
]


def head(title, desc, active):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/images/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
"""


def header(active):
    dd = "\n".join(
        f'          <li><a href="{u}">{html.escape(n)}</a></li>' for n, u in SERVICES
    )
    def cls(name):
        return ' class="active"' if name == active else ""
    return f"""<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="{COMPANY} home">
      <img src="assets/images/logo.png" alt="Majestic Excalibur Oil &amp; Gas Trading LLC logo">
    </a>
    <nav>
      <ul class="nav-links">
        <li><a href="index.html"{cls('home')}>Home</a></li>
        <li><a href="about.html"{cls('about')}>About Us</a></li>
        <li class="has-dropdown">
          <a href="services.html"{cls('services')}>Services</a>
          <ul class="dropdown">
{dd}
          </ul>
        </li>
        <li><a href="contact.html"{cls('contact')}>Contact Us</a></li>
      </ul>
    </nav>
    <div class="nav-cta">
      <a class="btn btn--dark" href="contact.html">Let&rsquo;s Talk</a>
      <button class="nav-toggle" aria-label="Toggle navigation"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
"""


def footer():
    quick = [
        ("Home", "index.html"), ("About Us", "about.html"),
        ("Services", "services.html"), ("Contact Us", "contact.html"),
        ("Operational &amp; Logistic Capability", "services.html"),
        ("Terms &amp; Condition", "#"),
    ]
    quick_html = "\n".join(f'          <li><a href="{u}">{n}</a></li>' for n, u in quick)
    serv_html = "\n".join(
        f'          <li><a href="{u}">{html.escape(n)}</a></li>' for n, u in SERVICES
    )
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/images/logo-white.png" alt="Majestic Excalibur logo">
        <p>Reliable Energy and<br>Commodity Supply</p>
        <div class="footer-social">
          <a href="#" aria-label="Facebook">f</a>
          <a href="#" aria-label="Twitter">t</a>
          <a href="#" aria-label="YouTube">&#9658;</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Quick Links</h4>
        <ul>
{quick_html}
        </ul>
      </div>
      <div class="footer-col">
        <h4>Services</h4>
        <ul>
{serv_html}
        </ul>
      </div>
      <div class="footer-col">
        <h4>Contact Information</h4>
        <ul class="footer-contact">
          <li><span class="ic">&#9679;</span><span>{ADDRESS}</span></li>
          <li><span class="ic">&#9993;</span><span>{EMAIL}</span></li>
          <li><span class="ic">&#9742;</span><span>{PHONE}</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>{COMPANY} 2025 &copy; All Rights Reserved</span>
      <span><a href="#">Terms &amp; Conditions</a> &nbsp; | &nbsp; <a href="#">Privacy Policy</a></span>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>
"""


def banner(title, crumb):
    return f"""<section class="page-banner">
  <div class="container">
    <h1>{title}</h1>
    <p class="breadcrumb"><a href="index.html">Home</a> &ndash; {crumb}</p>
  </div>
</section>
"""


# ============================================================
# Shared content blocks
# ============================================================
STRENGTH = f"""<section class="section section--soft">
  <div class="container">
    <div class="strength-top">
      <div>
        <span class="pill">Our Strength</span>
        <h2>Built for Scale, Reliability, and Global Reach</h2>
        <p class="muted">Our trading capabilities are supported by decades of experience, international partnerships, and a diversified product portfolio.</p>
      </div>
      <div class="strength-stats">
        <div class="item"><div class="num">35+</div><div class="lbl">Global Partners</div></div>
        <div class="item"><div class="num">20+</div><div class="lbl">Active Markets</div></div>
      </div>
    </div>
    <div class="strength-grid">
      <div class="strength-card"><div class="ic">&#128295;</div><h3>Global Sourcing</h3><p>We source products from internationally certified producers and refineries across multiple regions.</p></div>
      <div class="strength-card strength-card--brown"><div class="ic">&#127793;</div><h3>Diverse Portfolio</h3><p>Our offerings span energy, fuels, and commodities to serve multiple industries and markets.</p></div>
      <div class="strength-card"><div class="ic">&#128230;</div><h3>Supply Chain Control</h3><p>We manage logistics and coordination to ensure timely, secure, and efficient deliveries.</p></div>
      <div class="strength-card"><div class="ic">&#128104;</div><h3>Regulatory Compliance</h3><p>All operations adhere to international standards, safety protocols, and ethical trading practices.</p></div>
    </div>
  </div>
</section>
"""

WHY = f"""<section class="section">
  <div class="container why-grid">
    <div class="why-media">
      <div class="why-badge"><span class="ic">&#127942;</span>Trusted<br>Global Trader</div>
      <img src="assets/images/engineer.jpg" alt="Engineer at an energy facility">
    </div>
    <div>
      <span class="pill">Why Choose Us?</span>
      <h2>Trusted by Global Energy and Commodity Partners</h2>
      <p class="muted">We combine experience, transparency, and operational discipline to deliver consistent value across complex international trading environments.</p>
      <div class="why-list">
        <div class="why-item"><span class="no">01</span><h4>Integrity First Approach</h4><p>Our business is built on ethical conduct, transparency, and long term relationship building.</p></div>
        <div class="why-item"><span class="no">02</span><h4>Proven Market Expertise</h4><p>Decades of experience enable us to navigate volatile markets with confidence and precision.</p></div>
        <div class="why-item"><span class="no">03</span><h4>Reliable Execution</h4><p>We prioritize accuracy, consistency, and dependable delivery across every transaction.</p></div>
      </div>
    </div>
  </div>
</section>
"""

PARTNERS = f"""<section class="section--tight">
  <div class="container partners">
    <h4>Partnering With Leading Global Organizations</h4>
    <div class="partners-row">
      <span>pro&middot;d</span><span>H2O</span><span>BL&#8709;E</span><span>NIXIE</span><span>IFOCUS</span>
    </div>
  </div>
</section>
"""

CTA = f"""<section class="section cta">
  <div class="container cta-grid">
    <div>
      <span class="pill">Get Started</span>
      <h2>Let&rsquo;s Build a Strong Trading Partnership</h2>
      <p>Connect with {COMPANY} to explore reliable energy and commodity trading opportunities.</p>
      <a class="btn btn--light" href="contact.html">Contact Our Team</a>
    </div>
    <form class="cta-form" data-contact>
      <h3>Get Your Free Consultation</h3>
      <input class="field" type="text" name="name" placeholder="Name" required>
      <input class="field" type="email" name="email" placeholder="Email" required>
      <textarea class="field" name="message" placeholder="Message" required></textarea>
      <button type="submit" class="btn btn--gold btn--block">Send</button>
    </form>
  </div>
</section>
"""


# ============================================================
# HOME
# ============================================================
def page_home():
    core = [
        ("Energy Trading", "Petroleum Products Trading",
         "Supplying refined petroleum products from certified refineries with consistent quality, regulatory compliance, and reliable global delivery.",
         "offshore-rig.jpg", "Certified Supply", "petroleum.html"),
        ("Commodities", "Agricultural and Chemical Commodities",
         "Trading fertilizers and performance additives that support agricultural productivity and industrial fuel efficiency.",
         "petrochemical.jpg", "Strategic Supply", "agricultural-chemical.html"),
        ("Infrastructure", "Bitumen and Asphalt Products",
         "Supplying penetration and viscosity grade bitumen for road construction, waterproofing, and heavy duty infrastructure projects.",
         "power-lines.jpg", "ASTM Compliant", "bitumen.html"),
        ("Gas Supply", "LNG and LPG Supply",
         "Trading and supplying liquefied natural gas and petroleum gas for domestic, commercial, and industrial energy applications.",
         "pipelines.jpg", "Clean Energy", "lng-lpg.html"),
        ("Crude Trading", "Crude Oil Trading",
         "Facilitating global crude oil trade including premium export blends that support refinery operations worldwide.",
         "pumpjack.jpg", "Global Sourcing", "crude-oil.html"),
    ]
    cards = ""
    for i, (eb, title, desc, img, tag, url) in enumerate(core):
        last = " serv-card--last" if i == len(core) - 1 else ""
        cards += f"""      <article class="serv-card{last}">
        <div>
          <div class="eyebrow">{eb}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
          <a class="btn btn--dark" href="{url}">View Details</a>
        </div>
        <div class="serv-card__media">
          <img src="assets/images/{img}" alt="{title}">
          <span class="check">{tag}</span>
        </div>
      </article>
"""

    portfolio = [
        ("EN590 Diesel", "High quality ultra low sulfur diesel supplied in 10ppm specifications, suitable for automotive, industrial, and marine applications while meeting international fuel standards."),
        ("Gasoil", "A refined middle distillate fuel widely used across industrial and power generation sectors, supplied with consistent quality and regulatory compliance."),
        ("Fuel Oil", "Heavy fuel oils suitable for marine engines, power plants, and industrial boilers, delivered through structured supply arrangements."),
        ("Crude Oil", "Premium grade crude oil sourced from reliable producers to support refinery operations and international energy markets."),
        ("Marine Fuel and Lubricant Supply", "Comprehensive marine fuel and lubricant solutions supporting shipping and offshore operations with dependable supply coordination."),
        ("Liquefied Natural Gas (LNG)", "Clean burning natural gas supplied in liquefied form for efficient storage, transportation, and industrial energy use."),
        ("Jet Fuel", "Aviation turbine fuel supplied to meet international aviation standards for commercial and operational requirements."),
        ("Liquefied Petroleum Gas (LPG)", "A versatile energy source supplied for domestic, commercial, and industrial applications with safety and reliability."),
        ("Naphtha", "Light petroleum distillate used as a feedstock in petrochemical processing, blending, and industrial applications."),
        ("Bitumen", "High quality bitumen products supplied for road construction, infrastructure development, and industrial use."),
    ]
    pf = "".join(
        f'      <div class="pf-card"><h4>{t}</h4><p>{d}</p></div>\n' for t, d in portfolio
    )

    return head(
        "Majestic Excalibur Oil &amp; Gas Trading LLC | Global Energy &amp; Commodity Trading",
        "Majestic Excalibur Oil & Gas Trading LLC operates across global energy and commodity markets, supplying petroleum products, gas, lubricants, bitumen, coal, crude oil, and agricultural commodities.",
        "home",
    ) + header("home") + f"""
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <h1>Global Energy and Cross border transaction in petroleum products</h1>
        <p class="lead">{COMPANY} operates across global energy and commodity markets, supplying petroleum products, gas, lubricants, bitumen, coal, crude oil, and agricultural commodities through reliable sourcing and compliant trading practices.</p>
        <a class="btn btn--gold" href="contact.html">Connect With Us <span class="spark">&#9889;</span></a>
      </div>
      <div class="hero-media">
        <img src="assets/images/offshore-rig.jpg" alt="Offshore oil and gas platform">
      </div>
    </div>
    <div class="hero-strip">
      <div class="hs-card hs-card--split">
        <div>
          <h3>Global Energy Trade in Action</h3>
          <p class="muted" style="font-size:.88rem;margin:0;">Explore how our integrated trading network connects producers, refineries, and end users across international markets.</p>
        </div>
        <img src="assets/images/coal-plant.jpg" alt="Energy facility">
      </div>
      <div class="hs-card">
        <p class="muted" style="font-size:.88rem;">Supporting global industries with reliable energy supply and diversified commodity trading solutions.</p>
        <div class="hs-stats">
          <div><div class="num">10+</div><div class="lbl">Years Expertise</div></div>
          <div><div class="hs-icon">&#128188;</div><div class="lbl">Multi Commodity</div></div>
        </div>
      </div>
      <div class="hs-card hs-card--gold">
        <h3>Operational &amp; Logistic Capability</h3>
        <a class="btn btn--dark" href="services.html">Know More</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container about-split">
    <span class="pill">Who We Are</span>
    <div class="about-body">
      <h2>A Global Energy and Commodities Trading Company</h2>
      <p class="muted">{COMPANY} specializes in the sourcing, trading, and distribution of energy products and strategic commodities, serving industrial, commercial, and government clients across international markets.</p>
      <div class="about-visual">
        <img src="assets/images/refinery-water.jpg" alt="Refinery at dusk">
        <div class="vm-col">
          <a class="btn btn--gold vm-cta" href="about.html">About Us <span class="spark">&#9889;</span></a>
          <div class="vm-card"><h3>Our Vision</h3><p>To deliver dependable energy and commodity trading solutions through ethical practices, strong partnerships, and efficient supply chains that support global market demands.</p></div>
          <div class="vm-card vm-card--brown"><h3>Our Mission</h3><p>To be a globally respected trading organization recognized for integrity, operational excellence, and sustainable growth across energy and commodity sectors.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="pill">Services</span>
      <h2>Our Core Trading and Supply Services</h2>
      <p class="muted">We provide a diversified range of energy, fuel, and commodity trading services designed to meet the evolving needs of global markets.</p>
    </div>
    <div class="serv-grid">
{cards}    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>PRODUCT &amp; SUPPLY PORTFOLIO</h2>
    <p class="muted max-760" style="max-width:100%;">{COMPANY} offers a diversified portfolio of energy and petroleum products sourced from reputable producers and certified refineries. Our supply capability is designed to support industrial, commercial, and institutional buyers through reliable, compliant, and professionally managed trade execution across global markets.</p>
    <div class="portfolio-grid">
{pf}    </div>
  </div>
</section>

{STRENGTH}
{WHY}
{PARTNERS}

<section class="section">
  <div class="container testi-grid">
    <div class="testi-media"><img src="assets/images/refinery-aerial.jpg" alt="Aerial view of refinery"></div>
    <div>
      <span class="pill">Testimonials</span>
      <h2>Trusted by Clients and Partners Worldwide</h2>
      <p class="muted">Our partners value our commitment to reliability, compliance, and long standing professional relationships.</p>
      <div class="testi-card">
        <div class="testi-quote">&rdquo;</div>
        <blockquote>A professional team that understands market dynamics and executes with precision.</blockquote>
        <div class="testi-author">
          <div class="avatar">KM</div>
          <div><div class="name">Kwame Mensah</div><div class="role">Energy Operations Director</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

{CTA}
""" + footer()


# ============================================================
# ABOUT
# ============================================================
def page_about():
    values = [
        ("01", "Integrity", "We conduct all business with transparency, honesty, and strict adherence to ethical standards."),
        ("02", "Reliability", "We deliver consistent performance through dependable supply, disciplined execution, and accountability."),
        ("03", "Excellence", "We pursue operational efficiency, market expertise, and continuous improvement in every transaction."),
        ("04", "Partnership", "We build long term relationships based on trust, collaboration, and mutual growth."),
    ]
    vcards = "".join(
        f'        <div class="value-card"><div class="no">{n}</div><h4>{t}</h4><p>{d}</p></div>\n'
        for n, t, d in values
    )
    return head(
        "About Us | Majestic Excalibur Oil &amp; Gas Trading LLC",
        "Majestic Excalibur Oil & Gas Trading LLC is a global energy and commodity trading company focused on sourcing, supplying, and distributing high quality products across international markets.",
        "about",
    ) + header("about") + banner("About Us", "About Us") + f"""
<section class="section">
  <div class="container about-split">
    <span class="pill">Who We Are</span>
    <div class="about-body">
      <h2>A Global Energy and Commodities Trading Company</h2>
      <p class="muted">{COMPANY} is a global energy and commodity trading company focused on sourcing, supplying, and distributing high quality products across international markets. We work with trusted producers, refineries, and partners to deliver petroleum products, gas, lubricants, crude oil, coal, bitumen, and agricultural commodities with consistency and compliance.</p>
      <p class="muted">With a disciplined trading approach and strong market understanding, we support industrial, commercial, and government clients through reliable supply chains and transparent business practices. Our operations are guided by integrity, efficiency, and long term partnership values.</p>
      <div class="about-visual">
        <img src="assets/images/refinery-water.jpg" alt="Refinery at dusk">
        <div class="vm-col">
          <a class="btn btn--gold vm-cta" href="contact.html">Contact Us <span class="spark">&#9889;</span></a>
          <div class="vm-card"><h3>Our Vision</h3><p>To deliver dependable energy and commodity trading solutions through ethical practices, strong partnerships, and efficient supply chains that support global market demands.</p></div>
          <div class="vm-card vm-card--brown"><h3>Our Mission</h3><p>To be a globally respected trading organization recognized for integrity, operational excellence, and sustainable growth across energy and commodity sectors.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="pill">Our Value</span>
      <h2>The Principles That Guide Our Business</h2>
      <p class="muted max-760 mx-auto">Our values shape how we operate, partner, and grow. They reflect our commitment to responsible trading, professional conduct, and delivering long term value across global energy and commodity markets.</p>
    </div>
    <div class="values-grid" style="margin-top:40px;">
      <div class="values-media">
        <img src="assets/images/storage-tank.jpg" alt="Storage tanks">
      </div>
      <div class="values-cards">
{vcards}      </div>
    </div>
  </div>
</section>

{STRENGTH}
{WHY}
{CTA}
""" + footer()


# ============================================================
# SERVICES
# ============================================================
def page_services():
    items = [
        ("Petroleum Products Trading", "Trading refined petroleum products sourced from certified refineries, ensuring quality consistency, regulatory compliance, and dependable international supply.", "offshore-rig.jpg", "petroleum.html"),
        ("Lubricants and Greases", "Supplying automotive, industrial, and synthetic lubricants designed to enhance equipment performance and extend operational lifespan.", "storage-tank.jpg", "lubricants.html"),
        ("Bitumen and Asphalt Products", "Providing penetration and viscosity grade bitumen solutions for road construction, infrastructure development, and industrial applications.", "power-lines.jpg", "bitumen.html"),
        ("LNG and LPG Supply", "Trading liquefied natural and petroleum gas to support clean, efficient energy needs across commercial and industrial sectors.", "pipelines.jpg", "lng-lpg.html"),
        ("Coal Supply", "Supplying thermal and coking coal for power generation, steel production, and industrial processing through reliable global sourcing.", "coal-plant.jpg", "coal-supply.html"),
        ("Crude Oil Trading", "Facilitating global crude oil trade including premium export blends that support refinery operations and energy markets worldwide.", "pumpjack.jpg", "crude-oil.html"),
        ("Agricultural and Chemical Commodities", "Trading fertilizers, additives, and industrial chemicals that support agricultural productivity and industrial efficiency.", "petrochemical.jpg", "agricultural-chemical.html"),
    ]
    cards = ""
    for title, desc, img, url in items:
        cards += f"""      <article class="serv-card" style="grid-template-columns:1fr;">
        <img src="assets/images/{img}" alt="{title}" style="width:100%;height:220px;object-fit:cover;border-radius:16px;">
        <div>
          <h3 style="color:#fff;">{title}</h3>
          <p>{desc}</p>
          <a class="btn btn--dark" href="{url}">More Detail <span class="spark">&#9889;</span></a>
        </div>
      </article>
"""
    return head(
        "Services | Majestic Excalibur Oil &amp; Gas Trading LLC",
        "Integrated energy and commodity trading services: petroleum products, lubricants, bitumen, LNG/LPG, coal, crude oil, and agricultural commodities.",
        "services",
    ) + header("services") + banner("Services", "Services") + f"""
<section class="section">
  <div class="container">
    <div class="sec-head">
      <span class="pill">Our Services</span>
      <h2>Integrated Energy and Commodity Trading Services</h2>
      <p class="muted max-760">We deliver a diversified portfolio of energy, fuel, and commodity trading services through reliable sourcing, compliant operations, and efficient global supply networks.</p>
    </div>
    <div class="serv-grid" style="grid-template-columns:repeat(2,1fr);">
{cards}    </div>
  </div>
</section>

{STRENGTH}
{CTA}
""" + footer()


# ============================================================
# CONTACT
# ============================================================
def page_contact():
    faqs = [
        ("What products do you trade?", "We trade petroleum products, gas, lubricants, bitumen, coal, crude oil, and selected agricultural commodities."),
        ("Which regions do you serve?", "We operate across international markets, serving industrial, commercial, and government clients in multiple regions worldwide."),
        ("Do you work with government and industrial clients?", "Yes. We supply industrial, commercial, and government clients through compliant, professionally managed trade execution."),
        ("Are your operations compliant with international standards?", "All operations adhere to international standards, safety protocols, and ethical trading practices."),
        ("How can I start a business partnership?", "Reach out through our contact form or contact details, and our team will guide you through the partnership process."),
    ]
    faq_html = ""
    for i, (q, a) in enumerate(faqs):
        open_cls = " open" if i == 0 else ""
        ico = "&ndash;" if i == 0 else "+"
        faq_html += f"""      <div class="faq-item{open_cls}">
        <button class="faq-q">{i+1}. {q}<span class="ico">{ico}</span></button>
        <div class="faq-a"><p>{a}</p></div>
      </div>
"""
    return head(
        "Contact | Majestic Excalibur Oil &amp; Gas Trading LLC",
        "Contact Majestic Excalibur Oil & Gas Trading LLC for business inquiries, partnerships, or service related questions.",
        "contact",
    ) + header("contact") + banner("Contact", "Contact") + f"""
<section class="section">
  <div class="container">
    <div class="contact-wrap">
      <div>
        <h2>Send Us a Message</h2>
        <p class="muted">Reach out to our team for business inquiries, partnerships, or service related questions. We will respond promptly and professionally.</p>
        <form data-contact>
          <input class="field" type="text" name="name" placeholder="Full Name" required>
          <input class="field" type="tel" name="phone" placeholder="Phone Number">
          <input class="field" type="email" name="email" placeholder="Email" required>
          <textarea class="field" name="message" placeholder="Message" required></textarea>
          <button type="submit" class="btn btn--gold btn--block">Send</button>
        </form>
      </div>
      <div class="contact-info">
        <span class="pill">Get in Touch</span>
        <h3>Let&rsquo;s Start a Conversation</h3>
        <p>Connect with {COMPANY} to discuss energy and commodity trading opportunities.</p>
        <ul>
          <li><span class="ic">&#9679;</span><span>{ADDRESS}</span></li>
          <li><span class="ic">&#9742;</span><span>{PHONE}</span></li>
          <li><span class="ic">&#9993;</span><span>{EMAIL}</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="pill">FAQ</span>
      <h2>Frequently Asked Questions</h2>
      <p class="muted max-680 mx-auto">Find quick answers to common questions about our services, operations, and business process.</p>
    </div>
    <div class="faq" style="margin-top:36px;">
{faq_html}    </div>
  </div>
</section>
""" + footer()


# ============================================================
# PRODUCT / SERVICE DETAIL PAGES
# ============================================================
PRODUCTS = {
    "crude-oil.html": {
        "title": "Crude Oil Trading",
        "overview": "We facilitate the global trading of premium grade crude oil to support refinery operations and international energy markets. Our crude oil trading services are built on trusted sourcing and market expertise.",
        "why": ["Trusted crude oil sources", "Global market access", "Disciplined trading practices", "Regulatory compliance"],
        "approach": "We work with established producers and buyers to ensure transparent transactions and smooth trade execution.",
        "image": "pumpjack.jpg",
        "card_title": "Crude Grades",
        "card_items": ["ESPO Crude Oil", "Light Sweet Crude", "Heavy Crude Blends", "Export Grade Blends"],
    },
    "petroleum.html": {
        "title": "Petroleum Products Trading",
        "overview": "We supply refined petroleum products sourced from certified refineries, ensuring consistent quality, regulatory compliance, and dependable global delivery for industrial, commercial, and marine buyers.",
        "why": ["Certified refinery sourcing", "Consistent product specifications", "Reliable international logistics", "Full regulatory compliance"],
        "approach": "We coordinate sourcing, quality inspection, and delivery to provide a seamless supply experience across global markets.",
        "image": "offshore-rig.jpg",
        "card_title": "Products",
        "card_items": ["EN590 Diesel (10ppm)", "Gasoil", "Jet Fuel (Jet A-1)", "Fuel Oil", "Naphtha"],
    },
    "lubricants.html": {
        "title": "Lubricants and Greases",
        "overview": "We supply automotive, industrial, and synthetic lubricants and greases designed to enhance equipment performance, reduce wear, and extend operational lifespan across a wide range of applications.",
        "why": ["Automotive and industrial grades", "Synthetic and mineral formulations", "Marine and offshore solutions", "Dependable supply coordination"],
        "approach": "We match the right lubricant solutions to each client's operational requirements and ensure reliable, on time supply.",
        "image": "storage-tank.jpg",
        "card_title": "Products",
        "card_items": ["Automotive Lubricants", "Industrial Oils", "Greases", "Synthetic Lubricants", "Marine Lubricants"],
    },
    "bitumen.html": {
        "title": "Bitumen and Asphalt Products",
        "overview": "We supply penetration and viscosity grade bitumen for road construction, waterproofing, and heavy duty infrastructure projects, meeting international quality and ASTM standards.",
        "why": ["Penetration and viscosity grades", "ASTM compliant quality", "Infrastructure grade supply", "Flexible packaging and delivery"],
        "approach": "We support contractors and infrastructure projects with consistent, compliant bitumen supply and reliable logistics.",
        "image": "power-lines.jpg",
        "card_title": "Grades",
        "card_items": ["Penetration Grade 60/70", "Penetration Grade 80/100", "Viscosity Grade (VG)", "Cutback Bitumen", "Bitumen Emulsion"],
    },
    "lng-lpg.html": {
        "title": "LNG and LPG Supply",
        "overview": "We trade and supply liquefied natural gas and liquefied petroleum gas for domestic, commercial, and industrial energy applications, supporting clean and efficient energy needs.",
        "why": ["Clean energy solutions", "Domestic and industrial supply", "Safe handling and logistics", "Reliable long term contracts"],
        "approach": "We provide structured supply arrangements for LNG and LPG with a focus on safety, reliability, and efficiency.",
        "image": "pipelines.jpg",
        "card_title": "Products",
        "card_items": ["Liquefied Natural Gas (LNG)", "Liquefied Petroleum Gas (LPG)", "Propane", "Butane"],
    },
    "coal-supply.html": {
        "title": "Coal Supply",
        "overview": "We supply thermal and coking coal for power generation, steel production, and industrial processing, sourced through reliable global producers and structured supply arrangements.",
        "why": ["Thermal and coking coal", "Consistent calorific value", "Global sourcing network", "Structured bulk logistics"],
        "approach": "We manage sourcing, quality verification, and bulk logistics to deliver dependable coal supply worldwide.",
        "image": "coal-plant.jpg",
        "card_title": "Products",
        "card_items": ["Thermal (Steam) Coal", "Coking Coal", "Anthracite", "Bituminous Coal"],
    },
    "agricultural-chemical.html": {
        "title": "Agricultural and Chemical Commodities",
        "overview": "We trade fertilizers, performance additives, and industrial chemicals that support agricultural productivity and industrial fuel efficiency, delivered through compliant and reliable supply channels.",
        "why": ["Agricultural fertilizers", "Industrial performance additives", "Quality assured products", "Compliant global supply"],
        "approach": "We connect producers and buyers to ensure strategic, compliant, and dependable supply of agricultural and chemical commodities.",
        "image": "petrochemical.jpg",
        "card_title": "Products",
        "card_items": ["Urea", "Fertilizers", "Sulphur", "Performance Additives"],
    },
}


def page_product(filename, data):
    why = "".join(f"        <li>{w}</li>\n" for w in data["why"])
    citems = "".join(f"        <li>{c}</li>\n" for c in data["card_items"])
    return head(
        f"{data['title']} | Majestic Excalibur Oil &amp; Gas Trading LLC",
        data["overview"],
        "services",
    ) + header("services") + f"""
<section class="page-banner page-banner--product">
  <div class="container">
    <h1>{data['title']}</h1>
    <p class="breadcrumb"><a href="index.html">Home</a> &ndash; <a href="services.html">Services</a></p>
  </div>
</section>

<section class="section">
  <div class="container detail-grid">
    <div class="detail-body">
      <h2>Overview</h2>
      <p class="muted">{data['overview']}</p>
      <h3>Why Choose This Service</h3>
      <ul class="detail-list">
{why}      </ul>
      <div class="approach-card">
        <h3>Our Approach</h3>
        <p>{data['approach']}</p>
      </div>
    </div>
    <div class="detail-media">
      <img src="assets/images/{data['image']}" alt="{data['title']}">
      <div class="grades-card">
        <h3>{data['card_title']}</h3>
        <ul>
{citems}        </ul>
      </div>
    </div>
  </div>
</section>

{CTA}
""" + footer()


# ============================================================
# BUILD
# ============================================================
def write(name, content):
    path = os.path.join(ROOT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name)


def main():
    write("index.html", page_home())
    write("about.html", page_about())
    write("services.html", page_services())
    write("contact.html", page_contact())
    for fn, data in PRODUCTS.items():
        write(fn, page_product(fn, data))
    print("Done. %d pages." % (4 + len(PRODUCTS)))


if __name__ == "__main__":
    main()
