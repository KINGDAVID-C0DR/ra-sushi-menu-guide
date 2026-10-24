RA SUSHI GUEST MENU PHOTO GUIDE — FIRST BUILD

FILES
- index.html: mobile-friendly guest photo browsing site
- images/: real dish photography extracted from the supplied reference PDF
- menu-data.json / menu-data.js: 61 menu entries with descriptions and *provisional* allergen flags
- generate_qr.py: generates QR PNG once you have the real hosted address

TEST LOCALLY
Open index.html by double-clicking it. It does not require a server.

PUBLISH FREE (GitHub Pages)
1. Sign into GitHub and create a new repository (e.g. ra-sushi-photo-guide).
2. Upload the contents of this folder to the repository root.
3. In Settings > Pages, select Deploy from a branch, main, / (root), then Save.
4. Visit the resulting HTTPS address.
5. Run generate_qr.py, enter the real HTTPS address, and test the QR code on a phone before printing.

IMPORTANT: NOT APPROVED FOR PUBLIC ALLERGEN GUIDANCE
- Allergen flags are collected from the guide's allergen blocks and may include sauces; the PDF contains inconsistencies and typos.
- Pages 37 (Hibachi Shrimp description/ingredients show chicken), 19 (yellowtail cashews vs peanut allergen), 76 (mochi page includes poke-related sauce/allergens) need explicit review.
- Pages 39-40 (steak frites) have no allergens listed in source; do not treat them as allergen-free.
- Confirm which items are current at your restaurant, rights to publish corporate photos, and approved allergy language.
- The page currently displays a clear PREVIEW warning. Keep it until restaurant/corporate approval and full data quality checks.
- For guest service, avoid any "safe for allergy" or exclusion filter without approved cross-contact procedures.
