import os

# Complete, production-ready Royal Marathi Hindu Wedding Website Generator
# Combines:
# 1. Reference 1 (wedding-session.vercel.app): Editorial luxury layouts, Cormorant Garamond typography, 
#    responsive masonry photo gallery with full-featured interactive lightbox, clean functional RSVP.
# 2. Reference 2 (weddings-rouge.vercel.app): Royal Maroon (#641D2D) and Antique Gold (#C5A15B) aesthetic,
#    3D wax-sealed Maharashtrian envelope opening experience with Paithani border and audio unsealing.
# 3. Authentic Maharashtrian Hindu Wedding Traditions: 15 sacred rituals (आमचे मंगल सोहळे),
#    Ganesh Pujan (॥ श्री गणेशाय नमः ॥), Mangalashtake, Saptapadi, Mundavalya & Pheta dress code,
#    Shehnai & Raga audio synthesizer, and closing benediction (॥ शुभमंगल सावधान ॥).

def generate_website():
    html_content = '''<!DOCTYPE html>
<html lang="mr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="theme-color" content="#641D2D">
  <meta name="description" content="॥ शुभ विवाह ॥ The Royal Maharashtrian Hindu Wedding Celebration of Kasandra &amp; Imanule — Saturday, October 19, 2027 at The White Church, 125 Rd.">
  <title>॥ शुभ विवाह ॥ Kasandra &amp; Imanule — Royal Maharashtrian Wedding</title>

  <!-- External Stylesheets: Bootstrap 5, Bootstrap Icons, Swiper 11 -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">

  <!-- Google Fonts: Cormorant Garamond (Headings), DM Sans (Body), Noto Serif Devanagari (Marathi/Sanskrit) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600;1,700&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Noto+Serif+Devanagari:wght@400;500;600;700;800&family=Great+Vibes&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================================
       DESIGN SYSTEM & CSS VARIABLES (Royal Maharashtrian Heritage)
       ========================================================================== */
    :root {
      /* Primary Heritage Palette */
      --color-maroon: #641D2D;
      --color-maroon-dark: #4A121E;
      --color-burgundy: #3D101C;
      --color-maroon-06: rgba(100, 29, 45, 0.06);
      --color-maroon-12: rgba(100, 29, 45, 0.12);
      --color-maroon-20: rgba(100, 29, 45, 0.20);
      --color-maroon-40: rgba(100, 29, 45, 0.40);
      --color-maroon-80: rgba(100, 29, 45, 0.85);

      /* Antique Gold & Amber */
      --color-gold: #C5A15B;
      --color-gold-light: #E2CCA0;
      --color-gold-pale: #F3EBD8;
      --color-gold-dark: #9A7B38;
      --color-gold-20: rgba(197, 161, 91, 0.20);
      --color-gold-40: rgba(197, 161, 91, 0.40);

      /* Ivory, Beige & Warm Accents */
      --color-ivory: #FBF6EC;
      --color-ivory-light: #FFFCF7;
      --color-beige: #EDE0CB;
      --color-blush: #E8C8C2;
      --color-sage: #89917A;
      --color-charcoal: #30231F;
      --color-charcoal-muted: #5C4B46;

      /* Card & Surface Tokens */
      --color-bg-body: #FBF6EC;
      --color-bg-card: #FFFFFF;
      --color-bg-maroon-surface: #501522;

      /* Typography */
      --font-heading: 'Cormorant Garamond', Georgia, serif;
      --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-devanagari: 'Noto Serif Devanagari', serif;
      --font-script: 'Great Vibes', cursive;

      /* Layout */
      --max-container: 1180px;
      --transition-smooth: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Base & Reset */
    *, *::before, *::after {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      -webkit-tap-highlight-color: transparent;
    }

    html {
      scroll-behavior: smooth;
      background-color: var(--color-bg-body);
    }

    body {
      background: var(--color-bg-body);
      font-family: var(--font-body);
      color: var(--color-charcoal);
      line-height: 1.7;
      overflow-x: hidden;
      position: relative;
    }

    img {
      display: block;
      max-width: 100%;
      height: auto;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    /* Typography Utilities */
    .font-serif { font-family: var(--font-heading); }
    .font-body { font-family: var(--font-body); }
    .font-devanagari { font-family: var(--font-devanagari); }
    .font-script { font-family: var(--font-script); }

    .gold-gradient {
      background: linear-gradient(135deg, #DFCA95 0%, #C5A15B 50%, #9A7B38 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .maroon-gradient {
      background: linear-gradient(135deg, var(--color-maroon) 0%, var(--color-burgundy) 100%);
    }

    /* Container Utility */
    .site-container {
      width: 100%;
      max-width: var(--max-container);
      margin: 0 auto;
      padding: 0 24px;
    }

    .site-container-narrow {
      width: 100%;
      max-width: 820px;
      margin: 0 auto;
      padding: 0 24px;
    }

    .section-padding {
      padding: 100px 0;
      position: relative;
      z-index: 5;
    }

    @media (max-width: 768px) {
      .section-padding {
        padding: 68px 0;
      }
    }

    /* Section Headers */
    .section-eyebrow {
      font-family: var(--font-heading);
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: var(--color-gold);
      display: inline-flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
    }

    .section-eyebrow::before, .section-eyebrow::after {
      content: "";
      width: 28px;
      height: 1px;
      background: var(--color-gold);
      opacity: 0.7;
    }

    .section-heading {
      font-family: var(--font-heading);
      font-size: clamp(2.3rem, 4.5vw, 3.6rem);
      font-weight: 700;
      line-height: 1.15;
      color: var(--color-maroon);
      margin-bottom: 12px;
    }

    .section-subheading-mr {
      font-family: var(--font-devanagari);
      font-size: clamp(1.1rem, 2.2vw, 1.45rem);
      font-weight: 600;
      color: var(--color-gold-dark);
      margin-bottom: 14px;
      letter-spacing: 1px;
    }

    .section-desc {
      font-family: var(--font-body);
      font-size: 1.05rem;
      color: var(--color-charcoal-muted);
      max-width: 640px;
      margin: 0 auto 36px;
      line-height: 1.65;
    }

    .theme-divider {
      width: 54px;
      height: 2px;
      background: linear-gradient(90deg, transparent, var(--color-gold), transparent);
      margin: 16px auto 20px;
    }

    /* Temple / Paithani Ornamental Motif */
    .motif-divider {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      margin: 18px 0 24px;
      color: var(--color-gold);
    }

    .motif-line {
      width: 50px;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--color-gold), transparent);
    }

    .motif-symbol {
      font-size: 14px;
      letter-spacing: 4px;
    }

    /* Buttons */
    .btn-gold {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: linear-gradient(135deg, #E2CCA0 0%, #C5A15B 50%, #9A7B38 100%);
      color: var(--color-burgundy);
      font-family: var(--font-body);
      font-weight: 600;
      font-size: 14.5px;
      padding: 13px 36px;
      border-radius: 9999px;
      box-shadow: 0 8px 24px rgba(197, 161, 91, 0.35);
      transition: var(--transition-smooth);
      cursor: pointer;
      border: none;
      text-decoration: none;
    }

    .btn-gold:hover {
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 12px 32px rgba(197, 161, 91, 0.55);
      color: var(--color-burgundy);
    }

    .btn-maroon {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: linear-gradient(135deg, var(--color-maroon) 0%, var(--color-burgundy) 100%);
      color: var(--color-ivory);
      font-family: var(--font-body);
      font-weight: 600;
      font-size: 14.5px;
      padding: 13px 34px;
      border-radius: 9999px;
      box-shadow: 0 8px 24px rgba(100, 29, 45, 0.35);
      transition: var(--transition-smooth);
      cursor: pointer;
      border: 1px solid var(--color-gold-40);
      text-decoration: none;
    }

    .btn-maroon:hover {
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 12px 30px rgba(100, 29, 45, 0.55);
      color: #FFFFFF;
    }

    .btn-outline-gold {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: transparent;
      border: 1.5px solid var(--color-gold);
      color: var(--color-maroon);
      font-family: var(--font-body);
      font-weight: 600;
      font-size: 14px;
      padding: 12px 30px;
      border-radius: 9999px;
      transition: var(--transition-smooth);
      cursor: pointer;
      text-decoration: none;
    }

    .btn-outline-gold:hover {
      background: var(--color-maroon);
      color: var(--color-ivory);
      border-color: var(--color-maroon);
      transform: translateY(-2px);
    }

    /* ==========================================================================
       FLOATING AUDIO SOUNDWAVE PILL (No Header & No Navbar)
       ========================================================================== */
    .floating-audio-pill {
      position: fixed;
      top: 24px;
      right: 28px;
      z-index: 1000;
      background: rgba(61, 16, 28, 0.90);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--color-gold-40);
      border-radius: 9999px;
      padding: 8px 16px;
      display: flex;
      align-items: center;
      gap: 9px;
      cursor: pointer;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(197, 161, 91, 0.25);
      transition: var(--transition-smooth);
      color: var(--color-gold-light);
    }

    @media (max-width: 576px) {
      .floating-audio-pill {
        top: 16px;
        right: 16px;
        padding: 6px 12px;
      }
    }

    .floating-audio-pill:hover {
      background: var(--color-maroon);
      border-color: var(--color-gold);
      transform: translateY(-2px);
      color: #FFFFFF;
    }

    .audio-waves {
      display: flex;
      align-items: flex-end;
      gap: 2.5px;
      height: 14px;
    }

    .audio-wave-bar {
      width: 2.5px;
      background: var(--color-gold);
      border-radius: 2px;
      height: 4px;
      transition: height 0.2s;
    }

    .floating-audio-pill.playing .audio-wave-bar:nth-child(1) { animation: wavePulse 1s infinite alternate ease-in-out; }
    .floating-audio-pill.playing .audio-wave-bar:nth-child(2) { animation: wavePulse 0.8s 0.2s infinite alternate ease-in-out; }
    .floating-audio-pill.playing .audio-wave-bar:nth-child(3) { animation: wavePulse 1.2s 0.4s infinite alternate ease-in-out; }

    @keyframes wavePulse {
      0% { height: 3px; }
      100% { height: 14px; }
    }

    .audio-label {
      font-family: var(--font-heading);
      font-size: 12px;
      letter-spacing: 2px;
      text-transform: uppercase;
      font-weight: 700;
    }

    /* ==========================================================================
       SECTION 3: ROYAL MAHARASHTRIAN INVITATION ENVELOPE (Zareqia 3D Entrance)
       ========================================================================== */
    .envelope-entrance-overlay {
      position: fixed;
      inset: 0;
      z-index: 99999;
      background: radial-gradient(circle at 50% 45%, #4A121E 0%, #290811 60%, #150308 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      overflow-y: auto;
      overflow-x: hidden;
      padding: 24px 16px;
      transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1), transform 0.85s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.85s;
    }

    .envelope-entrance-overlay.envelope-dismissed {
      opacity: 0;
      visibility: hidden;
      transform: scale(1.06);
      pointer-events: none;
    }

    .envelope-intro-wrapper {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 100%;
      max-width: 440px;
      position: relative;
      z-index: 10;
    }

    .envelope-hint-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(61, 16, 28, 0.92);
      border: 1px solid var(--color-gold-40);
      color: var(--color-gold-light);
      padding: 7px 22px;
      border-radius: 9999px;
      font-family: var(--font-heading);
      font-size: 13.5px;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      font-weight: 700;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }

    .envelope-3d-scene {
      perspective: 1200px;
      width: 100%;
      display: flex;
      justify-content: center;
      position: relative;
      margin-top: 14px;
    }

    .vintage-envelope {
      position: relative;
      width: 100%;
      max-width: 390px;
      height: 550px;
      background: #FAF5EA linear-gradient(155deg, #FFFDF9 0%, #F6EEE0 50%, #ECDCC8 100%);
      border-radius: 20px;
      box-shadow: 
        0 30px 80px rgba(0, 0, 0, 0.95), 
        0 0 60px rgba(100, 29, 45, 0.3), 
        inset 0 0 0 1px rgba(197, 161, 91, 0.6),
        inset 0 0 0 5px rgba(250, 245, 234, 0.9),
        inset 0 0 0 7px rgba(197, 161, 91, 0.35);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      padding: 24px 20px 20px;
      box-sizing: border-box;
      transition: transform 0.4s ease, box-shadow 0.4s ease;
    }

    @media (max-width: 420px) {
      .vintage-envelope {
        height: 510px;
        padding: 20px 16px 16px;
      }
    }

    /* Paithani & Lotus Corner Accents */
    .envelope-corner-ornament {
      position: absolute;
      width: 44px;
      height: 44px;
      opacity: 0.7;
      pointer-events: none;
      z-index: 3;
    }

    .corner-tl { top: 12px; left: 12px; border-top: 2px solid var(--color-gold); border-left: 2px solid var(--color-gold); border-top-left-radius: 12px; }
    .corner-tr { top: 12px; right: 12px; border-top: 2px solid var(--color-gold); border-right: 2px solid var(--color-gold); border-top-right-radius: 12px; }
    .corner-bl { bottom: 12px; left: 12px; border-bottom: 2px solid var(--color-gold); border-left: 2px solid var(--color-gold); border-bottom-left-radius: 12px; }
    .corner-br { bottom: 12px; right: 12px; border-bottom: 2px solid var(--color-gold); border-right: 2px solid var(--color-gold); border-bottom-right-radius: 12px; }

    .envelope-floral-bottom {
      position: absolute;
      bottom: -10px;
      right: -10px;
      width: 190px;
      opacity: 0.85;
      pointer-events: none;
      z-index: 2;
    }

    .envelope-floral-bottom img {
      width: 100%;
      height: auto;
      filter: drop-shadow(0 4px 10px rgba(0,0,0,0.15));
    }

    /* Envelope Face Typography */
    .envelope-face-content {
      position: relative;
      z-index: 4;
      margin-top: 240px;
      text-align: center;
      color: var(--color-charcoal);
      width: 100%;
    }

    @media (max-width: 420px) {
      .envelope-face-content {
        margin-top: 220px;
      }
    }

    .envelope-ganesh-small {
      font-family: var(--font-devanagari);
      font-size: 15px;
      font-weight: 700;
      color: var(--color-gold-dark);
      letter-spacing: 2px;
      margin-bottom: 4px;
    }

    .envelope-couple-names {
      font-family: var(--font-heading);
      font-size: 27px;
      font-weight: 700;
      color: var(--color-maroon);
      letter-spacing: 0.5px;
      margin-bottom: 2px;
      line-height: 1.15;
    }

    .envelope-date-sub {
      font-family: var(--font-heading);
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 2.2px;
      text-transform: uppercase;
      color: var(--color-gold-dark);
      margin-bottom: 12px;
    }

    .envelope-filigree-divider {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      color: var(--color-gold);
      margin-bottom: 8px;
      font-size: 13px;
    }

    .envelope-filigree-divider .filigree-line {
      height: 1px;
      width: 44px;
      background: linear-gradient(90deg, transparent, var(--color-gold), transparent);
    }

    .envelope-invited-title {
      font-family: var(--font-heading);
      font-size: 21px;
      font-weight: 800;
      letter-spacing: 4px;
      color: var(--color-maroon);
      text-transform: uppercase;
      margin-bottom: 4px;
    }

    .envelope-invited-caption {
      font-family: var(--font-heading);
      font-style: italic;
      font-size: 14px;
      color: var(--color-charcoal-muted);
      max-width: 280px;
      margin: 0 auto;
      line-height: 1.4;
    }

    /* 3D Top Triangular Envelope Flap */
    .envelope-flap-top {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 165px;
      z-index: 10;
      transform-origin: top center;
      transition: transform 0.9s cubic-bezier(0.4, 0, 0.2, 1);
      pointer-events: none;
    }

    .envelope-flap-top .flap-outer-tri {
      width: 100%;
      height: 100%;
      background: linear-gradient(180deg, #ECDCC8 0%, #F6EEE0 65%, #EDE2D1 100%);
      clip-path: polygon(0 0, 100% 0, 50% 100%);
      border-top-left-radius: 18px;
      border-top-right-radius: 18px;
      filter: drop-shadow(0 10px 16px rgba(61, 16, 28, 0.4));
      border-bottom: 1.5px solid rgba(197, 161, 91, 0.55);
    }

    /* Inside Card Sliding Up */
    .envelope-inside-card {
      position: absolute;
      top: 24px;
      left: 14px;
      right: 14px;
      height: 440px;
      background: #FFFFFF;
      border-radius: 14px;
      border: 1.5px solid var(--color-gold);
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35);
      z-index: 5;
      opacity: 0;
      transform: translateY(30px);
      transition: transform 0.9s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.6s ease;
      pointer-events: none;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 30px 20px;
      box-sizing: border-box;
    }

    .inside-card-border {
      border: 1px solid rgba(197, 161, 91, 0.4);
      border-radius: 10px;
      padding: 24px 16px;
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      background: radial-gradient(circle at center, #FFFFFF 0%, #FAF5EA 100%);
    }

    .inside-card-invoc {
      font-family: var(--font-devanagari);
      font-size: 15px;
      font-weight: 700;
      color: var(--color-gold-dark);
      margin-bottom: 6px;
    }

    .inside-card-title {
      font-family: var(--font-heading);
      font-size: 16px;
      letter-spacing: 2px;
      color: var(--color-maroon);
      text-transform: uppercase;
      font-weight: 700;
      margin-bottom: 8px;
    }

    .inside-card-names {
      font-family: var(--font-heading);
      font-size: 26px;
      font-weight: 700;
      color: var(--color-burgundy);
      margin-bottom: 4px;
    }

    .inside-card-date {
      font-family: var(--font-heading);
      font-size: 13px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--color-gold-dark);
      font-weight: 700;
      margin-bottom: 4px;
    }

    .inside-card-church {
      font-family: var(--font-body);
      font-size: 12.5px;
      color: var(--color-charcoal-muted);
    }

    /* 3D Wax Seal Positioned at Flap Apex */
    .vintage-wax-seal {
      position: absolute;
      top: 130px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 25;
      width: 76px;
      height: 76px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
      user-select: none;
    }

    .vintage-wax-seal:hover {
      transform: translateX(-50%) scale(1.08);
    }

    .wax-seal-outer-rim {
      width: 100%;
      height: 100%;
      border-radius: 49% 51% 52% 48% / 51% 49% 51% 49%;
      background: radial-gradient(circle at 35% 32%, #A32840 0%, #7D1B2E 35%, #520F1D 70%, #300610 100%);
      box-shadow: inset 2.5px 2.5px 6px rgba(255, 255, 255, 0.45), inset -3.5px -3.5px 7px rgba(0, 0, 0, 0.75), 0 10px 28px rgba(0, 0, 0, 0.7), 0 0 25px rgba(100, 29, 45, 0.6);
      border: 2px solid rgba(226, 204, 160, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }

    .wax-seal-inner-emboss {
      width: 50px;
      height: 50px;
      border-radius: 50%;
      border: 1.5px dashed rgba(226, 204, 160, 0.6);
      background: radial-gradient(circle at 40% 40%, rgba(100, 29, 45, 0.85) 0%, rgba(61, 16, 28, 0.95) 100%);
      box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.6), 0 1px 2px rgba(255, 255, 255, 0.2);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

    .wax-seal-crest-crown {
      font-size: 13px;
      color: var(--color-gold);
      line-height: 1;
      margin-bottom: -2px;
      filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.5));
    }

    .wax-seal-monogram {
      font-family: var(--font-devanagari);
      font-weight: 800;
      font-size: 14px;
      letter-spacing: 1px;
      background: linear-gradient(135deg, #FFF0CA 0%, #C5A15B 50%, #9A7B38 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.7));
    }

    .wax-seal-ping {
      position: absolute;
      inset: -8px;
      border-radius: 50%;
      border: 2px solid var(--color-gold);
      opacity: 0.75;
      animation: waxPulsePing 2s cubic-bezier(0, 0, 0.2, 1) infinite;
      pointer-events: none;
    }

    @keyframes waxPulsePing {
      0% { transform: scale(0.92); opacity: 0.85; }
      70% { transform: scale(1.35); opacity: 0; }
      100% { transform: scale(1.35); opacity: 0; }
    }

    .wax-seal-tooltip {
      position: absolute;
      bottom: -32px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(61, 16, 28, 0.94);
      border: 1px solid var(--color-gold-40);
      border-radius: 9999px;
      padding: 4px 14px;
      display: flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
      font-family: var(--font-heading);
      font-size: 12px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--color-gold-light);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.6);
      animation: tooltipBounce 1.8s ease-in-out infinite;
      pointer-events: none;
    }

    @keyframes tooltipBounce {
      0%, 100% { transform: translateX(-50%) translateY(0); }
      50% { transform: translateX(-50%) translateY(4px); }
    }

    /* Unsealed Active Animations */
    .envelope-3d-scene.unsealed .envelope-flap-top {
      transform: rotateX(180deg);
      z-index: 1;
    }

    .envelope-3d-scene.unsealed .envelope-flap-top .flap-outer-tri {
      background: linear-gradient(180deg, #DED0BC 0%, #ECDCC8 100%);
      filter: drop-shadow(0 -6px 12px rgba(61, 16, 28, 0.3));
    }

    .envelope-3d-scene.unsealed .vintage-wax-seal {
      animation: waxCrackBreak 0.7s forwards cubic-bezier(0.2, 0.8, 0.2, 1);
      pointer-events: none;
    }

    @keyframes waxCrackBreak {
      0% { transform: translateX(-50%) scale(1); opacity: 1; }
      40% { transform: translateX(-50%) scale(1.22); filter: brightness(1.4); }
      100% { transform: translateX(-50%) scale(1.4) translateY(-20px); opacity: 0; visibility: hidden; }
    }

    .envelope-3d-scene.unsealed .envelope-inside-card {
      opacity: 1;
      transform: translateY(-80px);
      z-index: 15;
    }

    /* ==========================================================================
       SECTION 4: CINEMATIC MAHARASHTRIAN WEDDING HERO
       ========================================================================== */
    .hero-website-cover {
      min-height: clamp(680px, 100vh, 920px);
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 90px 24px;
      background: radial-gradient(circle at 50% 40%, rgba(100, 29, 45, 0.25) 0%, rgba(61, 16, 28, 0.85) 60%, #20060C 100%);
      overflow: hidden;
    }

    .hero-bg-media {
      position: absolute;
      inset: 0;
      z-index: 1;
      opacity: 0.32;
    }

    .hero-bg-media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      filter: blur(2px);
    }

    .hero-cover-container {
      position: relative;
      z-index: 3;
      width: 100%;
      max-width: 860px;
      text-align: center;
      background: rgba(41, 10, 18, 0.88);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--color-gold-40);
      border-radius: 32px;
      padding: 60px 40px 50px;
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.8), 0 0 60px rgba(100, 29, 45, 0.4);
    }

    @media (max-width: 576px) {
      .hero-cover-container {
        padding: 42px 20px 36px;
        border-radius: 24px;
      }
    }

    .hero-crest-badge {
      width: 84px;
      height: 84px;
      margin: 0 auto 18px;
      border-radius: 50%;
      border: 2px solid var(--color-gold);
      padding: 4px;
      background: #FFFFFF;
      box-shadow: 0 0 30px rgba(197, 161, 91, 0.4);
    }

    .hero-invoc-mr {
      font-family: var(--font-devanagari);
      font-size: clamp(1.4rem, 3vw, 1.85rem);
      font-weight: 700;
      color: var(--color-gold-light);
      letter-spacing: 3px;
      margin-bottom: 6px;
      text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
    }

    .hero-couple-title {
      font-family: var(--font-heading);
      font-size: clamp(2.8rem, 7.5vw, 5.4rem);
      font-weight: 700;
      line-height: 1.05;
      letter-spacing: 1px;
      margin: 8px 0;
      color: #FFFFFF;
    }

    .hero-couple-title span.amp {
      font-family: var(--font-script);
      font-size: 0.88em;
      color: var(--color-gold);
      margin: 0 10px;
    }

    .hero-tagline {
      font-family: var(--font-heading);
      font-style: italic;
      font-size: 1.25rem;
      color: var(--color-gold-pale);
      margin-bottom: 24px;
    }

    .hero-date-venue-capsule {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: rgba(30, 8, 14, 0.85);
      border: 1px solid var(--color-gold-40);
      padding: 10px 28px;
      border-radius: 9999px;
      font-family: var(--font-heading);
      font-size: 0.95rem;
      letter-spacing: 2px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--color-gold-light);
      margin-bottom: 30px;
    }

    /* Live Countdown Grid */
    .countdown-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      max-width: 480px;
      margin: 0 auto 32px;
    }

    @media (max-width: 480px) {
      .countdown-grid {
        gap: 10px;
      }
    }

    .countdown-box {
      background: rgba(20, 4, 8, 0.7);
      border: 1px solid var(--color-gold-20);
      border-radius: 16px;
      padding: 14px 8px;
      text-align: center;
    }

    .countdown-num {
      font-family: var(--font-heading);
      font-size: clamp(1.8rem, 4vw, 2.6rem);
      font-weight: 700;
      color: var(--color-gold-light);
      line-height: 1;
      margin-bottom: 4px;
    }

    .countdown-lbl {
      font-family: var(--font-body);
      font-size: 11px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #D3C4BC;
      font-weight: 500;
    }

    /* ==========================================================================
       SECTION 5: GANESH INVOCATION & DEVOTIONAL SANCTUARY
       ========================================================================== */
    .ganesh-blessing-section {
      background: radial-gradient(circle at 50% 50%, #FFFDF9 0%, var(--color-ivory) 100%);
      position: relative;
      overflow: hidden;
      border-top: 1px solid var(--color-beige);
      border-bottom: 1px solid var(--color-beige);
    }

    .ganesh-blessing-showcase {
      max-width: 860px;
      margin: 0 auto;
      background: #FFFFFF;
      border: 1px solid var(--color-gold-40);
      border-radius: 28px;
      padding: 48px 32px;
      box-shadow: 0 20px 60px rgba(100, 29, 45, 0.08), 0 0 40px rgba(197, 161, 91, 0.12);
    }

    .theme5-ganesh-frame {
      position: relative;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }

    .ganesh-radiance-aura {
      position: absolute;
      width: 260px;
      height: 260px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(197, 161, 91, 0.28) 0%, rgba(226, 204, 160, 0.15) 50%, transparent 75%);
      filter: blur(16px);
      animation: auraBreathe 4s infinite alternate ease-in-out;
      pointer-events: none;
    }

    .ganesh-central-img {
      max-height: 220px;
      width: auto;
      display: block;
      position: relative;
      z-index: 2;
      filter: drop-shadow(0 0 25px rgba(197, 161, 91, 0.45));
      transition: transform 0.4s ease;
    }

    .ganesh-central-img:hover {
      transform: scale(1.04);
    }

    .diya-glow-img {
      max-height: 125px;
      width: auto;
      display: block;
      filter: drop-shadow(0 0 18px rgba(197, 161, 91, 0.5));
    }

    .sanskrit-chant {
      font-family: var(--font-devanagari);
      font-size: clamp(1.4rem, 3.5vw, 2.1rem);
      font-weight: 700;
      color: var(--color-maroon);
      letter-spacing: 2px;
    }

    .translit-chant {
      font-family: var(--font-heading);
      font-size: 1.15rem;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--color-gold-dark);
      font-weight: 700;
      margin-top: 4px;
    }

    .blessing-mantra-text {
      font-family: var(--font-heading);
      font-style: italic;
      font-size: 1.18rem;
      color: var(--color-charcoal-muted);
      max-width: 600px;
      margin: 14px auto 0;
      line-height: 1.65;
    }

    /* ==========================================================================
       SECTION 6: MEET THE BRIDE & GROOM (वधू आणि वर)
       ========================================================================== */
    .couple-cards-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 36px;
      max-width: 960px;
      margin: 0 auto;
    }

    @media (max-width: 768px) {
      .couple-cards-grid {
        grid-template-columns: 1fr;
        gap: 28px;
      }
    }

    .couple-portrait-card {
      background: #FFFFFF;
      border: 1px solid var(--color-gold-40);
      border-radius: 24px;
      padding: 36px 30px 32px;
      text-align: center;
      box-shadow: 0 16px 45px rgba(100, 29, 45, 0.08);
      transition: var(--transition-smooth);
    }

    .couple-portrait-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 22px 55px rgba(100, 29, 45, 0.14);
      border-color: var(--color-gold);
    }

    .couple-avatar-decor {
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 14px;
    }

    .couple-avatar-img {
      width: 58px;
      height: 58px;
      border-radius: 50%;
      border: 2px solid var(--color-gold);
      box-shadow: 0 0 16px rgba(197, 161, 91, 0.35);
      background: var(--color-ivory);
      padding: 3px;
    }

    .portrait-frame {
      width: 100%;
      max-width: 320px;
      height: 380px;
      border-radius: 18px;
      overflow: hidden;
      margin: 0 auto 20px;
      position: relative;
      border: 1px solid var(--color-beige);
    }

    .portrait-frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
    }

    .couple-portrait-card:hover .portrait-frame img {
      transform: scale(1.04);
    }

    .role-badge-pill {
      position: absolute;
      bottom: 14px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(61, 16, 28, 0.90);
      color: var(--color-gold-light);
      border: 1px solid var(--color-gold-40);
      border-radius: 9999px;
      padding: 5px 18px;
      font-family: var(--font-heading);
      font-size: 13px;
      letter-spacing: 2px;
      text-transform: uppercase;
      font-weight: 700;
      white-space: nowrap;
    }

    .couple-person-name {
      font-family: var(--font-heading);
      font-size: 2rem;
      font-weight: 700;
      color: var(--color-maroon);
      margin-bottom: 4px;
    }

    .couple-person-parents {
      font-family: var(--font-heading);
      font-size: 1.05rem;
      color: var(--color-gold-dark);
      margin-bottom: 14px;
      font-style: italic;
    }

    .couple-personal-vow {
      font-family: var(--font-body);
      font-size: 0.96rem;
      color: var(--color-charcoal-muted);
      line-height: 1.65;
    }

    /* ==========================================================================
       SECTION 7: OUR LOVE STORY (आमची प्रेमकथा)
       ========================================================================== */
    .story-timeline-container {
      max-width: 900px;
      margin: 0 auto;
      position: relative;
    }

    .story-timeline-container::before {
      content: "";
      position: absolute;
      top: 0;
      bottom: 0;
      left: 50%;
      width: 2px;
      background: linear-gradient(180deg, transparent, var(--color-gold) 15%, var(--color-gold) 85%, transparent);
      transform: translateX(-50%);
    }

    @media (max-width: 768px) {
      .story-timeline-container::before {
        left: 20px;
      }
    }

    .story-item {
      display: flex;
      align-items: center;
      margin-bottom: 60px;
      position: relative;
    }

    .story-item:nth-child(even) {
      flex-direction: row-reverse;
    }

    @media (max-width: 768px) {
      .story-item, .story-item:nth-child(even) {
        flex-direction: column;
        align-items: flex-start;
        padding-left: 48px;
        margin-bottom: 44px;
      }
    }

    .story-content-box {
      width: 44%;
      background: #FFFFFF;
      border: 1px solid var(--color-gold-40);
      border-radius: 20px;
      padding: 24px;
      box-shadow: 0 12px 35px rgba(100, 29, 45, 0.06);
    }

    @media (max-width: 768px) {
      .story-content-box {
        width: 100%;
        padding: 20px;
      }
    }

    .story-img-frame {
      width: 100%;
      height: 200px;
      border-radius: 14px;
      overflow: hidden;
      margin-bottom: 16px;
    }

    .story-img-frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .story-chapter-tag {
      font-family: var(--font-heading);
      font-size: 12px;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      color: var(--color-gold);
      font-weight: 700;
    }

    .story-chapter-title {
      font-family: var(--font-heading);
      font-size: 1.6rem;
      font-weight: 700;
      color: var(--color-maroon);
      margin: 4px 0 8px;
    }

    .story-timeline-marker {
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--color-maroon);
      border: 2px solid var(--color-gold);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--color-gold-light);
      font-size: 14px;
      z-index: 2;
      box-shadow: 0 0 16px rgba(197, 161, 91, 0.4);
    }

    @media (max-width: 768px) {
      .story-timeline-marker {
        left: 20px;
        top: 0;
      }
    }

    /* ==========================================================================
       SECTION 8: AUTHENTIC MARATHI HINDU WEDDING CEREMONIES (आमचे मंगल सोहळे)
       ========================================================================== */
    .rituals-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      max-width: 1120px;
      margin: 0 auto;
    }

    @media (max-width: 992px) {
      .rituals-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (max-width: 600px) {
      .rituals-grid {
        grid-template-columns: 1fr;
      }
    }

    .ritual-card {
      background: #FFFFFF;
      border: 1px solid var(--color-gold-40);
      border-radius: 20px;
      padding: 28px 24px;
      transition: var(--transition-smooth);
      position: relative;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 30px rgba(100, 29, 45, 0.05);
    }

    .ritual-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 16px 40px rgba(100, 29, 45, 0.12);
      border-color: var(--color-gold);
    }

    .ritual-number {
      font-family: var(--font-heading);
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--color-gold);
      margin-bottom: 6px;
    }

    .ritual-title-mr {
      font-family: var(--font-devanagari);
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--color-maroon);
      margin-bottom: 2px;
    }

    .ritual-title-en {
      font-family: var(--font-heading);
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--color-gold-dark);
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 12px;
    }

    .ritual-desc {
      font-size: 0.94rem;
      color: var(--color-charcoal-muted);
      line-height: 1.6;
    }

    /* ==========================================================================
       SECTION 9: WEDDING EVENT TIMELINE (विवाह कार्यक्रम पत्रिका)
       ========================================================================== */
    .events-editorial-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 26px;
      max-width: 1140px;
      margin: 0 auto;
    }

    @media (max-width: 992px) {
      .events-editorial-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (max-width: 640px) {
      .events-editorial-grid {
        grid-template-columns: 1fr;
      }
    }

    .event-editorial-card {
      background: #FFFFFF;
      border: 1px solid var(--color-gold-40);
      border-radius: 22px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 12px 35px rgba(100, 29, 45, 0.06);
      transition: var(--transition-smooth);
    }

    .event-editorial-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 18px 45px rgba(100, 29, 45, 0.12);
      border-color: var(--color-gold);
    }

    .event-media-cover {
      width: 100%;
      height: 220px;
      position: relative;
      overflow: hidden;
    }

    .event-media-cover img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }

    .event-editorial-card:hover .event-media-cover img {
      transform: scale(1.05);
    }

    .event-time-badge {
      position: absolute;
      bottom: 12px;
      left: 14px;
      background: rgba(61, 16, 28, 0.90);
      color: var(--color-gold-light);
      border: 1px solid var(--color-gold-40);
      border-radius: 9999px;
      padding: 5px 14px;
      font-family: var(--font-heading);
      font-size: 12.5px;
      font-weight: 700;
      letter-spacing: 1.5px;
    }

    .event-card-body {
      padding: 24px 20px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }

    .event-title-mr {
      font-family: var(--font-devanagari);
      font-size: 1.45rem;
      font-weight: 700;
      color: var(--color-maroon);
      margin-bottom: 2px;
    }

    .event-title-en {
      font-family: var(--font-heading);
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--color-gold-dark);
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 8px;
    }

    .event-venue-meta {
      font-size: 0.88rem;
      color: var(--color-charcoal-muted);
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 12px;
    }

    .event-desc-text {
      font-size: 0.93rem;
      color: var(--color-charcoal-muted);
      line-height: 1.6;
      margin-bottom: 18px;
      flex-grow: 1;
    }

    .event-attire-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--color-beige);
      padding-top: 14px;
      font-size: 12.5px;
      color: var(--color-maroon);
      font-weight: 600;
    }

    /* ==========================================================================
       SECTION 10: MAHARASHTRIAN WEDDING DRESS CODE (पोषाख मार्गदर्शिका)
       ========================================================================== */
    .dresscode-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 26px;
      max-width: 1040px;
      margin: 0 auto;
    }

    @media (max-width: 768px) {
      .dresscode-grid {
        grid-template-columns: 1fr;
      }
    }

    .dresscode-card {
      background: #FFFFFF;
      border: 1px solid var(--color-gold-40);
      border-radius: 22px;
      padding: 32px 24px;
      text-align: center;
      box-shadow: 0 10px 30px rgba(100, 29, 45, 0.05);
    }

    .dresscode-icon {
      font-size: 2.2rem;
      color: var(--color-gold);
      margin-bottom: 12px;
    }

    .dresscode-title {
      font-family: var(--font-heading);
      font-size: 1.6rem;
      font-weight: 700;
      color: var(--color-maroon);
      margin-bottom: 8px;
    }

    .dresscode-items-list {
      list-style: none;
      padding: 0;
      margin: 16px 0 0;
      font-size: 0.94rem;
      color: var(--color-charcoal-muted);
      line-height: 1.8;
    }

    /* Palette Swatches */
    .palette-swatches-wrap {
      display: flex;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
      margin-top: 36px;
    }

    .swatch-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #FFFFFF;
      border: 1px solid var(--color-gold-40);
      border-radius: 9999px;
      padding: 6px 16px 6px 6px;
      font-size: 12.5px;
      font-weight: 600;
      color: var(--color-charcoal);
    }

    .swatch-dot {
      width: 22px;
      height: 22px;
      border-radius: 50%;
      border: 1px solid rgba(0,0,0,0.1);
    }

    /* ==========================================================================
       SECTION 12: LUXURY EDITORIAL PHOTO GALLERY WITH LIGHTBOX (क्षणचित्रे)
       ========================================================================== */
    .gallery-filter-buttons {
      display: flex;
      justify-content: center;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 36px;
    }

    .gallery-tab-btn {
      background: transparent;
      border: 1px solid var(--color-gold-40);
      color: var(--color-charcoal-muted);
      font-family: var(--font-heading);
      font-size: 14.5px;
      font-weight: 600;
      letter-spacing: 1px;
      padding: 8px 22px;
      border-radius: 9999px;
      cursor: pointer;
      transition: var(--transition-smooth);
    }

    .gallery-tab-btn:hover, .gallery-tab-btn.active {
      background: var(--color-maroon);
      color: var(--color-ivory);
      border-color: var(--color-maroon);
    }

    .gallery-masonry-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      max-width: 1140px;
      margin: 0 auto;
    }

    @media (max-width: 992px) {
      .gallery-masonry-grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    @media (max-width: 640px) {
      .gallery-masonry-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 14px;
      }
    }

    .gallery-item-tile {
      position: relative;
      border-radius: 16px;
      overflow: hidden;
      cursor: pointer;
      box-shadow: 0 8px 24px rgba(100, 29, 45, 0.08);
      aspect-ratio: 4/5;
    }

    .gallery-item-tile.tall {
      aspect-ratio: 3/4.2;
    }

    .gallery-item-tile.wide {
      grid-column: span 2;
      aspect-ratio: 16/9;
    }

    @media (max-width: 640px) {
      .gallery-item-tile.wide {
        grid-column: span 1;
        aspect-ratio: 4/5;
      }
    }

    .gallery-item-tile img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .gallery-item-tile:hover img {
      transform: scale(1.06);
    }

    .gallery-item-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, transparent 40%, rgba(61, 16, 28, 0.90) 100%);
      opacity: 0;
      transition: opacity 0.3s ease;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 18px 16px;
      color: #FFFFFF;
    }

    .gallery-item-tile:hover .gallery-item-overlay {
      opacity: 1;
    }

    .gallery-overlay-caption {
      font-family: var(--font-heading);
      font-size: 1.05rem;
      font-weight: 600;
    }

    .gallery-overlay-tag {
      font-size: 11px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--color-gold-light);
    }

    /* Lightbox Modal */
    .editorial-lightbox-modal {
      position: fixed;
      inset: 0;
      z-index: 100000;
      background: rgba(20, 4, 8, 0.96);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.3s ease, visibility 0.3s ease;
    }

    .editorial-lightbox-modal.active {
      opacity: 1;
      visibility: visible;
    }

    .lightbox-dialog {
      position: relative;
      max-width: 900px;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    .lightbox-img-frame {
      max-height: 75vh;
      max-width: 90vw;
      border-radius: 14px;
      overflow: hidden;
      border: 1px solid var(--color-gold-40);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8);
    }

    .lightbox-img-frame img {
      max-height: 75vh;
      max-width: 90vw;
      object-fit: contain;
    }

    .lightbox-meta-caption {
      font-family: var(--font-heading);
      font-size: 1.25rem;
      color: var(--color-ivory);
      margin-top: 14px;
      font-style: italic;
    }

    .lightbox-btn-close {
      position: absolute;
      top: 20px;
      right: 24px;
      background: transparent;
      border: none;
      color: var(--color-ivory);
      font-size: 2.2rem;
      cursor: pointer;
      z-index: 10;
      transition: color 0.2s ease;
    }

    .lightbox-btn-close:hover {
      color: var(--color-gold);
    }

    .lightbox-btn-nav {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(61, 16, 28, 0.7);
      border: 1px solid var(--color-gold-40);
      color: var(--color-ivory);
      width: 48px;
      height: 48px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
      cursor: pointer;
      transition: var(--transition-smooth);
      z-index: 10;
    }

    .lightbox-btn-nav:hover {
      background: var(--color-maroon);
      border-color: var(--color-gold);
    }

    .lightbox-btn-prev { left: 24px; }
    .lightbox-btn-next { right: 24px; }

    /* ==========================================================================
       SECTION 13: FAMILY BLESSINGS (आशीर्वाद)
       ========================================================================== */
    .blessings-quotes-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 30px;
      max-width: 960px;
      margin: 0 auto;
    }

    @media (max-width: 768px) {
      .blessings-quotes-grid {
        grid-template-columns: 1fr;
      }
    }

    .blessing-quote-card {
      background: #FFFFFF;
      border: 1px solid var(--color-gold-40);
      border-radius: 22px;
      padding: 34px 28px;
      box-shadow: 0 10px 30px rgba(100, 29, 45, 0.05);
      position: relative;
    }

    .blessing-quote-text {
      font-family: var(--font-heading);
      font-style: italic;
      font-size: 1.15rem;
      color: var(--color-charcoal);
      line-height: 1.7;
      margin-bottom: 18px;
    }

    .blessing-author-name {
      font-family: var(--font-devanagari);
      font-weight: 700;
      font-size: 1.1rem;
      color: var(--color-maroon);
    }

    .blessing-author-relation {
      font-size: 12.5px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--color-gold-dark);
      font-weight: 600;
    }

    /* ==========================================================================
       SECTION 14: RSVP EXPERIENCE (उपस्थिती नोंदणी)
       ========================================================================== */
    .rsvp-editorial-card {
      background: #FFFFFF;
      border: 1px solid var(--color-gold-40);
      border-radius: 28px;
      padding: 50px 42px;
      box-shadow: 0 20px 60px rgba(100, 29, 45, 0.08);
      max-width: 780px;
      margin: 0 auto;
    }

    @media (max-width: 576px) {
      .rsvp-editorial-card {
        padding: 36px 20px;
        border-radius: 20px;
      }
    }

    .form-group-custom {
      margin-bottom: 20px;
      text-align: left;
    }

    .form-label-custom {
      font-family: var(--font-heading);
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--color-maroon);
      margin-bottom: 6px;
      display: block;
    }

    .form-input-custom {
      width: 100%;
      background: var(--color-ivory);
      border: 1px solid var(--color-beige);
      border-radius: 12px;
      padding: 12px 16px;
      font-family: var(--font-body);
      font-size: 14.5px;
      color: var(--color-charcoal);
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    .form-input-custom:focus {
      border-color: var(--color-gold);
      box-shadow: 0 0 0 3px rgba(197, 161, 91, 0.25);
      outline: none;
      background: #FFFFFF;
    }

    /* Attendance Radio Buttons */
    .attendance-btn-group {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-bottom: 20px;
    }

    .attendance-option {
      position: relative;
    }

    .attendance-option input[type="radio"] {
      position: absolute;
      opacity: 0;
      width: 0;
      height: 0;
    }

    .attendance-option label {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 13px 16px;
      background: var(--color-ivory);
      border: 1.5px solid var(--color-beige);
      border-radius: 12px;
      cursor: pointer;
      font-family: var(--font-body);
      font-weight: 600;
      font-size: 14px;
      color: var(--color-charcoal-muted);
      transition: var(--transition-smooth);
    }

    .attendance-option input[type="radio"]:checked + label {
      background: var(--color-maroon);
      color: var(--color-ivory);
      border-color: var(--color-maroon);
      box-shadow: 0 4px 16px rgba(100, 29, 45, 0.25);
    }

    /* ==========================================================================
       SECTION 15: VENUE & LOCATION (स्थळ व प्रवास)
       ========================================================================== */
    .venue-showcase-card {
      background: #FFFFFF;
      border: 1px solid var(--color-gold-40);
      border-radius: 28px;
      overflow: hidden;
      max-width: 1040px;
      margin: 0 auto;
      box-shadow: 0 16px 50px rgba(100, 29, 45, 0.08);
    }

    .venue-media-banner {
      width: 100%;
      height: 340px;
      position: relative;
    }

    .venue-media-banner img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .venue-content-padding {
      padding: 44px 36px;
    }

    @media (max-width: 576px) {
      .venue-content-padding {
        padding: 30px 20px;
      }
    }

    .venue-amenities-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin: 30px 0;
      text-align: left;
    }

    @media (max-width: 768px) {
      .venue-amenities-grid {
        grid-template-columns: 1fr;
      }
    }

    .amenity-box {
      background: var(--color-ivory);
      border: 1px solid var(--color-beige);
      border-radius: 14px;
      padding: 18px;
    }

    .amenity-title {
      font-family: var(--font-heading);
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--color-maroon);
      margin-bottom: 4px;
    }

    /* ==========================================================================
       SECTION 17: CLOSING SECTION (॥ शुभमंगल सावधान ॥) & FOOTER
       ========================================================================== */
    .closing-finale-section {
      background: linear-gradient(180deg, #3D101C 0%, #20060C 100%);
      color: var(--color-ivory);
      padding: 90px 24px 60px;
      text-align: center;
      position: relative;
      overflow: hidden;
    }

    .closing-benediction {
      font-family: var(--font-devanagari);
      font-size: clamp(2rem, 5vw, 3.4rem);
      font-weight: 800;
      color: var(--color-gold-light);
      letter-spacing: 4px;
      margin-bottom: 12px;
      text-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
    }

    .closing-names {
      font-family: var(--font-heading);
      font-size: clamp(2.4rem, 6vw, 4rem);
      font-weight: 700;
      margin-bottom: 16px;
      color: #FFFFFF;
    }

    .closing-desc {
      font-family: var(--font-heading);
      font-style: italic;
      font-size: 1.25rem;
      color: var(--color-gold-pale);
      max-width: 620px;
      margin: 0 auto 36px;
      line-height: 1.6;
    }

    /* Toast Notification */
    .global-toast {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: rgba(61, 16, 28, 0.95);
      border: 1px solid var(--color-gold);
      color: var(--color-gold-light);
      padding: 12px 28px;
      border-radius: 9999px;
      font-family: var(--font-heading);
      font-size: 15px;
      font-weight: 600;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
      z-index: 100000;
      opacity: 0;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      pointer-events: none;
    }

    .global-toast.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }
  </style>
</head>
<body>

  <!-- ==========================================================================
       SECTION 3: ROYAL MAHARASHTRIAN INVITATION ENVELOPE (Zareqia 3D Entrance)
       ========================================================================== -->
  <div id="envelopeEntranceOverlay" class="envelope-entrance-overlay">
    <div class="envelope-intro-wrapper">
      <!-- Top Hint Badge -->
      <div class="text-center mb-2">
        <span class="envelope-hint-badge">
          <i class="bi bi-envelope-paper-heart me-1"></i> निमंत्रण पत्रिका • Special Wedding Invitation
        </span>
      </div>

      <!-- 3D Envelope Scene -->
      <div class="envelope-3d-scene" id="envelopeScene">
        <div class="vintage-envelope" id="vintageEnvelope">
          
          <!-- Paithani Corner Accents -->
          <div class="envelope-corner-ornament corner-tl"></div>
          <div class="envelope-corner-ornament corner-tr"></div>
          <div class="envelope-corner-ornament corner-bl"></div>
          <div class="envelope-corner-ornament corner-br"></div>

          <!-- Floral Bottom Vignette -->
          <div class="envelope-floral-bottom">
            <img src="images/rose_bottom_clean.png" alt="Floral Decoration" onerror="this.style.display='none'">
          </div>

          <!-- Envelope Face Content (Cleanly Placed Below Wax Seal) -->
          <div class="envelope-face-content">
            <div class="envelope-ganesh-small">॥ श्री गणेशाय नमः ॥</div>
            <div class="envelope-couple-names">Kasandra &amp; Imanule</div>
            <div class="envelope-date-sub">Saturday, October 19, 2027 • The White Church</div>

            <div class="envelope-filigree-divider">
              <span class="filigree-line"></span>
              <span class="filigree-symbol">❧ ❦ ☙</span>
              <span class="filigree-line"></span>
            </div>

            <div class="envelope-invited-title">निमंत्रण पत्रिका</div>
            <p class="envelope-invited-caption">
              With the divine blessings of Lord Ganesha and our beloved families, we joyfully invite you.
            </p>
          </div>

          <!-- Inside Letter Card (Slides Up on Unseal) -->
          <div class="envelope-inside-card" id="envelopeInsideCard">
            <div class="inside-card-border">
              <div class="inside-card-invoc">॥ श्री गणेशाय नमः ॥</div>
              <div class="inside-card-title">You Are Cordially Invited</div>
              <p class="inside-card-names">Kasandra &amp; Imanule</p>
              <div class="inside-card-date">Saturday, October 19, 2027</div>
              <p class="inside-card-church">The White Church • 125 Rd</p>
              <div style="color: var(--color-gold); font-size: 13px; letter-spacing: 5px; margin-top: 10px;">✦ ✦ ✦</div>
            </div>
          </div>

          <!-- 3D Top Triangular Envelope Flap -->
          <div class="envelope-flap-top" id="envelopeFlapTop">
            <div class="flap-outer-tri"></div>
          </div>

          <!-- 3D Wax Seal Positioned at Flap Apex -->
          <div class="vintage-wax-seal" id="vintageWaxSeal" role="button" tabindex="0" title="Click to break seal and open invitation">
            <div class="wax-seal-outer-rim">
              <div class="wax-seal-inner-emboss">
                <span class="wax-seal-crest-crown">♔</span>
                <span class="wax-seal-monogram">॥ श्री ॥</span>
              </div>
            </div>
            <div class="wax-seal-ping"></div>
            <div class="wax-seal-tooltip">
              <span>Tap to Open</span>
              <i class="bi bi-hand-index-thumb-fill"></i>
            </div>
          </div>

        </div>
      </div>

      <!-- Bottom Envelope Actions Bar -->
      <div class="text-center mt-3">
        <button type="button" class="btn-gold" id="btnEnvelopeOpen">
          <i class="bi bi-envelope-open me-2"></i> Open Invitation
        </button>
        <div class="mt-2">
          <button type="button" class="btn" style="color: var(--color-gold-light); font-size: 13px; letter-spacing: 1px;" id="btnEnvelopeSkip">
            Skip to Celebration &rarr;
          </button>
        </div>
      </div>

    </div>
  </div>

  <!-- Floating Audio Soundwave Capsule (No Header & No Navbar) -->
  <button type="button" class="floating-audio-pill" id="audioToggleBtn" title="Toggle Traditional Shehnai &amp; Raga Soundtrack">
    <div class="audio-waves">
      <span class="audio-wave-bar"></span>
      <span class="audio-wave-bar"></span>
      <span class="audio-wave-bar"></span>
    </div>
    <span class="audio-label" id="audioLabel">Shehnai &amp; Raga</span>
  </button>

  <!-- ==========================================================================
       SECTION 4: CINEMATIC MAHARASHTRIAN WEDDING HERO
       ========================================================================== -->
  <section class="hero-website-cover" id="hero">
    <div class="hero-bg-media">
      <img src="images/hero_couple.jpg" alt="Kasandra &amp; Imanule">
    </div>

    <div class="hero-cover-container">
      <div class="hero-crest-badge">
        <img src="images/wedding_crest.svg" alt="Royal Crest" style="width: 100%; height: 100%;">
      </div>

      <div class="hero-invoc-mr">॥ शुभ विवाह ॥</div>
      <h1 class="hero-couple-title">
        Kasandra <span class="amp">&amp;</span> Imanule
      </h1>
      <div class="hero-tagline">Two families, one beautiful beginning.</div>

      <div class="hero-date-venue-capsule">
        <i class="bi bi-calendar-event text-warning"></i> Saturday, October 19, 2027 &bull; The White Church, 125 Rd
      </div>

      <!-- Live Countdown Timer -->
      <div class="countdown-grid">
        <div class="countdown-box">
          <div class="countdown-num" id="cdDays">00</div>
          <div class="countdown-lbl">Days</div>
        </div>
        <div class="countdown-box">
          <div class="countdown-num" id="cdHours">00</div>
          <div class="countdown-lbl">Hours</div>
        </div>
        <div class="countdown-box">
          <div class="countdown-num" id="cdMinutes">00</div>
          <div class="countdown-lbl">Mins</div>
        </div>
        <div class="countdown-box">
          <div class="countdown-num" id="cdSeconds">00</div>
          <div class="countdown-lbl">Secs</div>
        </div>
      </div>

      <div class="d-flex justify-content-center gap-3 flex-wrap">
        <a href="#rituals" class="btn-gold">
          <i class="bi bi-flower1"></i> आमचे मंगल सोहळे
        </a>
        <button type="button" class="btn-maroon" onclick="downloadEventIcs('Royal Maharashtrian Wedding — Kasandra & Imanule', '2027-10-19T10:00:00', '2027-10-19T23:30:00', 'The White Church, 125 Rd')">
          <i class="bi bi-calendar-plus"></i> Add to Calendar
        </button>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 5: GANESH INVOCATION & DEVOTIONAL SANCTUARY
       ========================================================================== -->
  <section class="section-padding ganesh-blessing-section" id="blessings">
    <div class="site-container text-center">
      <div class="section-eyebrow">Auspicious Beginning</div>
      <h2 class="section-heading">॥ श्री गणेशाय नमः ॥</h2>
      <div class="section-subheading-mr">With divine blessings, a beautiful new journey begins.</div>
      <div class="theme-divider"></div>

      <div class="ganesh-blessing-showcase">
        <div class="d-flex align-items-center justify-content-center gap-4 flex-wrap">
          <div class="d-none d-md-block">
            <img src="images/diya.png" alt="Sacred Diya Lamp" class="diya-glow-img">
          </div>
          <div class="theme5-ganesh-frame">
            <div class="ganesh-radiance-aura"></div>
            <img src="images/ganesh.png" alt="Lord Ganesh Shubh Vivah" class="ganesh-central-img">
          </div>
          <div class="d-none d-md-block">
            <img src="images/diya1.png" alt="Sacred Diya Lamp" class="diya-glow-img">
          </div>
        </div>

        <div class="mt-4">
          <div class="sanskrit-chant">वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ। निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥</div>
          <div class="translit-chant">Shri Ganeshaya Namah &bull; Divine Invocation</div>
          <p class="blessing-mantra-text">
            &ldquo;May Lord Ganesha, the remover of all obstacles and harbinger of supreme wisdom, bless this sacred union with lifelong prosperity, spiritual joy, and boundless harmony.&rdquo;
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 6: MEET THE BRIDE & GROOM (वधू आणि वर)
       ========================================================================== */
       ========================================================================== -->
  <section class="section-padding" id="union" style="background: var(--color-bg-body); position: relative; overflow: hidden;">
    <div class="site-container">
      <div class="text-center">
        <div class="section-eyebrow">Two Families, One Union</div>
        <h2 class="section-heading">वधू आणि वर</h2>
        <div class="section-subheading-mr">Meet the Bride &amp; Groom</div>
        <div class="theme-divider"></div>
        <p class="section-desc">
          Guided by our cherished families, traditions of love, and sacred blessings, we begin our eternal journey as one.
        </p>
      </div>

      <div class="couple-cards-grid">
        <!-- Bride Card -->
        <div class="couple-portrait-card">
          <div class="couple-avatar-decor">
            <img src="images/girl.png" alt="Bride Avatar" class="couple-avatar-img">
          </div>
          <div class="portrait-frame">
            <img src="images/bride_kasandra.jpg" alt="Kasandra Miller">
            <span class="role-badge-pill">वधू &bull; The Bride</span>
          </div>
          <h3 class="couple-person-name">Kasandra Miller</h3>
          <div class="couple-person-parents">Daughter of Mr. &amp; Mrs. Miller</div>
          <p class="couple-personal-vow">
            &ldquo;With an open heart and deep reverence for our families, I take Imanule's hand. In him, I have found my greatest confidant, my warmth, and my peaceful sanctuary.&rdquo;
          </p>
        </div>

        <!-- Groom Card -->
        <div class="couple-portrait-card">
          <div class="couple-avatar-decor">
            <img src="images/boy.png" alt="Groom Avatar" class="couple-avatar-img">
          </div>
          <div class="portrait-frame">
            <img src="images/groom_imanule.jpg" alt="Imanule David">
            <span class="role-badge-pill">वर &bull; The Groom</span>
          </div>
          <h3 class="couple-person-name">Imanule David</h3>
          <div class="couple-person-parents">Son of Mr. &amp; Mrs. David</div>
          <p class="couple-personal-vow">
            &ldquo;Kasandra illuminates every day with grace, kindness, and devotion. Loving her is the simplest and most sacred commitment of my life. I am blessed to call her my wife.&rdquo;
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 7: OUR LOVE STORY (आमची प्रेमकथा)
       ========================================================================== -->
  <section class="section-padding" id="story" style="background: #FFFFFF; border-top: 1px solid var(--color-beige); border-bottom: 1px solid var(--color-beige);">
    <div class="site-container">
      <div class="text-center">
        <div class="section-eyebrow">A Timeless Romance</div>
        <h2 class="section-heading">आमची प्रेमकथा</h2>
        <div class="section-subheading-mr">Chapters of Our Journey</div>
        <div class="theme-divider"></div>
        <p class="section-desc">
          The defining milestones of friendship, companionship, and devotion that led us to this sacred threshold.
        </p>
      </div>

      <div class="story-timeline-container">
        <!-- Milestone 1 -->
        <div class="story-item">
          <div class="story-timeline-marker">I</div>
          <div class="story-content-box">
            <div class="story-img-frame">
              <img src="images/story_met.jpg" alt="Where We Met">
            </div>
            <div class="story-chapter-tag">2020 &bull; Chapter I</div>
            <h3 class="story-chapter-title">The First Meeting</h3>
            <p style="font-size: 0.94rem; color: var(--color-charcoal-muted); line-height: 1.6; margin: 0;">
              A rainy afternoon at a quiet coffee house turned into hours of shared stories, genuine laughter, and an unspoken connection that neither of us could forget.
            </p>
          </div>
        </div>

        <!-- Milestone 2 -->
        <div class="story-item">
          <div class="story-timeline-marker">II</div>
          <div class="story-content-box">
            <div class="story-img-frame">
              <img src="images/story_date.jpg" alt="The First Journey">
            </div>
            <div class="story-chapter-tag">2022 &bull; Chapter II</div>
            <h3 class="story-chapter-title">The First Journey Together</h3>
            <p style="font-size: 0.94rem; color: var(--color-charcoal-muted); line-height: 1.6; margin: 0;">
              Exploring scenic mountain riverbanks under golden autumn foliage. It was during these quiet walks that we realized we wanted to walk through every season of life together.
            </p>
          </div>
        </div>

        <!-- Milestone 3 -->
        <div class="story-item">
          <div class="story-timeline-marker">III</div>
          <div class="story-content-box">
            <div class="story-img-frame">
              <img src="images/story_proposal.jpg" alt="The Proposal">
            </div>
            <div class="story-chapter-tag">2025 &bull; Chapter III</div>
            <h3 class="story-chapter-title">The Proposal</h3>
            <p style="font-size: 0.94rem; color: var(--color-charcoal-muted); line-height: 1.6; margin: 0;">
              Beneath a starlit mountain sky during a weekend getaway, Imanule asked the question that made eternity real. With joyous tears and smiling eyes, Kasandra said yes.
            </p>
          </div>
        </div>

        <!-- Milestone 4 -->
        <div class="story-item">
          <div class="story-timeline-marker">IV</div>
          <div class="story-content-box">
            <div class="story-img-frame">
              <img src="images/story_forever.jpg" alt="Walking to Forever">
            </div>
            <div class="story-chapter-tag">2027 &bull; Chapter IV</div>
            <h3 class="story-chapter-title">Sacred Forever</h3>
            <p style="font-size: 0.94rem; color: var(--color-charcoal-muted); line-height: 1.6; margin: 0;">
              Surrounded by our families, sacred Vedic chants, and lifelong blessings, our hands are joined forever in holy matrimony and eternal love.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 8: AUTHENTIC MARATHI HINDU WEDDING CEREMONIES (आमचे मंगल सोहळे)
       ========================================================================== -->
  <section class="section-padding" id="rituals" style="background: var(--color-ivory);">
    <div class="site-container">
      <div class="text-center">
        <div class="section-eyebrow">Sacred Traditions</div>
        <h2 class="section-heading">आमचे मंगल सोहळे</h2>
        <div class="section-subheading-mr">Celebrating the Traditions &amp; Blessings of a Maharashtrian Wedding</div>
        <div class="theme-divider"></div>
        <p class="section-desc">
          Every ritual carries timeless spiritual meaning, honoring our ancestors, seeking divine grace, and uniting two families in holy bond.
        </p>
      </div>

      <div class="rituals-grid">
        <!-- 1. Devak Sthapana -->
        <div class="ritual-card" data-ritual="1">
          <div class="ritual-number">०१ &bull; Ritual I</div>
          <div class="ritual-title-mr">देवक स्थापना</div>
          <div class="ritual-title-en">Devak Sthapana</div>
          <p class="ritual-desc">
            Invoking the family's Kuldevata (guardian deity) and seeking blessings for auspiciousness, harmony, and protection throughout the wedding festivities.
          </p>
        </div>

        <!-- 2. Ganesh Pujan -->
        <div class="ritual-card" data-ritual="2">
          <div class="ritual-number">०२ &bull; Ritual II</div>
          <div class="ritual-title-mr">श्री गणेश पूजन</div>
          <div class="ritual-title-en">Ganesh Pujan</div>
          <p class="ritual-desc">
            Devotional prayer to Lord Ganesha, seeking the removal of all obstacles and blessing the couple's new beginning with prosperity and grace.
          </p>
        </div>

        <!-- 3. Halad Samarambh -->
        <div class="ritual-card" data-ritual="3">
          <div class="ritual-number">०३ &bull; Ritual III</div>
          <div class="ritual-title-mr">हळद समारंभ</div>
          <div class="ritual-title-en">Halad Samarambh</div>
          <p class="ritual-desc">
            Auspicious fragrant turmeric paste applied to the bride and groom by married women (Suhasinis), accompanied by folk songs, marigolds, and laughter.
          </p>
        </div>

        <!-- 4. Mehendi -->
        <div class="ritual-card" data-ritual="4">
          <div class="ritual-number">०४ &bull; Ritual IV</div>
          <div class="ritual-title-mr">शुभ मेहंदी</div>
          <div class="ritual-title-en">Mehendi Ceremony</div>
          <p class="ritual-desc">
            Intricate natural henna designs adorned upon the bride's hands and feet, symbolizing good fortune, deep affection, and festive beauty.
          </p>
        </div>

        <!-- 5. Seemant Pujan -->
        <div class="ritual-card" data-ritual="5">
          <div class="ritual-number">०५ &bull; Ritual V</div>
          <div class="ritual-title-mr">सीमांत पूजन</div>
          <div class="ritual-title-en">Seemant Pujan</div>
          <p class="ritual-desc">
            Traditional welcoming ritual where the bride's parents warmly greet the groom and his family at the wedding venue border with arati and gifts.
          </p>
        </div>

        <!-- 6. Varat Swagat -->
        <div class="ritual-card" data-ritual="6">
          <div class="ritual-number">०६ &bull; Ritual VI</div>
          <div class="ritual-title-mr">वरात स्वागत</div>
          <div class="ritual-title-en">Varat Swagat</div>
          <p class="ritual-desc">
            The joyous ceremonial arrival of the groom's procession, received at the entrance with traditional music, rose water, and royal Marathi hospitality.
          </p>
        </div>

        <!-- 7. Antarpat -->
        <div class="ritual-card" data-ritual="7">
          <div class="ritual-number">०७ &bull; Ritual VII</div>
          <div class="ritual-title-mr">अंतरपाट</div>
          <div class="ritual-title-en">Antarpat Ceremony</div>
          <p class="ritual-desc">
            A sacred silk cloth held between the bride and groom, concealing them from each other while sacred Mangalashtake verses are recited.
          </p>
        </div>

        <!-- 8. Mangalashtake -->
        <div class="ritual-card" data-ritual="8">
          <div class="ritual-number">०८ &bull; Ritual VIII</div>
          <div class="ritual-title-mr">मंगलाष्टके</div>
          <div class="ritual-title-en">Mangalashtake Verses</div>
          <p class="ritual-desc">
            Sacred poetic verses chanted by the priest and elders, culminating in the joyous declaration of &ldquo;शुभमंगल सावधान&rdquo; as the Antarpat is lowered.
          </p>
        </div>

        <!-- 9. Akshata -->
        <div class="ritual-card" data-ritual="9">
          <div class="ritual-number">०९ &bull; Ritual IX</div>
          <div class="ritual-title-mr">अक्षतारोपण</div>
          <div class="ritual-title-en">Akshata Shower</div>
          <p class="ritual-desc">
            Family members and cherished guests gently shower the couple with consecrated unbroken rice grains, bestowing heartfelt blessings for eternal happiness.
          </p>
        </div>

        <!-- 10. Kanyadaan -->
        <div class="ritual-card" data-ritual="10">
          <div class="ritual-number">१० &bull; Ritual X</div>
          <div class="ritual-title-mr">कन्यादान</div>
          <div class="ritual-title-en">Kanyadaan</div>
          <p class="ritual-desc">
            The solemn and emotional moment where parents place their daughter's hand into the groom's, receiving his sacred promise of lifelong love and honor.
          </p>
        </div>

        <!-- 11. Saptapadi -->
        <div class="ritual-card" data-ritual="11">
          <div class="ritual-number">११ &bull; Ritual XI</div>
          <div class="ritual-title-mr">सप्तपदी</div>
          <div class="ritual-title-en">Saptapadi (Seven Steps)</div>
          <p class="ritual-desc">
            Walking the seven sacred steps together around the holy Agni fire, sealing seven solemn vows of nourishment, strength, prosperity, and eternal devotion.
          </p>
        </div>

        <!-- 12. Mangalsutra & Sindoor -->
        <div class="ritual-card" data-ritual="12">
          <div class="ritual-number">१२ &bull; Ritual XII</div>
          <div class="ritual-title-mr">मंगळसूत्र आणि सिंदूर</div>
          <div class="ritual-title-en">Mangalsutra &amp; Sindoor</div>
          <p class="ritual-desc">
            The groom adorns the bride with the sacred black-and-gold beaded Mangalsutra and applies red Sindoor, sacred emblems of love and wedded unity.
          </p>
        </div>

        <!-- 13. Aashirwad -->
        <div class="ritual-card" data-ritual="13">
          <div class="ritual-number">१३ &bull; Ritual XIII</div>
          <div class="ritual-title-mr">आशीर्वाद</div>
          <div class="ritual-title-en">Aashirwad (Elder Blessings)</div>
          <p class="ritual-desc">
            Touching the feet of parents, grandparents, and revered elders to receive their heartfelt prayers and blessings for a life of righteousness.
          </p>
        </div>

        <!-- 14. Grihapravesh -->
        <div class="ritual-card" data-ritual="14">
          <div class="ritual-number">१४ &bull; Ritual XIV</div>
          <div class="ritual-title-mr">गृहप्रवेश</div>
          <div class="ritual-title-en">Grihapravesh</div>
          <p class="ritual-desc">
            The bride is warmly welcomed into her new home, gently knocking over a measuring vessel of rice with her right foot to symbolize incoming prosperity.
          </p>
        </div>

        <!-- 15. Swagat Samarambh -->
        <div class="ritual-card" data-ritual="15">
          <div class="ritual-number">१५ &bull; Ritual XV</div>
          <div class="ritual-title-mr">स्वागत समारंभ</div>
          <div class="ritual-title-en">Swagat Samarambh (Reception)</div>
          <p class="ritual-desc">
            A grand evening reception banquet where relatives, friends, and well-wishers gather to celebrate, feast, and toast to the newlyweds.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 9: WEDDING EVENT TIMELINE (विवाह कार्यक्रम पत्रिका)
       ========================================================================== -->
  <section class="section-padding" id="schedule" style="background: #FFFFFF; border-top: 1px solid var(--color-beige); border-bottom: 1px solid var(--color-beige);">
    <div class="site-container">
      <div class="text-center">
        <div class="section-eyebrow">Itinerary &amp; Timeline</div>
        <h2 class="section-heading">विवाह कार्यक्रम पत्रिका</h2>
        <div class="section-subheading-mr">Wedding Event Schedule</div>
        <div class="theme-divider"></div>
        <p class="section-desc">
          Join us throughout our celebratory weekend. Add each special ceremony to your personal calendar with a single click.
        </p>
      </div>

      <div class="events-editorial-grid">
        <!-- Event 1: Halad & Sangeet -->
        <div class="event-editorial-card">
          <div class="event-media-cover">
            <img src="images/dance.png" alt="हळद व संगीत">
            <span class="event-time-capsule">Friday, Oct 18 &bull; 6:00 PM</span>
          </div>
          <div class="event-card-body">
            <div class="event-title-mr">हळद व संगीत सोहळा</div>
            <div class="event-title-en">Halad &amp; Sangeet Evening</div>
            <div class="event-venue-meta">
              <i class="bi bi-geo-alt-fill text-danger"></i> Courtyard Garden Veranda
            </div>
            <p class="event-desc-text">
              An energetic musical evening with traditional Marathi Lavani rhythms, turmeric blessings, family performances, and festive dinner.
            </p>
            <div class="event-attire-row">
              <span>Attire: Yellow &amp; Festive Ethnic</span>
              <button type="button" class="btn-outline-gold" style="padding: 6px 16px; font-size: 12px;" onclick="downloadEventIcs('Halad & Sangeet Evening', '2027-10-18T18:00:00', '2027-10-18T22:00:00', 'Courtyard Garden Veranda')">
                + Calendar
              </button>
            </div>
          </div>
        </div>

        <!-- Event 2: Seemant & Ganesh Pujan -->
        <div class="event-editorial-card">
          <div class="event-media-cover">
            <img src="images/diya.png" alt="सीमांत व गणेश पूजन">
            <span class="event-time-capsule">Saturday, Oct 19 &bull; 9:30 AM</span>
          </div>
          <div class="event-card-body">
            <div class="event-title-mr">सीमांत व गणेश पूजन</div>
            <div class="event-title-en">Seemant &amp; Ganesh Pujan</div>
            <div class="event-venue-meta">
              <i class="bi bi-geo-alt-fill text-danger"></i> Mandap Entrance &bull; 125 Rd
            </div>
            <p class="event-desc-text">
              Welcoming the groom's family followed by solemn prayers to Lord Ganesha for harmony, auspiciousness, and sacred beginnings.
            </p>
            <div class="event-attire-row">
              <span>Attire: Traditional Indian Silk</span>
              <button type="button" class="btn-outline-gold" style="padding: 6px 16px; font-size: 12px;" onclick="downloadEventIcs('Seemant & Ganesh Pujan', '2027-10-19T09:30:00', '2027-10-19T11:30:00', 'The White Church Mandap')">
                + Calendar
              </button>
            </div>
          </div>
        </div>

        <!-- Event 3: Sacred Vivah & Saptapadi -->
        <div class="event-editorial-card">
          <div class="event-media-cover">
            <img src="images/vivah.png" alt="शुभ विवाह व सप्तपदी">
            <span class="event-time-capsule">Saturday, Oct 19 &bull; 12:30 PM</span>
          </div>
          <div class="event-card-body">
            <div class="event-title-mr">शुभ विवाह व सप्तपदी</div>
            <div class="event-title-en">Sacred Vivah &amp; Saptapadi</div>
            <div class="event-venue-meta">
              <i class="bi bi-geo-alt-fill text-danger"></i> Main Sanctuary Mandap
            </div>
            <p class="event-desc-text">
              The sacred muhurt, Mangalashtake chanting, lowering of the Antarpat, Kanyadaan, and the sacred seven steps around holy fire.
            </p>
            <div class="event-attire-row">
              <span>Attire: Royal Maroon &amp; Gold Silk</span>
              <button type="button" class="btn-outline-gold" style="padding: 6px 16px; font-size: 12px;" onclick="downloadEventIcs('Sacred Vivah & Saptapadi', '2027-10-19T12:30:00', '2027-10-19T14:30:00', 'The White Church Sanctuary')">
                + Calendar
              </button>
            </div>
          </div>
        </div>

        <!-- Event 4: Jai Mala & Akshata -->
        <div class="event-editorial-card">
          <div class="event-media-cover">
            <img src="images/jaymala.png" alt="जयमाला व अक्षतारोपण">
            <span class="event-time-capsule">Saturday, Oct 19 &bull; 2:00 PM</span>
          </div>
          <div class="event-card-body">
            <div class="event-title-mr">जयमाला व अक्षतारोपण</div>
            <div class="event-title-en">Jai Mala &amp; Akshata Shower</div>
            <div class="event-venue-meta">
              <i class="bi bi-geo-alt-fill text-danger"></i> Central Floral Stage
            </div>
            <p class="event-desc-text">
              The joyous exchange of rose and jasmine garlands followed by consecrated rice blessings showered by all beloved guests.
            </p>
            <div class="event-attire-row">
              <span>Attire: Paithani / Kurta</span>
              <button type="button" class="btn-outline-gold" style="padding: 6px 16px; font-size: 12px;" onclick="downloadEventIcs('Jai Mala & Akshata Shower', '2027-10-19T14:00:00', '2027-10-19T15:30:00', 'The White Church Pavilion')">
                + Calendar
              </button>
            </div>
          </div>
        </div>

        <!-- Event 5: Swagat Samarambh (Reception) -->
        <div class="event-editorial-card">
          <div class="event-media-cover">
            <img src="images/location.png" alt="स्वागत समारंभ">
            <span class="event-time-capsule">Saturday, Oct 19 &bull; 7:00 PM</span>
          </div>
          <div class="event-card-body">
            <div class="event-title-mr">स्वागत समारंभ व स्नेहभोजन</div>
            <div class="event-title-en">Swagat Samarambh (Reception)</div>
            <div class="event-venue-meta">
              <i class="bi bi-geo-alt-fill text-danger"></i> Grand Heritage Ballroom
            </div>
            <p class="event-desc-text">
              A regal evening celebration, heartfelt toasts, live Indian classical ensemble, and a sumptuous Maharashtrian wedding feast.
            </p>
            <div class="event-attire-row">
              <span>Attire: Formal Evening / Royal Ethnic</span>
              <button type="button" class="btn-outline-gold" style="padding: 6px 16px; font-size: 12px;" onclick="downloadEventIcs('Swagat Samarambh Reception', '2027-10-19T19:00:00', '2027-10-19T23:30:00', 'Grand Heritage Ballroom')">
                + Calendar
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 10: MAHARASHTRIAN WEDDING DRESS CODE (पोषाख मार्गदर्शिका)
       ========================================================================== -->
  <section class="section-padding" id="dresscode" style="background: var(--color-ivory);">
    <div class="site-container">
      <div class="text-center">
        <div class="section-eyebrow">Attire &amp; Styling Guide</div>
        <h2 class="section-heading">पोषाख मार्गदर्शिका</h2>
        <div class="section-subheading-mr">Maharashtrian Wedding Dress Code</div>
        <div class="theme-divider"></div>
        <p class="section-desc">
          We welcome you to celebrate with us in elegant traditional attire or sophisticated semi-formal wedding wear.
        </p>
      </div>

      <div class="dresscode-grid">
        <!-- Bride Styling -->
        <div class="dresscode-card">
          <div class="dresscode-icon"><i class="bi bi-gem"></i></div>
          <h3 class="dresscode-title">Bride-Inspired Grace</h3>
          <p style="font-size: 0.94rem; color: var(--color-charcoal-muted); margin-bottom: 12px;">
            The radiant elegance of timeless Maharashtrian bridal heritage:
          </p>
          <ul class="dresscode-items-list">
            <li>✦ Traditional <strong>Nauvari</strong> or <strong>Paithani Saree</strong></li>
            <li>✦ Classic pearl <strong>Brahmani Nath</strong> (nose ornament)</li>
            <li>✦ Sacred silk <strong>Mundavalya</strong> forehead pearls</li>
            <li>✦ Traditional Kolhapuri Saaj &amp; green glass bangles</li>
          </ul>
        </div>

        <!-- Groom Styling -->
        <div class="dresscode-card">
          <div class="dresscode-icon"><i class="bi bi-award"></i></div>
          <h3 class="dresscode-title">Groom-Inspired Regalia</h3>
          <p style="font-size: 0.94rem; color: var(--color-charcoal-muted); margin-bottom: 12px;">
            Dignified traditional Maharashtrian royal wedding attire:
          </p>
          <ul class="dresscode-items-list">
            <li>✦ Silk <strong>Kurta</strong> with embroidered angarakha</li>
            <li>✦ Royal pleated <strong>Pheta</strong> (traditional turban)</li>
            <li>✦ Traditional Dhoti or tailored Churidar</li>
            <li>✦ Sacred silk <strong>Mundavalya</strong> forehead pearls</li>
          </ul>
        </div>

        <!-- Guest Attire -->
        <div class="dresscode-card">
          <div class="dresscode-icon"><i class="bi bi-people"></i></div>
          <h3 class="dresscode-title">Guest Dress Suggestions</h3>
          <p style="font-size: 0.94rem; color: var(--color-charcoal-muted); margin-bottom: 12px;">
            Celebrate in festive colors and comfortable traditional wear:
          </p>
          <ul class="dresscode-items-list">
            <li>✦ Women: Paithani, Chanderi, Kanjivaram or Silk Sarees</li>
            <li>✦ Men: Kurta-Pyjama, Nehru Jackets or Dark Suits</li>
            <li>✦ Halad: Vibrant yellows, oranges, and warm pastels</li>
            <li>✦ Reception: Deep royal jewel tones &amp; evening wear</li>
          </ul>
        </div>
      </div>

      <!-- Color Palette Swatches -->
      <div class="text-center">
        <div class="palette-swatches-wrap">
          <div class="swatch-pill">
            <span class="swatch-dot" style="background: #641D2D;"></span>
            <span>Royal Maroon</span>
          </div>
          <div class="swatch-pill">
            <span class="swatch-dot" style="background: #C5A15B;"></span>
            <span>Antique Gold</span>
          </div>
          <div class="swatch-pill">
            <span class="swatch-dot" style="background: #FBF6EC;"></span>
            <span>Warm Ivory</span>
          </div>
          <div class="swatch-pill">
            <span class="swatch-dot" style="background: #EAB308;"></span>
            <span>Turmeric Yellow</span>
          </div>
          <div class="swatch-pill">
            <span class="swatch-dot" style="background: #475E4C;"></span>
            <span>Muted Sage</span>
          </div>
          <div class="swatch-pill">
            <span class="swatch-dot" style="background: #E8C8C2;"></span>
            <span>Soft Blush</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 12: LUXURY EDITORIAL PHOTO GALLERY WITH LIGHTBOX (क्षणचित्रे)
       ========================================================================== -->
  <section class="section-padding" id="gallery" style="background: #FFFFFF; border-top: 1px solid var(--color-beige); border-bottom: 1px solid var(--color-beige);">
    <div class="site-container">
      <div class="text-center">
        <div class="section-eyebrow">Visual Diary</div>
        <h2 class="section-heading">क्षणचित्रे</h2>
        <div class="section-subheading-mr">Editorial Wedding Gallery</div>
        <div class="theme-divider"></div>
        <p class="section-desc">
          Snapshots of devotion, family smiles, and unforgettable celebrations along our path to forever.
        </p>
      </div>

      <!-- Filter Buttons -->
      <div class="gallery-filter-buttons">
        <button class="gallery-tab-btn active" data-filter="all">All Moments</button>
        <button class="gallery-tab-btn" data-filter="moments">Our Romance</button>
        <button class="gallery-tab-btn" data-filter="halad">Halad &amp; Mehendi</button>
        <button class="gallery-tab-btn" data-filter="rituals">Wedding Rituals</button>
        <button class="gallery-tab-btn" data-filter="celebration">Celebrations</button>
      </div>

      <!-- Masonry Grid -->
      <div class="gallery-masonry-grid" id="galleryMasonry">
        <!-- Tile 1 -->
        <div class="gallery-item-tile tall" data-category="moments" data-caption="Kasandra &amp; Imanule — Two souls united in grace" data-src="images/hero_couple.jpg">
          <img src="images/hero_couple.jpg" alt="Couple Portrait" loading="lazy">
          <div class="gallery-item-overlay">
            <span class="gallery-overlay-tag">Our Romance</span>
            <span class="gallery-overlay-caption">Soulful Companionship</span>
          </div>
        </div>

        <!-- Tile 2 -->
        <div class="gallery-item-tile" data-category="rituals" data-caption="Sacred wedding rings symbolizing unbroken eternity" data-src="images/rings.jpg">
          <img src="images/rings.jpg" alt="Sacred Rings" loading="lazy">
          <div class="gallery-item-overlay">
            <span class="gallery-overlay-tag">Wedding Rituals</span>
            <span class="gallery-overlay-caption">Eternal Rings</span>
          </div>
        </div>

        <!-- Tile 3 -->
        <div class="gallery-item-tile tall" data-category="moments" data-caption="The glowing bride, Kasandra" data-src="images/bride_kasandra.jpg">
          <img src="images/bride_kasandra.jpg" alt="The Bride" loading="lazy">
          <div class="gallery-item-overlay">
            <span class="gallery-overlay-tag">Our Romance</span>
            <span class="gallery-overlay-caption">The Radiant Bride</span>
          </div>
        </div>

        <!-- Tile 4 -->
        <div class="gallery-item-tile" data-category="halad" data-caption="Fragrant auspicious henna adornments" data-src="images/mehandi.png">
          <img src="images/mehandi.png" alt="Mehndi Hands" loading="lazy">
          <div class="gallery-item-overlay">
            <span class="gallery-overlay-tag">Halad &amp; Mehendi</span>
            <span class="gallery-overlay-caption">Sacred Henna</span>
          </div>
        </div>

        <!-- Tile 5 -->
        <div class="gallery-item-tile wide" data-category="celebration" data-caption="Sangeet night joyful celebrations" data-src="images/dance.png">
          <img src="images/dance.png" alt="Celebration Dance" loading="lazy">
          <div class="gallery-item-overlay">
            <span class="gallery-overlay-tag">Celebrations</span>
            <span class="gallery-overlay-caption">Sangeet Joy &amp; Dance</span>
          </div>
        </div>

        <!-- Tile 6 -->
        <div class="gallery-item-tile" data-category="rituals" data-caption="Shubh Jai Mala sacred garland exchange" data-src="images/jaymala.png">
          <img src="images/jaymala.png" alt="Jai Mala Ceremony" loading="lazy">
          <div class="gallery-item-overlay">
            <span class="gallery-overlay-tag">Wedding Rituals</span>
            <span class="gallery-overlay-caption">Jai Mala Varmala</span>
          </div>
        </div>

        <!-- Tile 7 -->
        <div class="gallery-item-tile" data-category="rituals" data-caption="Sacred Holy Vivah circumambulation vows" data-src="images/vivah.png">
          <img src="images/vivah.png" alt="Holy Vivah Pheras" loading="lazy">
          <div class="gallery-item-overlay">
            <span class="gallery-overlay-tag">Wedding Rituals</span>
            <span class="gallery-overlay-caption">Sacred Saptapadi</span>
          </div>
        </div>

        <!-- Tile 8 -->
        <div class="gallery-item-tile" data-category="celebration" data-caption="Grand Heritage Banquet reception ballroom" data-src="images/location.png">
          <img src="images/location.png" alt="Reception Banquet Hall" loading="lazy">
          <div class="gallery-item-overlay">
            <span class="gallery-overlay-tag">Celebrations</span>
            <span class="gallery-overlay-caption">Grand Banquet Ballroom</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Editorial Lightbox Modal -->
  <div class="editorial-lightbox-modal" id="lightboxModal" role="dialog" aria-modal="true" aria-label="Photo View">
    <button type="button" class="lightbox-btn-close" id="lightboxClose" aria-label="Close Lightbox">&times;</button>
    <button type="button" class="lightbox-btn-nav lightbox-btn-prev" id="lightboxPrev" aria-label="Previous Photo">&#10094;</button>
    <button type="button" class="lightbox-btn-nav lightbox-btn-next" id="lightboxNext" aria-label="Next Photo">&#10095;</button>

    <div class="lightbox-dialog">
      <div class="lightbox-img-frame">
        <img src="" alt="" id="lightboxImg">
      </div>
      <div class="lightbox-meta-caption" id="lightboxCaption"></div>
    </div>
  </div>

  <!-- ==========================================================================
       SECTION 13: FAMILY BLESSINGS (आशीर्वाद)
       ========================================================================== -->
  <section class="section-padding" id="blessings-family" style="background: var(--color-ivory);">
    <div class="site-container">
      <div class="text-center">
        <div class="section-eyebrow">Elder Words &amp; Prayers</div>
        <h2 class="section-heading">आशीर्वाद</h2>
        <div class="section-subheading-mr">Family Blessings &amp; Cherished Wishes</div>
        <div class="theme-divider"></div>
        <p class="section-desc">
          Heartfelt prayers and words of wisdom from the loving families who nurtured and guided our path.
        </p>
      </div>

      <div class="blessings-quotes-grid">
        <div class="blessing-quote-card">
          <p class="blessing-quote-text">
            &ldquo;From her very first steps to this sacred day, Kasandra has filled our home with boundless light. Seeing her unite with Imanule, a man of such honor and gentle strength, is our deepest blessing.&rdquo;
          </p>
          <div class="blessing-author-name">Mr. &amp; Mrs. Miller</div>
          <div class="blessing-author-relation">Parents of the Bride</div>
        </div>

        <div class="blessing-quote-card">
          <p class="blessing-quote-text">
            &ldquo;Imanule has always walked with integrity and devotion. In Kasandra, our family has been gifted not only a loving daughter-in-law, but a soul of genuine grace. May their path together always be illuminated with happiness.&rdquo;
          </p>
          <div class="blessing-author-name">Mr. &amp; Mrs. David</div>
          <div class="blessing-author-relation">Parents of the Groom</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 14: RSVP EXPERIENCE (उपस्थिती नोंदणी)
       ========================================================================== -->
  <section class="section-padding" id="rsvp" style="background: #FFFFFF; border-top: 1px solid var(--color-beige); border-bottom: 1px solid var(--color-beige);">
    <div class="site-container">
      <div class="text-center">
        <div class="section-eyebrow">Confirm Your Attendance</div>
        <h2 class="section-heading">उपस्थिती नोंदणी</h2>
        <div class="section-subheading-mr">RSVP &bull; Will You Join Us?</div>
        <div class="theme-divider"></div>
        <p class="section-desc">
          Kindly confirm your presence before September 15, 2027, so our families can prepare for your warm hospitality.
        </p>
      </div>

      <div class="rsvp-editorial-card">
        <form id="marathiRsvpForm" onsubmit="handleMarathiRsvp(event)">
          <!-- Attendance Selection Buttons -->
          <div class="attendance-btn-group">
            <div class="attendance-option">
              <input type="radio" name="attend_choice" id="attendYes" value="yes" checked>
              <label for="attendYes"><i class="bi bi-check-circle-fill text-warning"></i> Joyfully Attending</label>
            </div>
            <div class="attendance-option">
              <input type="radio" name="attend_choice" id="attendNo" value="no">
              <label for="attendNo"><i class="bi bi-x-circle text-danger"></i> Regretfully Declining</label>
            </div>
          </div>

          <div class="row g-3">
            <div class="col-md-6 form-group-custom">
              <label class="form-label-custom" for="rsvpFullName">Guest Full Name *</label>
              <input type="text" id="rsvpFullName" class="form-input-custom" placeholder="e.g. Rahul Patil &amp; Family" required>
            </div>

            <div class="col-md-6 form-group-custom">
              <label class="form-label-custom" for="rsvpContact">Email Address / Phone *</label>
              <input type="text" id="rsvpContact" class="form-input-custom" placeholder="rahul@example.com" required>
            </div>

            <div class="col-md-6 form-group-custom">
              <label class="form-label-custom" for="rsvpGuestCount">Number of Accompanying Guests</label>
              <select id="rsvpGuestCount" class="form-input-custom">
                <option value="1">1 Guest (Self)</option>
                <option value="2">2 Guests (Couple)</option>
                <option value="3">3 Guests (Family)</option>
                <option value="4">4 Guests (Family)</option>
                <option value="5">5+ Guests</option>
              </select>
            </div>

            <div class="col-md-6 form-group-custom">
              <label class="form-label-custom" for="rsvpDietary">Feast Preferences</label>
              <select id="rsvpDietary" class="form-input-custom">
                <option value="traditional_veg">Traditional Maharashtrian Vegetarian Feast</option>
                <option value="jain">Jain Vegetarian Feast</option>
                <option value="standard">Standard Feast</option>
              </select>
            </div>

            <div class="col-12 form-group-custom">
              <label class="form-label-custom">Ceremonies You Plan to Attend</label>
              <div class="d-flex gap-3 flex-wrap mt-2">
                <label class="d-flex align-items-center gap-2" style="font-size: 13.5px; cursor: pointer;">
                  <input type="checkbox" name="ceremonies" value="halad" checked> Halad &amp; Sangeet
                </label>
                <label class="d-flex align-items-center gap-2" style="font-size: 13.5px; cursor: pointer;">
                  <input type="checkbox" name="ceremonies" value="vivah" checked> Sacred Vivah &amp; Saptapadi
                </label>
                <label class="d-flex align-items-center gap-2" style="font-size: 13.5px; cursor: pointer;">
                  <input type="checkbox" name="ceremonies" value="reception" checked> Swagat Samarambh (Reception)
                </label>
              </div>
            </div>

            <div class="col-12 form-group-custom">
              <label class="form-label-custom" for="rsvpMessage">Personal Blessings &amp; Message for Couple</label>
              <textarea id="rsvpMessage" class="form-input-custom" rows="3" placeholder="Leave your heartfelt blessings for Kasandra &amp; Imanule..."></textarea>
            </div>

            <div class="col-12 text-center mt-3">
              <button type="submit" class="btn-maroon w-100 py-3" style="font-size: 16px;">
                <i class="bi bi-send-check me-1"></i> Submit RSVP Response
              </button>
            </div>
          </div>
        </form>

        <div id="rsvpSuccessPanel" style="display: none; text-align: center; padding: 30px 10px;">
          <div style="font-size: 3rem; margin-bottom: 12px;">💌</div>
          <h3 class="section-heading" style="font-size: 2.2rem; margin-bottom: 8px;">आभार &bull; Thank You!</h3>
          <p id="rsvpSuccessMsg" style="font-size: 1.05rem; color: var(--color-charcoal-muted); max-width: 500px; margin: 0 auto 24px;">
            Your response has been lovingly received by the families of Kasandra &amp; Imanule.
          </p>
          <button type="button" class="btn-outline-gold" onclick="resetRsvpForm()">Submit Another Response</button>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 15: VENUE AND LOCATION (स्थळ व प्रवास)
       ========================================================================== -->
  <section class="section-padding" id="venue" style="background: var(--color-ivory);">
    <div class="site-container">
      <div class="text-center">
        <div class="section-eyebrow">Ceremony Destination</div>
        <h2 class="section-heading">स्थळ व प्रवास</h2>
        <div class="section-subheading-mr">Venue &amp; Travel Guide</div>
        <div class="theme-divider"></div>
        <p class="section-desc">
          Historic architecture surrounded by peaceful botanical gardens at 125 Rd.
        </p>
      </div>

      <div class="venue-showcase-card">
        <div class="venue-media-banner">
          <img src="images/location.png" alt="The White Church &amp; Grand Ballroom">
        </div>

        <div class="venue-content-padding">
          <div class="row align-items-center g-4">
            <div class="col-lg-7">
              <div style="font-size: 2.2rem; color: var(--color-gold); margin-bottom: 8px;">⛪</div>
              <h3 style="font-family: var(--font-heading); font-size: 2.2rem; font-weight: 700; color: var(--color-maroon); margin-bottom: 4px;">
                The White Church &amp; Grand Heritage Ballroom
              </h3>
              <div style="font-family: var(--font-heading); font-size: 1.15rem; color: var(--color-gold-dark); font-weight: 700; margin-bottom: 14px;">
                125 Rd, Sanctuary &amp; The Grand Pavilion
              </div>
              <p style="font-size: 0.96rem; color: var(--color-charcoal-muted); line-height: 1.7; margin: 0;">
                Offering an auspicious, sacred ambiance for our morning Mandap ceremonies, followed by an opulent indoor banquet in the Grand Heritage Ballroom.
              </p>
            </div>

            <div class="col-lg-5 text-lg-end">
              <div class="d-flex flex-column gap-3 align-items-lg-end">
                <a href="https://maps.google.com/?q=The+White+Church+125+Rd" target="_blank" rel="noopener" class="btn-maroon">
                  <i class="bi bi-geo-alt-fill"></i> Google Maps Directions
                </a>
                <button type="button" class="btn-outline-gold" onclick="copyVenueAddress()">
                  <i class="bi bi-clipboard"></i> Copy Venue Address
                </button>
              </div>
            </div>
          </div>

          <div class="venue-amenities-grid">
            <div class="amenity-box">
              <div class="amenity-title"><i class="bi bi-p-circle me-1 text-warning"></i> Valet &amp; Parking</div>
              <p style="font-size: 0.88rem; color: var(--color-charcoal-muted); margin: 0;">
                Complimentary chauffeured valet parking is stationed at the main gates on 125 Rd.
              </p>
            </div>

            <div class="amenity-box">
              <div class="amenity-title"><i class="bi bi-building me-1 text-warning"></i> Hotel Accommodations</div>
              <p style="font-size: 0.88rem; color: var(--color-charcoal-muted); margin: 0;">
                Reserved room blocks at The Grand Heritage Hotel. Mention code <strong>KASANDRA2027</strong>.
              </p>
            </div>

            <div class="amenity-box">
              <div class="amenity-title"><i class="bi bi-bus-front me-1 text-warning"></i> Private Shuttles</div>
              <p style="font-size: 0.88rem; color: var(--color-charcoal-muted); margin: 0;">
                Continuous complimentary air-conditioned shuttles running between the hotel and wedding mandap.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 17: CLOSING SECTION (॥ शुभमंगल सावधान ॥) & FOOTER
       ========================================================================== -->
  <footer class="closing-finale-section">
    <div class="site-container">
      <div class="closing-benediction">॥ शुभमंगल सावधान ॥</div>
      <h3 class="closing-names">Kasandra &amp; Imanule</h3>
      <div class="closing-desc">
        &ldquo;Thank you for blessing our union with your love, prayers, and cherished presence as we begin our forever journey together.&rdquo;
      </div>

      <div class="d-flex justify-content-center gap-3 flex-wrap mt-4 mb-5">
        <button type="button" class="btn-outline-gold" style="border-color: var(--color-gold); color: var(--color-gold-light); font-size: 13px;" onclick="replayWeddingEnvelope()">
          <i class="bi bi-envelope-paper me-1"></i> Replay Invitation Envelope
        </button>
        <button type="button" class="btn-outline-gold" style="border-color: var(--color-gold); color: var(--color-gold-light); font-size: 13px;" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">
          Back to Top &uarr;
        </button>
      </div>

      <div style="border-top: 1px solid rgba(226, 204, 160, 0.2); padding-top: 28px; font-size: 0.86rem; color: var(--color-gold-pale);">
        &copy; 2027 Kasandra &amp; Imanule &bull; Royal Maharashtrian Wedding Celebration &bull; Crafted with devotion.
      </div>
    </div>
  </footer>

  <!-- Global Toast Feedback -->
  <div class="global-toast" id="globalToast">Notification</div>

  <!-- Scripts: Bootstrap 5, Swiper 11, Custom Interactive Engine -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

  <script>
    /* ==========================================================================
       1. LIVE WEDDING COUNTDOWN TIMER (Saturday, October 19, 2027)
       ========================================================================== */
    var TARGET_TIME = new Date("2027-10-19T10:00:00+05:30").getTime();
    var elDays = document.getElementById('cdDays');
    var elHours = document.getElementById('cdHours');
    var elMins = document.getElementById('cdMinutes');
    var elSecs = document.getElementById('cdSeconds');

    function updateCountdown() {
      var now = Date.now();
      var diff = Math.max(0, TARGET_TIME - now);

      var d = Math.floor(diff / (1000 * 60 * 60 * 24));
      var h = Math.floor((diff / (1000 * 60 * 60)) % 24);
      var m = Math.floor((diff / (1000 * 60)) % 60);
      var s = Math.floor((diff / 1000) % 60);

      if (elDays) elDays.textContent = String(d).padStart(2, '0');
      if (elHours) elHours.textContent = String(h).padStart(2, '0');
      if (elMins) elMins.textContent = String(m).padStart(2, '0');
      if (elSecs) elSecs.textContent = String(s).padStart(2, '0');
    }
    updateCountdown();
    setInterval(updateCountdown, 1000);

    /* ==========================================================================
       2. ZAREQIA-STYLE ENVELOPE UNSEALING & INTERACTION
       ========================================================================== */
    var envelopeOverlay = document.getElementById('envelopeEntranceOverlay');
    var envelopeScene = document.getElementById('envelopeScene');
    var waxSealBtn = document.getElementById('vintageWaxSeal');
    var btnEnvOpen = document.getElementById('btnEnvelopeOpen');
    var btnEnvSkip = document.getElementById('btnEnvelopeSkip');

    function playWaxCrackle() {
      try {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (audioCtx.state === 'suspended') audioCtx.resume();
        var t = audioCtx.currentTime;
        var freqs = [587.33, 880.00, 1174.66, 1760.00];
        freqs.forEach(function(f, idx) {
          var osc = audioCtx.createOscillator();
          var g = audioCtx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(f, t + idx * 0.04);
          g.gain.setValueAtTime(0.001, t + idx * 0.04);
          g.gain.linearRampToValueAtTime(0.06, t + idx * 0.04 + 0.015);
          g.gain.exponentialRampToValueAtTime(0.0001, t + idx * 0.04 + 0.28);
          osc.connect(g);
          g.connect(audioCtx.destination);
          osc.start(t + idx * 0.04);
          osc.stop(t + idx * 0.04 + 0.3);
        });
      } catch (err) {}
    }

    function openWeddingEnvelope() {
      if (!envelopeScene || envelopeScene.classList.contains('unsealed')) return;
      playWaxCrackle();
      envelopeScene.classList.add('unsealed');
      setTimeout(function() {
        startAudio();
      }, 350);
      setTimeout(function() {
        if (envelopeOverlay) envelopeOverlay.classList.add('envelope-dismissed');
      }, 1350);
      setTimeout(function() {
        if (envelopeOverlay) envelopeOverlay.style.display = 'none';
      }, 2200);
    }

    function skipWeddingEnvelope() {
      if (envelopeOverlay) {
        envelopeOverlay.classList.add('envelope-dismissed');
        setTimeout(function() {
          envelopeOverlay.style.display = 'none';
        }, 850);
      }
      startAudio();
    }

    function replayWeddingEnvelope() {
      if (!envelopeOverlay || !envelopeScene) return;
      envelopeScene.classList.remove('unsealed');
      envelopeOverlay.classList.remove('envelope-dismissed');
      envelopeOverlay.style.display = 'flex';
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    if (waxSealBtn) {
      waxSealBtn.addEventListener('click', openWeddingEnvelope);
      waxSealBtn.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          openWeddingEnvelope();
        }
      });
    }
    if (btnEnvOpen) btnEnvOpen.addEventListener('click', openWeddingEnvelope);
    if (btnEnvSkip) btnEnvSkip.addEventListener('click', skipWeddingEnvelope);

    /* ==========================================================================
       3. INDIAN SHEHNAI & SANTOOR RAGA SYNTHESIZER (100% Offline, Zero External MP3)
       ========================================================================== */
    var audioCtx = null;
    var audioPlaying = false;
    var audioInterval = null;

    // Raag Bilawal / Indian Wedding Classical Swaras (C, D, E, F, G, A, B)
    var RAGA_PHRASES = [
      [261.63, 329.63, 392.00, 523.25], // Sa Ga Pa Sa'
      [293.66, 349.23, 440.00, 587.33], // Re Ma Dha Re'
      [329.63, 392.00, 493.88, 659.25], // Ga Pa Ni Ga'
      [261.63, 392.00, 440.00, 523.25]  // Sa Pa Dha Sa'
    ];

    function toggleAudio() {
      if (audioPlaying) {
        stopAudio();
      } else {
        startAudio();
      }
    }

    function startAudio() {
      if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      if (audioCtx.state === 'suspended') audioCtx.resume();

      audioPlaying = true;
      var btn = document.getElementById('audioToggleBtn');
      var label = document.getElementById('audioLabel');
      btn.classList.add('playing');
      label.textContent = "Playing";

      var phraseIdx = 0;
      function playRaga() {
        if (!audioPlaying || !audioCtx) return;
        var notes = RAGA_PHRASES[phraseIdx % RAGA_PHRASES.length];
        notes.forEach(function(freq, i) {
          var osc = audioCtx.createOscillator();
          var gain = audioCtx.createGain();
          osc.type = i % 2 === 0 ? 'sine' : 'triangle';
          var t = audioCtx.currentTime + i * 0.28;
          osc.frequency.setValueAtTime(freq, t);
          gain.gain.setValueAtTime(0.0001, t);
          gain.gain.linearRampToValueAtTime(0.048, t + 0.14);
          gain.gain.exponentialRampToValueAtTime(0.0001, t + 2.5);

          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(t);
          osc.stop(t + 2.7);
        });
        phraseIdx++;
      }

      playRaga();
      audioInterval = setInterval(playRaga, 2800);
      showToast("Playing traditional wedding Shehnai &amp; Raga ♪");
    }

    function stopAudio() {
      audioPlaying = false;
      if (audioInterval) clearInterval(audioInterval);
      var btn = document.getElementById('audioToggleBtn');
      var label = document.getElementById('audioLabel');
      btn.classList.remove('playing');
      label.textContent = "Shehnai & Raga";
      showToast("Soundtrack paused");
    }

    document.getElementById('audioToggleBtn').addEventListener('click', toggleAudio);

    /* ==========================================================================
       4. LUXURY PHOTO GALLERY & FULLSCREEN LIGHTBOX
       ========================================================================== */
    var galleryTiles = Array.from(document.querySelectorAll('.gallery-item-tile'));
    var filterBtns = document.querySelectorAll('.gallery-tab-btn');
    var lightbox = document.getElementById('lightboxModal');
    var lightboxImg = document.getElementById('lightboxImg');
    var lightboxCaption = document.getElementById('lightboxCaption');
    var lightboxClose = document.getElementById('lightboxClose');
    var lightboxPrev = document.getElementById('lightboxPrev');
    var lightboxNext = document.getElementById('lightboxNext');
    var currentImgIdx = 0;
    var visibleTiles = galleryTiles;

    // Filter functionality
    filterBtns.forEach(function(btn) {
      btn.addEventListener('click', function() {
        filterBtns.forEach(function(b) { b.classList.remove('active'); });
        btn.classList.add('active');
        var filter = btn.dataset.filter;

        galleryTiles.forEach(function(tile) {
          if (filter === 'all' || tile.dataset.category === filter) {
            tile.style.display = 'block';
          } else {
            tile.style.display = 'none';
          }
        });
        visibleTiles = galleryTiles.filter(function(t) { return t.style.display !== 'none'; });
      });
    });

    // Lightbox open
    galleryTiles.forEach(function(tile) {
      tile.addEventListener('click', function() {
        currentImgIdx = visibleTiles.indexOf(tile);
        if (currentImgIdx === -1) currentImgIdx = 0;
        openLightbox();
      });
    });

    function openLightbox() {
      var tile = visibleTiles[currentImgIdx];
      if (!tile) return;
      lightboxImg.src = tile.dataset.src;
      lightboxCaption.textContent = tile.dataset.caption;
      lightbox.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
      lightbox.classList.remove('active');
      document.body.style.overflow = '';
    }

    function prevLightbox() {
      if (visibleTiles.length === 0) return;
      currentImgIdx = (currentImgIdx - 1 + visibleTiles.length) % visibleTiles.length;
      openLightbox();
    }

    function nextLightbox() {
      if (visibleTiles.length === 0) return;
      currentImgIdx = (currentImgIdx + 1) % visibleTiles.length;
      openLightbox();
    }

    if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
    if (lightboxPrev) lightboxPrev.addEventListener('click', prevLightbox);
    if (lightboxNext) lightboxNext.addEventListener('click', nextLightbox);

    lightbox.addEventListener('click', function(e) {
      if (e.target === lightbox) closeLightbox();
    });

    document.addEventListener('keydown', function(e) {
      if (!lightbox.classList.contains('active')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowLeft') prevLightbox();
      if (e.key === 'ArrowRight') nextLightbox();
    });

    // Touch Swipe on mobile
    var touchStartX = 0;
    var touchEndX = 0;
    lightbox.addEventListener('touchstart', function(e) {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });
    lightbox.addEventListener('touchend', function(e) {
      touchEndX = e.changedTouches[0].screenX;
      if (touchStartX - touchEndX > 50) nextLightbox();
      if (touchEndX - touchStartX > 50) prevLightbox();
    }, { passive: true });

    /* ==========================================================================
       5. RSVP SUBMISSION & FEEDBACK
       ========================================================================== */
    function handleMarathiRsvp(e) {
      e.preventDefault();
      var name = document.getElementById('rsvpFullName').value.trim();
      var choice = document.querySelector('input[name="attend_choice"]:checked').value;
      var msg = document.getElementById('rsvpMessage').value.trim();

      showToast("आभार, " + name + "! Your response has been received ✨");
      document.getElementById('marathiRsvpForm').style.display = 'none';
      var successPanel = document.getElementById('rsvpSuccessPanel');
      var successMsg = document.getElementById('rsvpSuccessMsg');
      
      if (choice === 'yes') {
        successMsg.innerHTML = "Thank you, <strong>" + name + "</strong>! We are deeply honored by your blessings and look forward to celebrating our sacred union with you.";
      } else {
        successMsg.innerHTML = "Thank you, <strong>" + name + "</strong>, for sending your warm wishes. You will be dearly missed in our celebrations!";
      }
      successPanel.style.display = 'block';
    }

    function resetRsvpForm() {
      document.getElementById('marathiRsvpForm').reset();
      document.getElementById('marathiRsvpForm').style.display = 'block';
      document.getElementById('rsvpSuccessPanel').style.display = 'none';
    }

    /* ==========================================================================
       6. ICALENDAR (.ICS) DOWNLOAD
       ========================================================================== */
    function downloadEventIcs(title, startIso, endIso, loc) {
      var format = function(iso) { return new Date(iso).toISOString().replace(/[-:]|\\.\\d+/g, ''); };
      var ics = "BEGIN:VCALENDAR\\nVERSION:2.0\\nPRODID:-//Kasandra & Imanule Royal Maharashtrian Wedding//EN\\nBEGIN:VEVENT\\n" +
        "UID:" + Date.now() + "@royal-marathi-wedding.com\\n" +
        "DTSTAMP:" + format(new Date().toISOString()) + "\\n" +
        "DTSTART:" + format(startIso) + "\\n" +
        "DTEND:" + format(endIso) + "\\n" +
        "SUMMARY:" + title + "\\n" +
        "LOCATION:" + loc + "\\n" +
        "DESCRIPTION:Royal Maharashtrian Wedding Celebration of Kasandra & Imanule at " + loc + "\\n" +
        "END:VEVENT\\nEND:VCALENDAR";

      var blob = new Blob([ics], { type: 'text/calendar;charset=utf-8' });
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = title.replace(/[^a-zA-Z0-9]/g, '_') + ".ics";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      showToast("Calendar event saved: " + title);
    }

    /* ==========================================================================
       7. TOAST & VENUE COPY
       ========================================================================== */
    function showToast(msg) {
      var toast = document.getElementById('globalToast');
      toast.innerHTML = msg;
      toast.classList.add('show');
      setTimeout(function() { toast.classList.remove('show'); }, 2800);
    }

    function copyVenueAddress() {
      var addr = "The White Church, 125 Rd";
      if (navigator.clipboard) {
        navigator.clipboard.writeText(addr).then(function() {
          showToast("Address copied: " + addr);
        }, function() {
          showToast("Venue: " + addr);
        });
      } else {
        showToast("Venue: " + addr);
      }
    }
  </script>
</body>
</html>'''
    
    with open('Wedding Invitation.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Generated Wedding Invitation.html successfully')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Synchronized index.html successfully')

if __name__ == '__main__':
    generate_website()
