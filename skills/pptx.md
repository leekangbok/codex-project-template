---
name: pptx
description: "Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill."
license: Proprietary. LICENSE.txt has complete terms
---

# PPTX Skill

## Quick Reference

| Task | Guide |
|------|-------|
| Read/analyze content | `python -m markitdown presentation.pptx` |
| Create from scratch | Use `pptxgenjs` |

---

## Reading Content

```bash
# Text extraction
python -m markitdown presentation.pptx
```

---

## Design Ideas

Don't create boring slides. Plain bullets on a white background won't impress anyone.

### Visual Excellence
- **Dominance**: One color should dominate (60-70% weight).
- **Contrast**: Use dark backgrounds for title/conclusion and light for content.
- **Visual Motif**: Repeat ONE distinctive element (e.g., rounded frames, specific icons) across every slide.

### Recommended Palettes
- **Midnight Executive**: `1E2761` (navy), `CADCFC` (ice blue), `FFFFFF` (white)
- **Forest & Moss**: `2C5F2D` (forest), `97BC62` (moss), `F5F5F5` (cream)
- **Charcoal Minimal**: `36454F` (charcoal), `F2F2F2` (off-white), `212121` (black)

### Layout Principles
- **Grid Layouts**: Use 2x2 grids or text-plus-illustration splits.
- **Stat Callouts**: Big numbers (60pt+) with small labels below.
- **Icon Usage**: Icons in small colored circles next to headers.

### Typography
- Titles: 36-44pt bold
- Body: 14-16pt
- Headers: 20-24pt bold

---

## QA (Required)

Always test your output. Your first render is almost never correct.

### Content QA
```bash
python -m markitdown output.pptx
```
Check for missing content, typos, or placeholder text (`xxxx`, `lorem ipsum`).

### Visual QA
Convert slides to images for inspection:
```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

Look for:
- Overlapping elements
- Text overflow or cut off
- Low-contrast text/icons
- Inconsistent alignment or margins (< 0.5")

---

## Dependencies
- `pip install "markitdown[pptx]"`
- `npm install -g pptxgenjs`
- LibreOffice (`soffice`)
- Poppler (`pdftoppm`)
