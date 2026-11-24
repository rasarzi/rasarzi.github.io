# Rasa Rezaei — personal website

A dependency-free, responsive single-page portfolio. No paid tools, hosting, backend, build system, tracking or external assets are needed.

## Local preview

Open `index.html` in a browser, or run `python -m http.server 8000` in this directory and visit http://localhost:8000.

## Publish for free

1. Create a public repository called `rasarzi.github.io` under your GitHub account (or use your existing repository of that name if present).
2. Upload the contents of this folder into the repository root, including the `cv` directory and `.nojekyll` file. Do not upload the enclosing folder as a subfolder.
3. Go to Settings → Pages → Build and deployment → Deploy from a branch. Select `main` and `/ (root)`, then Save.
4. Open https://rasarzi.github.io/ after deployment. Check all CV links.

To use a purchased or student domain later, configure GitHub Pages' custom-domain setting and the DNS records specified by GitHub. Update canonical URL, JSON-LD URL, robots.txt and sitemap.xml. Enable HTTPS. Submit the sitemap in Google Search Console if desired.

## Editing

- All website copy, links and conceptual technical diagrams are in `index.html`.
- `style.css` controls colors, layouts and responsive breakpoints.
- Replace the three PDFs in `cv/` to update CVs; retain filenames. These public copies have the original phone number removed.
- There is no portrait placeholder. An authentic photo can be added later if desired.
- Project links came from the provided CV PDF hyperlinks; check external destinations periodically. The V2 preprint is unreviewed and real-data evaluation is pending. The technical diagrams are explanatory, not experimental results.


## Logo assets
The four organization plates reference the original logo URLs (Wikimedia Commons for Microsoft, Vodafone and Sabancı University; Brandfetch for the Turkish investment platform Midas). The `*-offline.svg` files are visual reconstructions for offline display, not downloaded original brand files. When the actual image loads it replaces the reconstruction. Before publishing, run `python fetch-logos.py` on an internet-connected computer and confirm the original images replace the offline versions. The Deep Tech Club image references the official Sabancı student-life club directory. All brand marks remain the property of their respective owners; review the brand guidelines and obtain permission if required.
