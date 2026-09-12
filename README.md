# Ian Burke's portfolio

Static HTML published through GitHub Pages. `index.html` is the portfolio; `resume.html` is the resume source. `Ian-Burke-Resume.pdf` is its downloadable print export.

`portfolio.html` is the three-page visual case-study portfolio. Its PDF is `Ian-Burke-Portfolio.pdf`. It has its own 12-by-8.5-inch print layout; export it using the CSS page size, background graphics on, and headers and footers off. Keep it separate from the one-page application resume.

Preview locally:

```sh
python3 -m http.server 8769 --bind 127.0.0.1
```

Open `http://127.0.0.1:8769/`. After editing the resume, open `/resume.html` in Chrome, choose Print, and save as PDF. Use Letter paper, 100% scale, and disable headers and footers. The print stylesheet sets the page margins and hides the navigation. Replace `Ian-Burke-Resume.pdf`, then confirm it remains one page with selectable text and working links.

Keep resume and portfolio descriptions consistent. Publish measured outcomes only when supported, distinguish pre-release projects from delivered work, and confirm employment dates before changing them.

## Resume layout alternatives

Open `/portfolio-options.html` to compare three simpler drafts: a one-page visual resume, three pages organized by project, and a two-page resume with selected work. Each has an HTML preview and a Letter-sized PDF. These are alternatives for review; the homepage download stays unchanged until a layout is selected.

Run `python3 scripts/build-resume-options.py` after changing the shared copy or layouts. Export each `portfolio-option-N.html` using its CSS page size, background graphics on, and headers and footers off to `Ian-Burke-Option-N.pdf`. Refresh the first-page previews in `images/` as well. Expected page counts are 1, 3, and 2.

`video-review-crop.css` hides the browser toolbar on the Narrative video-review screenshot across the gallery and portfolio layouts. It preserves the original image file. Re-export affected PDFs after changing the crop.
