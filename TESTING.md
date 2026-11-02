# Release verification

Published at https://vantmedia.site/ using GitHub Pages (main branch, repository root).

- GitHub Pages build completed without errors; custom domain configured and HTTPS enforced.
- Public DNS resolves vantmedia.site to GitHub Pages. www.vantmedia.site aliases AnalyticsInAction.github.io.
- Live HTML, CSS, JavaScript, favicon and all three campaign photographs returned HTTP 200.
- Browser checks at 390 × 844 CSS pixels (iPhone 16e layout size): no horizontal overflow, headline fits on two lines, full billboard is visible in the hero, contact email link is correct.
- Live desktop check at 1440 × 1000 CSS pixels: document width 1425 with scrollbar, no horizontal overflow.
- Additional live mobile checks: 390-pixel and 320-pixel viewports both have matching document and scroll widths, with no overflowing page content.
- All campaign images loaded. Gallery opens, closes with Escape, restores focus to its trigger, and restores page scrolling. No browser console errors observed during local gallery checks.
- Responsive checks use Chrome emulation; a physical iPhone/Safari was not available.
- Shane's existing default Spacemail signature was preserved and a separate clickable https://vantmedia.site/ line was added. Saved and verified after reload. No email was sent.

The initial mobile check revealed an oversized headline and cropped hero photograph; both were corrected and published.

## HTTPS correction — 3 November 2026

The initial certificate covered only vantmedia.site. The www DNS alias was added afterward, so HTTPS requests to www.vantmedia.site produced a hostname mismatch. GitHub certificate provisioning was restarted after both DNS records were present.

Final verification with Python's default certificate trust and hostname validation enabled:

- Both vantmedia.site and www.vantmedia.site negotiate trusted TLS 1.3.
- The replacement certificate includes both names and is approved by GitHub. It expires 1 February 2027; renewal is managed by GitHub Pages.
- All four entry points (HTTP and HTTPS, apex and www) resolve successfully to https://vantmedia.site/ with HTTP 200.
- GitHub Pages has HTTPS enforcement enabled.
- No HTTP image, stylesheet or script dependencies appear in site source; externally hosted Google Fonts use HTTPS. The HTTP string in the SVG is the standard XML namespace, not a network asset.
- Chrome opened https://www.vantmedia.site/ and securely redirected to the working apex site without a warning.

These checks cover publication, transport security, resources and responsive behaviour, not a general penetration test of GitHub's infrastructure.
