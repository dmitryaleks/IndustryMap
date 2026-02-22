# Markdown-to-EPUB Conversion Guidelines for Agentic LLM

This document provides comprehensive instructions for converting the audiobook manuscript of *Silicon Foundations -- Japan's Hidden Dominance in the Semiconductor Supply Chain* from Markdown into a valid, accessible, professionally formatted EPUB 3.2 file. The source material is a single continuous Markdown document (`audiobook/v1/audiobook.md`) produced by applying the audiobook rewrite guidelines in `context/AUDIOBOOK_STYLE.md` to the print chapters in `book/`.

The conversion agent must produce an EPUB that passes epubcheck validation, meets WCAG 2.1 AA accessibility requirements, renders correctly across major reading systems (Apple Books, Kindle via KindleGen/KindlePreviewer, Kobo, Google Play Books, Readium), and presents the content with the typographic quality expected of a professional digital publication.

---

## 1. EPUB 3.2 Package Structure

### 1.1 Directory Layout

```
silicon-foundations.epub (ZIP container)
  mimetype                          (uncompressed, first entry)
  META-INF/
    container.xml
  OEBPS/
    content.opf                     (package document)
    toc.xhtml                       (EPUB 3 navigation document)
    toc.ncx                         (EPUB 2 NCX fallback)
    css/
      style.css                     (master stylesheet)
      fonts.css                     (font-face declarations, if embedded)
    fonts/                          (optional: embedded OTF/WOFF2 files)
    images/
      cover.jpg                     (front cover, 1600x2400px minimum)
    text/
      cover.xhtml
      title.xhtml
      copyright.xhtml
      dedication.xhtml              (if applicable)
      toc-page.xhtml                (printable table of contents)
      part-i.xhtml                  (part divider page)
      ch01.xhtml
      ch02.xhtml
      ...
      ch18.xhtml
      part-viii.xhtml
      appendix-a.xhtml
      appendix-b.xhtml
      appendix-c.xhtml              (omitted in audiobook; include if print-sourced)
      appendix-d.xhtml
      appendix-e.xhtml
      backmatter.xhtml              (about the author / colophon)
```

### 1.2 The mimetype File

The `mimetype` file must contain exactly `application/epub+zip` with no trailing newline and no byte-order mark. It must be stored uncompressed (compression method 0) as the first entry in the ZIP archive. This is a hard requirement of the EPUB specification; violation causes immediate validation failure.

### 1.3 container.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
```

No modifications are needed. This file is identical for all EPUB 3 publications.

---

## 2. Package Document (content.opf)

### 2.1 Required Metadata

```xml
<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0"
         unique-identifier="bookid" xml:lang="en">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">urn:uuid:GENERATE-UUID-HERE</dc:identifier>
    <dc:title>Silicon Foundations: Japan's Hidden Dominance in the Semiconductor Supply Chain</dc:title>
    <dc:language>en</dc:language>
    <dc:creator>IndustryMap Research</dc:creator>
    <dc:publisher>IndustryMap</dc:publisher>
    <dc:date>2026</dc:date>
    <dc:description>A comprehensive analysis of 62 Japanese companies that control critical chokepoints in the global semiconductor supply chain, with investment frameworks for technology investors.</dc:description>
    <dc:subject>Semiconductors</dc:subject>
    <dc:subject>Japan</dc:subject>
    <dc:subject>Investing</dc:subject>
    <dc:subject>Supply Chain</dc:subject>
    <dc:subject>Technology</dc:subject>
    <dc:rights>All rights reserved</dc:rights>
    <meta property="dcterms:modified">2026-02-22T00:00:00Z</meta>
    <meta property="schema:accessMode">textual</meta>
    <meta property="schema:accessModeSufficient">textual</meta>
    <meta property="schema:accessibilityFeature">structuralNavigation</meta>
    <meta property="schema:accessibilityFeature">tableOfContents</meta>
    <meta property="schema:accessibilityFeature">readingOrder</meta>
    <meta property="schema:accessibilityHazard">none</meta>
    <meta property="schema:accessibilitySummary">This publication is fully accessible with structured navigation, semantic markup, and a logical reading order.</meta>
  </metadata>
  <manifest>
    <!-- List all content documents, stylesheets, images, fonts -->
  </manifest>
  <spine>
    <!-- Reading order -->
  </spine>
</package>
```

### 2.2 Manifest Rules

- Every file inside `OEBPS/` must appear in the manifest with a unique `id` and correct `media-type`.
- The navigation document (`toc.xhtml`) must carry `properties="nav"`.
- The cover image item must carry `properties="cover-image"`.
- Allowed media types: `application/xhtml+xml`, `text/css`, `image/jpeg`, `image/png`, `image/svg+xml`, `application/font-woff`, `font/woff2`, `font/otf`, `application/x-dtbncx+xml`.
- Do not include any file that is not referenced in the manifest. Extraneous files cause epubcheck warnings.

### 2.3 Spine Rules

- The spine defines the reading order. List content documents in the exact order a reader would encounter them: cover, title page, copyright, table of contents, Part I divider, Chapter 1, Chapter 2, ... through Appendix E, backmatter.
- The cover page should carry `linear="no"` if it is purely decorative (image-only cover).
- The NCX fallback is referenced via the `toc` attribute on the `<spine>` element: `<spine toc="ncx">`.

---

## 3. Navigation Documents

### 3.1 EPUB 3 Navigation (toc.xhtml)

The `toc.xhtml` file provides the primary navigation. It must contain a `<nav epub:type="toc">` element with a nested ordered list.

```xhtml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en">
<head>
  <title>Table of Contents</title>
  <link rel="stylesheet" type="text/css" href="css/style.css"/>
</head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>Contents</h1>
    <ol>
      <li><a href="text/ch01.xhtml">Chapter 1: Why Japan Matters</a></li>
      <li><a href="text/ch02.xhtml">Chapter 2: How a Chip Is Made</a></li>
      <!-- ... all 18 chapters ... -->
      <li><a href="text/appendix-a.xhtml">Appendix A: Japanese Company Cards</a></li>
      <!-- ... all 5 appendices ... -->
    </ol>
  </nav>
  <nav epub:type="landmarks" hidden="">
    <h2>Landmarks</h2>
    <ol>
      <li><a epub:type="cover" href="text/cover.xhtml">Cover</a></li>
      <li><a epub:type="toc" href="toc.xhtml">Table of Contents</a></li>
      <li><a epub:type="bodymatter" href="text/ch01.xhtml">Start of Content</a></li>
    </ol>
  </nav>
</body>
</html>
```

Rules:
- Include Part dividers as nested `<ol>` groups if the reading system supports hierarchical TOC display. If not, flat-list all chapters.
- Every chapter and appendix must appear in the TOC. Part dividers are optional.
- The `landmarks` nav is required for accessibility. Include at minimum: `cover`, `toc`, and `bodymatter`.

### 3.2 NCX Fallback (toc.ncx)

Provide an NCX file for backward compatibility with EPUB 2 reading systems and older Kindle devices. The NCX mirrors the TOC structure using `<navPoint>` elements with sequential `playOrder` values starting at 1.

---

## 4. Content Conversion: Markdown to XHTML

### 4.1 XHTML Document Template

Every content file must be a well-formed XHTML document:

```xhtml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en">
<head>
  <title>Chapter 1: Why Japan Matters</title>
  <link rel="stylesheet" type="text/css" href="../css/style.css"/>
</head>
<body epub:type="bodymatter">
  <section epub:type="chapter" role="doc-chapter" aria-label="Chapter 1: Why Japan Matters">
    <!-- chapter content here -->
  </section>
</body>
</html>
```

Rules:
- Every `<html>` element must declare the XHTML namespace and `xml:lang="en"`.
- Every `<head>` must contain a `<title>` matching the chapter title.
- The `epub:type` attribute provides semantic inflection for reading systems.
- The `role` attribute provides ARIA semantics for assistive technology.
- Self-closing tags must use XML syntax: `<br/>`, `<hr/>`, `<img ... />`.

### 4.2 Mapping Markdown Elements to XHTML

| Markdown Element | XHTML Equivalent | Notes |
|---|---|---|
| `# Chapter Title` | `<h1>` | One per XHTML file. Include chapter number. |
| `## Section` | `<h2>` | Major sections within a chapter. |
| `### Subsection` | `<h3>` | Company profiles, sub-topics. |
| `#### Sub-subsection` | `<h4>` | Rarely used; financial detail breakdowns. |
| Paragraph text | `<p>` | Standard paragraph. |
| `**bold**` | `<strong>` | Semantic emphasis, not visual. |
| `*italic*` | `<em>` | Semantic emphasis, not visual. |
| `> blockquote` | `<blockquote>` | Chapter thesis, pull quotes. |
| `- bullet` | `<ul><li>` | Unordered list. |
| `1. item` | `<ol><li>` | Ordered list. |
| `---` | `<hr/>` | Thematic break. Style with CSS, not presentational attributes. |
| `[text](url)` | `<a href="url">text</a>` | External links. Add `target="_blank"` for web URLs. |
| `` `code` `` | `<code>` | Inline code. Rare in this book. |
| Code block | `<pre><code>` | Should not appear in audiobook prose. If present in print source, convert to prose or omit. |

### 4.3 Audiobook Source Considerations

The audiobook manuscript (`audiobook/v1/audiobook.md`) has already been processed through the audiobook rewrite guidelines and may lack Markdown formatting. If the source is pure prose (no headers, no bold, no tables), the conversion agent must:

1. **Reintroduce structural markup.** The audiobook prose uses verbal signposts ("Chapter Six. Lithography") instead of Markdown headers. Convert these back to proper `<h1>` elements for EPUB navigation and structure.
2. **Identify section breaks.** The audiobook uses paragraph breaks and transitional sentences where the print version uses `##` headers. Reintroduce `<h2>` elements at these natural section boundaries to enable in-chapter navigation.
3. **Preserve the prose.** Do not revert the audiobook's prose simplifications. The EPUB should carry the audiobook's natural-language text, not the print version's tables and dense formatting. The audiobook version is the definitive text for this EPUB.

### 4.4 Special Content Patterns

#### 4.4.1 Chapter Thesis (Opening Blockquote)

Each chapter opens with a thesis statement. In the print version, this is a Markdown blockquote (`>`). In the audiobook version, it is a declarative opening paragraph. Wrap it in a styled `<blockquote>` with a distinguishing class:

```xhtml
<blockquote class="chapter-thesis" epub:type="epigraph">
  <p>Japan controls an extraordinary number of critical chokepoints in the global semiconductor supply chain -- positions that are structural, not incidental -- and most investors do not fully appreciate this dominance.</p>
</blockquote>
```

#### 4.4.2 Company Profile Sections

When a chapter introduces a company profile (the audiobook version begins with a transitional sentence like "Let us now turn to Shin-Etsu Chemical..."), wrap the company section in a semantically distinct container:

```xhtml
<section class="company-profile" aria-label="Shin-Etsu Chemical">
  <h3>Shin-Etsu Chemical</h3>
  <p>Let us now turn to Shin-Etsu Chemical, the largest silicon wafer manufacturer in the world...</p>
  <!-- remaining profile paragraphs -->
</section>
```

#### 4.4.3 Investment Perspective Asides

Investment analysis passages should be wrapped in an `<aside>` element:

```xhtml
<aside class="investment-perspective" epub:type="sidebar" role="doc-tip">
  <h4>Investment Perspective</h4>
  <p>From an investment standpoint, Gun Ei Chemical is one of the most compelling names in this study...</p>
</aside>
```

#### 4.4.4 Financial Data in Prose

The audiobook version converts tables to flowing prose. In the EPUB, preserve this prose form but add semantic microdata where appropriate:

```xhtml
<p>The company trades at a price-to-earnings ratio of about twenty-two times
and a price-to-book of just under two. Revenue has been growing at roughly
sixteen percent, with operating margins near fifteen percent.</p>
```

Do **not** revert prose back to tables. The audiobook prose is the definitive text. If the EPUB is later produced from the print source instead, tables should be properly marked up (see Section 4.5).

#### 4.4.5 Em Dashes

The source uses `--` for em dashes. Convert to the Unicode em dash character (U+2014, `&#x2014;` or `&mdash;`). Optionally wrap in thin hair spaces for improved typography:

```xhtml
<p>Lasertec Corporation&#x2014;the sole global supplier of EUV photomask
inspection equipment&#x2014;occupies what may be the most absolute monopoly
in the entire semiconductor supply chain.</p>
```

Consistency is paramount. Use either hair-spaced or unspaced em dashes throughout, never a mix.

### 4.5 Table Markup (Print Source Only)

If producing the EPUB from the print chapters in `book/` rather than the audiobook manuscript, tables must be properly marked up with accessibility attributes:

```xhtml
<table class="financial-metrics" role="table" aria-label="Key financial metrics for Shin-Etsu Chemical">
  <caption>Key Financial Metrics</caption>
  <thead>
    <tr>
      <th scope="col">Metric</th>
      <th scope="col">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PER</td>
      <td>21.5x</td>
    </tr>
    <!-- additional rows -->
  </tbody>
</table>
```

Rules:
- Every table must have a `<caption>` or `aria-label`.
- Use `<thead>` and `<tbody>`.
- Use `scope="col"` on column headers, `scope="row"` on row headers.
- For comparison tables with both row and column headers, use `id`/`headers` attributes for complex cell associations.
- Tables must linearize sensibly when CSS is disabled (reading order: left-to-right, top-to-bottom).

---

## 5. CSS Styling

### 5.1 Design Principles

- **Reflowable layout.** This is a text-heavy analytical book. Use reflowable EPUB, not fixed layout. All dimensions must use relative units (`em`, `rem`, `%`). Never use `px` for font sizes or margins.
- **Reading system compatibility.** Many reading systems override publisher CSS. Design defensively: use a clean, minimal stylesheet that degrades gracefully when overridden.
- **Dark mode support.** Use `prefers-color-scheme` media queries or avoid hardcoding background colors. Reading systems increasingly support dark mode; hardcoded white backgrounds create poor experiences.
- **Font stacking.** Always provide a generic fallback: `font-family: "Source Serif Pro", Georgia, serif;`.

### 5.2 Master Stylesheet (style.css)

```css
/* === Base Typography === */

body {
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.6;
  margin: 1em;
  text-align: justify;
  hyphens: auto;
  -webkit-hyphens: auto;
  orphans: 2;
  widows: 2;
}

/* === Headings === */

h1 {
  font-size: 1.8em;
  font-weight: bold;
  text-align: center;
  margin-top: 2em;
  margin-bottom: 1em;
  line-height: 1.2;
  page-break-before: always;
}

h2 {
  font-size: 1.3em;
  font-weight: bold;
  margin-top: 1.5em;
  margin-bottom: 0.5em;
  line-height: 1.3;
}

h3 {
  font-size: 1.1em;
  font-weight: bold;
  margin-top: 1.2em;
  margin-bottom: 0.4em;
}

h4 {
  font-size: 1em;
  font-weight: bold;
  font-style: italic;
  margin-top: 1em;
  margin-bottom: 0.3em;
}

/* === Paragraphs === */

p {
  margin-top: 0;
  margin-bottom: 0.5em;
  text-indent: 1.5em;
}

p:first-of-type,
blockquote + p,
h1 + p, h2 + p, h3 + p, h4 + p {
  text-indent: 0;
}

/* === Chapter Thesis / Epigraph === */

blockquote.chapter-thesis {
  font-style: italic;
  margin: 1.5em 2em;
  padding: 0;
  border: none;
  text-indent: 0;
}

blockquote.chapter-thesis p {
  text-indent: 0;
}

/* === Company Profile Sections === */

section.company-profile {
  margin-top: 1.5em;
  padding-top: 0.5em;
  border-top: 1px solid #ccc;
}

/* === Investment Perspective Aside === */

aside.investment-perspective {
  margin: 1em 1.5em;
  padding: 0.8em 1em;
  border-left: 3px solid #336699;
  background-color: #f8f9fa;
  font-size: 0.95em;
}

aside.investment-perspective h4 {
  font-size: 1em;
  font-style: normal;
  margin-top: 0;
  color: #336699;
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  aside.investment-perspective {
    background-color: #1a1a2e;
    border-left-color: #6699cc;
  }
  aside.investment-perspective h4 {
    color: #6699cc;
  }
  section.company-profile {
    border-top-color: #444;
  }
}

/* === Tables (print-source EPUB only) === */

table {
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
  font-size: 0.9em;
}

caption {
  font-weight: bold;
  margin-bottom: 0.5em;
  text-align: left;
}

th, td {
  padding: 0.4em 0.6em;
  border-bottom: 1px solid #ddd;
  text-align: left;
  vertical-align: top;
}

th {
  font-weight: bold;
  border-bottom: 2px solid #999;
}

/* === Lists === */

ul, ol {
  margin: 0.5em 0 0.5em 1.5em;
  padding: 0;
}

li {
  margin-bottom: 0.3em;
}

/* === Horizontal Rules === */

hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 1.5em 2em;
}

/* === Part Divider Pages === */

section.part-divider {
  text-align: center;
  padding-top: 30%;
}

section.part-divider h1 {
  font-size: 2em;
  page-break-before: always;
}

section.part-divider p.part-subtitle {
  font-size: 1.2em;
  font-style: italic;
  margin-top: 0.5em;
}

/* === Cover === */

section.cover {
  text-align: center;
  padding: 0;
  margin: 0;
}

section.cover img {
  max-width: 100%;
  max-height: 100%;
}

/* === Title Page === */

section.title-page {
  text-align: center;
  padding-top: 20%;
}

section.title-page h1 {
  font-size: 2.2em;
  page-break-before: auto;
}

section.title-page p.subtitle {
  font-size: 1.3em;
  font-style: italic;
  margin-top: 0.8em;
}

section.title-page p.author {
  font-size: 1.1em;
  margin-top: 2em;
}

/* === Glossary (Appendix E) === */

dl.glossary {
  margin: 1em 0;
}

dl.glossary dt {
  font-weight: bold;
  margin-top: 0.8em;
}

dl.glossary dd {
  margin-left: 1.5em;
  margin-bottom: 0.3em;
}

/* === Footnotes / Endnotes === */

aside[epub|type~="footnote"] {
  font-size: 0.85em;
  margin: 0.5em 1em;
  padding: 0.3em;
  border-top: 1px solid #ccc;
}
```

### 5.3 Font Embedding

Font embedding is optional. If fonts are embedded:
- Use WOFF2 format for maximum compatibility and compression.
- Include Regular, Bold, Italic, and BoldItalic weights at minimum.
- Declare `@font-face` rules in a separate `fonts.css` file.
- Ensure font licenses permit embedding. Libre/OFL-licensed fonts (Source Serif Pro, Noto Serif, Literata) are safe choices.
- Apply EPUB font obfuscation (IDPF algorithm) if required by the font license. Reference the obfuscation in `encryption.xml` inside `META-INF/`.

### 5.4 CSS Properties to Avoid

The following CSS properties are poorly supported or actively harmful in EPUB reading systems:
- `position: fixed` or `position: absolute` -- breaks reflow.
- `float` -- inconsistent across reading systems; use `text-align` instead.
- `display: flex` or `display: grid` -- limited support in older reading systems.
- `@font-face` with `.ttf` files -- use `.woff2` or `.otf` instead.
- `background-image` for decorative elements -- use `<img>` in XHTML.
- `column-count` -- reading systems manage pagination; do not impose columns.
- `!important` on font sizes -- prevents user accessibility overrides.

---

## 6. Book Front Matter

### 6.1 Cover Page (cover.xhtml)

```xhtml
<body>
  <section class="cover" epub:type="cover">
    <img src="../images/cover.jpg" alt="Silicon Foundations: Japan's Hidden Dominance in the Semiconductor Supply Chain -- Book Cover"/>
  </section>
</body>
```

- The cover image should be JPEG, minimum 1600x2400 pixels (portrait, 2:3 aspect ratio).
- The `alt` attribute must include the book title for accessibility.
- Amazon KDP requires a cover image of at least 2500 pixels on the longest side.

### 6.2 Title Page (title.xhtml)

```xhtml
<body>
  <section class="title-page" epub:type="titlepage">
    <h1>Silicon Foundations</h1>
    <p class="subtitle">Japan's Hidden Dominance in the Semiconductor Supply Chain</p>
    <p class="author">IndustryMap Research</p>
    <p class="year">2026</p>
  </section>
</body>
```

### 6.3 Copyright Page (copyright.xhtml)

Include: copyright statement, edition information, ISBN (if assigned), rights notice, disclaimer that financial data is for informational purposes and not investment advice. Use `epub:type="copyright-page"`.

### 6.4 Table of Contents Page (toc-page.xhtml)

A visible, printable table of contents page separate from the navigation document. Lists all parts, chapters, and appendices with page-break-before on the page. Use `epub:type="toc"`.

---

## 7. Part Divider Pages

The book is organized into eight parts. Each part should have a dedicated divider page:

```xhtml
<body>
  <section class="part-divider" epub:type="part">
    <h1>Part I</h1>
    <p class="part-subtitle">Foundations</p>
  </section>
</body>
```

Part dividers are brief, visually centered pages that create natural pauses in the reading experience. They should force a page break before and after.

---

## 8. Chapter Content Structure

### 8.1 Chapter File Template

```xhtml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en">
<head>
  <title>Chapter 1: Why Japan Matters</title>
  <link rel="stylesheet" type="text/css" href="../css/style.css"/>
</head>
<body epub:type="bodymatter">
  <section epub:type="chapter" role="doc-chapter" aria-label="Chapter 1: Why Japan Matters">
    <h1>Chapter 1<br/>Why Japan Matters</h1>

    <blockquote class="chapter-thesis" epub:type="epigraph">
      <p>Japan controls an extraordinary number of critical chokepoints...</p>
    </blockquote>

    <h2>The Invisible Hand</h2>
    <p>Every advanced chip manufactured anywhere in the world passes through
    Japanese hands at least twenty times before it reaches a consumer device.</p>

    <!-- remaining sections -->

  </section>
</body>
</html>
```

### 8.2 Chapter Numbering in Headings

Format the `<h1>` as:
```xhtml
<h1>Chapter 1<br/>Why Japan Matters</h1>
```

The `<br/>` creates a visual line break between the chapter number and title. The CSS `h1` styles ensure centered display. For appendices:
```xhtml
<h1>Appendix A<br/>Japanese Company Cards</h1>
```

### 8.3 Section IDs for Deep Linking

Every `<h2>` and `<h3>` should have an `id` attribute for potential cross-references and enhanced TOC entries:

```xhtml
<h2 id="the-invisible-hand">The Invisible Hand</h2>
<h3 id="shin-etsu-chemical">Shin-Etsu Chemical</h3>
```

Use lowercase kebab-case derived from the heading text. These IDs enable:
- Deep links in the TOC navigation (`href="text/ch01.xhtml#the-invisible-hand"`)
- Cross-chapter references (`href="text/ch04.xhtml#shin-etsu-chemical"`)

---

## 9. Appendix-Specific Formatting

### 9.1 Appendix A -- Japanese Company Cards

Each company card becomes a `<section class="company-card">` with:
- `<h3>` for the company name
- Structured profile paragraphs
- Consistent ordering: introduction, products, supply chain, financials

In the audiobook EPUB, these are brief prose profiles (two to three sentences per company). In a print-source EPUB, they would include the full structured cards.

### 9.2 Appendix B -- Global Ecosystem

Same structure as Appendix A but briefer. Group companies under `<h2>` headings by category (Foundries, Memory, Equipment, IDMs, EDA/IP, Fabless).

### 9.3 Appendix C -- Supply Chain Edge List

If included (print EPUB only, omitted from audiobook EPUB), present the edge list as a structured table with sortable columns: Supplier, Client, Relationship Type, Category. Apply the table markup rules from Section 4.5.

### 9.4 Appendix D -- Evaluation Methodology

Convert the scoring rubric into structured content. Use `<dl>` (definition lists) for dimension descriptions and `<table>` for scoring grids where appropriate. In the audiobook EPUB, this is narrative prose.

### 9.5 Appendix E -- Glossary

Use a `<dl class="glossary">` (definition list) for the glossary:

```xhtml
<dl class="glossary" epub:type="glossary">
  <dt id="term-cmp">Chemical Mechanical Planarization (CMP)</dt>
  <dd>The process of polishing a wafer surface to atomic-level flatness using a combination of chemical etching and mechanical abrasion. Essential for multi-patterning lithography at advanced nodes.</dd>

  <dt id="term-euv">Extreme Ultraviolet Lithography (EUV)</dt>
  <dd>Lithography using 13.5-nanometer wavelength light, enabling circuit features below 7 nanometers. Supplied exclusively by ASML.</dd>
</dl>
```

Add `id` attributes to each `<dt>` to enable cross-linking from chapter text.

---

## 10. Accessibility Requirements

### 10.1 WCAG 2.1 AA Compliance

The EPUB must meet WCAG 2.1 Level AA. Key requirements:

- **Text alternatives:** Every `<img>` must have a meaningful `alt` attribute. The cover image alt text should include the book title.
- **Logical reading order:** The DOM order must match the visual reading order. Do not use CSS to visually reorder content.
- **Semantic structure:** Use heading levels sequentially (`h1` > `h2` > `h3`). Do not skip levels.
- **Color contrast:** Text and background colors must meet a 4.5:1 contrast ratio for body text, 3:1 for large text. The default stylesheet above meets this requirement with black-on-white.
- **Language declaration:** The `xml:lang="en"` attribute on `<html>` is mandatory. For Japanese company names rendered in romaji, no language change is needed. If any content were in Japanese script, use `<span xml:lang="ja">`.

### 10.2 EPUB Accessibility Metadata

The package document must include the `schema:accessMode`, `schema:accessModeSufficient`, `schema:accessibilityFeature`, `schema:accessibilityHazard`, and `schema:accessibilitySummary` metadata properties as shown in Section 2.1.

### 10.3 Page Navigation (Optional)

For mapping to a print edition's page numbers, include a `<nav epub:type="page-list">` in the navigation document. This is optional for a digital-first publication but required for publications with a print counterpart.

### 10.4 ARIA Landmarks

Use ARIA roles on structural elements:
- `role="doc-chapter"` on chapter `<section>` elements
- `role="doc-appendix"` on appendix `<section>` elements
- `role="doc-toc"` on the table of contents `<nav>`
- `role="doc-glossary"` on the glossary `<section>` in Appendix E
- `role="doc-tip"` on investment perspective `<aside>` elements

---

## 11. Typography and Punctuation

### 11.1 Typographic Characters

Convert all ASCII approximations to proper Unicode characters during conversion:

| ASCII Source | Unicode Target | Entity | Description |
|---|---|---|---|
| `--` | --- | `&#x2014;` | Em dash |
| `...` | ... | `&#x2026;` | Ellipsis |
| `"text"` | "text" | `&#x201C;` / `&#x201D;` | Curly double quotes |
| `'text'` | 'text' | `&#x2018;` / `&#x2019;` | Curly single quotes |
| `isn't` | isn't | `&#x2019;` | Typographic apostrophe |
| `1/2` | 1/2 | `&#xBD;` | Vulgar fraction (when appropriate) |

### 11.2 Non-Breaking Spaces

Insert non-breaking spaces (`&#xa0;` or `&nbsp;`) in the following contexts:
- Between a number and its unit: `300&#xa0;mm`, `9.4&#xa0;trillion&#xa0;yen`
- Before a percent sign: `42&#xa0;percent` (though in audiobook prose, "percent" is a word, not a symbol)
- After chapter/appendix labels in cross-references: `Chapter&#xa0;6`
- Between initials and surnames if any appear in the text

### 11.3 Hyphenation

Enable CSS hyphenation (`hyphens: auto`) for justified text. Disable it for headings (`hyphens: none`). Some reading systems ignore this property, which is acceptable.

---

## 12. Content Sanitization

### 12.1 Elements to Strip

The conversion agent must remove the following from the source material before or during XHTML conversion:

- **CMP identifiers:** Any occurrence of `CMP-0001` through `CMP-0110` must be stripped.
- **File references:** References to `graph.json`, `evaluation_progress.json`, `CMP-*.json`, or any data file path.
- **Data source footers:** Lines matching `*Data sources: CMP-...` at chapter ends.
- **Progress tracking metadata:** Session logs, status tables, agent instructions.
- **Raw Markdown formatting artifacts:** Leftover `**`, `*`, `#`, `---`, `>` markers that were not converted to XHTML.
- **Internal cross-reference IDs:** Any database or internal tracking identifiers.

### 12.2 Elements to Preserve

- **Company names** in full, as written in the source.
- **Ticker symbols** where they appear in the audiobook text (already reduced to one per chapter by the audiobook rewrite).
- **Numerical facts** exactly as stated in the source. Do not alter data.
- **Chapter structure** and reading order.
- **All prose content.** The conversion is structural, not editorial. Do not rewrite sentences.

---

## 13. Cross-References

### 13.1 Internal Links

Convert textual cross-references to XHTML hyperlinks:

Source (audiobook prose): "as we will explore in Chapter Eight, on photoresists and chemicals"

XHTML:
```xhtml
<p>as we will explore in <a href="ch08.xhtml">Chapter Eight, on photoresists and chemicals</a></p>
```

Rules:
- Link the full descriptive phrase, not just the chapter number.
- Use relative paths (`ch08.xhtml`, not `../text/ch08.xhtml`) when linking within the same directory.
- Do not over-link. If a chapter is mentioned in passing without substantive cross-reference intent, do not create a link.

### 13.2 External Links

The book should contain no external URLs in the body text. If the source contains website references (e.g., company websites), convert them to footnotes or omit them. EPUB readers handle external links inconsistently, and broken links degrade the reading experience.

---

## 14. EPUB Validation

### 14.1 epubcheck

The final EPUB file must pass validation with epubcheck version 5.x with zero errors and zero warnings. Common validation failures to prevent:

| Issue | Prevention |
|---|---|
| Malformed XHTML | Validate every XHTML file individually before packaging. Ensure all tags are closed, attributes are quoted, and self-closing tags use `/>`. |
| Missing manifest entries | Cross-check every file in `OEBPS/` against the manifest in `content.opf`. |
| Incorrect media types | Use the exact MIME types specified in EPUB 3.2. |
| NCX `playOrder` gaps | Assign sequential integers starting at 1 with no gaps. |
| Missing `dc:identifier` | Always include a UUID or ISBN. |
| Missing `dcterms:modified` | Always include the modification timestamp in ISO 8601. |
| Unreferenced resources | Remove any file not referenced in the manifest. |
| Non-UTF-8 encoding | Save all text files as UTF-8 without BOM. |

### 14.2 Reading System Testing

After epubcheck validation, test the EPUB in at minimum:

1. **Apple Books** (macOS/iOS) -- The most standards-compliant reading system.
2. **Kindle Previewer 3** -- Convert via KindleGen/KindlePreviewer and verify. Amazon applies aggressive CSS overrides; verify that the book remains readable.
3. **Calibre viewer** -- A good cross-platform baseline.
4. **Google Play Books** (web or Android) -- Verify table rendering if tables are present.

### 14.3 Accessibility Validation

Run the EPUB through the Ace by DAISY accessibility checker. Address all violations and best-practice warnings. Key checks:
- Heading hierarchy is sequential and complete.
- All images have alt text.
- Tables have captions and proper header markup.
- Language is declared.
- Reading order matches DOM order.

---

## 15. ZIP Packaging

### 15.1 Building the EPUB Archive

The EPUB file is a ZIP archive with specific requirements:

```bash
# Step 1: Write mimetype uncompressed as first entry
echo -n "application/epub+zip" > mimetype

# Step 2: Create the ZIP with mimetype first, uncompressed
zip -X0 silicon-foundations.epub mimetype

# Step 3: Add remaining content with compression
zip -Xr9 silicon-foundations.epub META-INF/ OEBPS/
```

Rules:
- The `mimetype` file must be the first entry.
- The `mimetype` file must be uncompressed (flag `-0`).
- The `mimetype` file must not have an extra field in its ZIP header (flag `-X`).
- All other files should be compressed with deflate.
- Do not include OS-specific files (`.DS_Store`, `Thumbs.db`, `__MACOSX/`).
- Do not include hidden files or version control directories.

---

## 16. Multi-Version Considerations

### 16.1 Audiobook EPUB vs Print EPUB

This project may produce two EPUB variants:

| Feature | Audiobook EPUB | Print EPUB |
|---|---|---|
| Source | `audiobook/v1/audiobook.md` | `book/ch*.md` and `book/appendix-*.md` |
| Tables | Converted to prose (no `<table>` elements) | Full table markup with accessibility attributes |
| Numbers | Spelled out ("forty-two percent") | Numeric ("42%") |
| Ticker symbols | At most one per chapter, natural speech | Full, in structured company headers |
| CMP IDs | Stripped entirely | Stripped entirely |
| Appendix C | Omitted | Included with full edge list table |
| Tone | Conversational, signposted | Analytical, reference-oriented |
| Target length | ~158K words (similar to print) | ~158K words |

The conversion agent must confirm which source variant is being processed and apply the appropriate rules. The structural XHTML and CSS are identical between variants; only the content handling differs.

### 16.2 Kindle (KF8/AZW3) Compatibility

For Amazon distribution, the EPUB must be convertible to KF8 format via Kindle Previewer or KindleGen. Known compatibility requirements:

- Avoid `epub:type` namespace on elements that Kindle does not process (Kindle ignores `epub:type` but does not error on it).
- Include the NCX fallback for Kindle's legacy navigation.
- Embed fonts using IDPF obfuscation, not Adobe obfuscation (Kindle only supports IDPF).
- Keep CSS simple; Kindle overrides many properties.
- Test that the cover image appears in the Kindle library thumbnail.

---

## 17. Agent Workflow

### 17.1 Pre-Conversion Checklist

Before beginning conversion, the agent must verify:

- [ ] Source manuscript exists and is complete (`audiobook/v1/audiobook.md` or `book/` directory).
- [ ] `context/BOOK_PLAN_AND_PROGRESS.md` confirms all chapters are written.
- [ ] Cover image is available or a placeholder is designated.
- [ ] Book metadata (title, author, description, ISBN if any) is confirmed.
- [ ] Target variant (audiobook or print) is specified.

### 17.2 Conversion Sequence

1. **Parse the source manuscript.** Split on chapter boundaries. Identify all chapters and appendices.
2. **Create the directory structure** as specified in Section 1.1.
3. **Write front matter files:** cover, title, copyright, TOC page.
4. **Write part divider files** for each of the eight parts.
5. **Convert each chapter** to XHTML, applying all rules in Sections 4 and 8.
6. **Convert each appendix** to XHTML, applying appendix-specific rules in Section 9.
7. **Write the CSS stylesheet** (`style.css` and optionally `fonts.css`).
8. **Build the navigation documents** (`toc.xhtml` and `toc.ncx`).
9. **Write `content.opf`** with complete metadata, manifest, and spine.
10. **Write `container.xml`** and `mimetype`.
11. **Validate** with epubcheck.
12. **Package** into the final `.epub` ZIP file.
13. **Test** in at least two reading systems.

### 17.3 Quality Checklist

Before delivering the final EPUB, verify:

- [ ] epubcheck reports zero errors and zero warnings.
- [ ] Ace accessibility checker reports no violations.
- [ ] All 18 chapters and included appendices appear in the TOC navigation.
- [ ] The cover image displays correctly in reading system library views.
- [ ] All internal cross-reference links resolve correctly.
- [ ] No CMP identifiers, file references, or data source footers remain in the text.
- [ ] Em dashes, curly quotes, and ellipses use proper Unicode characters.
- [ ] The CSS renders acceptably with and without publisher stylesheet overrides.
- [ ] Dark mode does not produce unreadable color combinations.
- [ ] Heading hierarchy passes sequential-heading validation (no skipped levels).
- [ ] Every `<img>` has a non-empty `alt` attribute.
- [ ] The `mimetype` file is the first entry in the ZIP and is uncompressed.
- [ ] No OS-specific files (`.DS_Store`, `Thumbs.db`) are included in the archive.

---

## 18. File Naming Conventions

| Content | Filename | Notes |
|---|---|---|
| Cover page | `cover.xhtml` | |
| Title page | `title.xhtml` | |
| Copyright | `copyright.xhtml` | |
| TOC page | `toc-page.xhtml` | Visible TOC, distinct from `toc.xhtml` nav |
| Part dividers | `part-i.xhtml` through `part-viii.xhtml` | Roman numerals, lowercase |
| Chapters | `ch01.xhtml` through `ch18.xhtml` | Zero-padded two-digit numbers |
| Appendices | `appendix-a.xhtml` through `appendix-e.xhtml` | Lowercase letter suffix |
| Back matter | `backmatter.xhtml` | |
| Navigation | `toc.xhtml` | EPUB 3 nav document |
| NCX | `toc.ncx` | EPUB 2 fallback |
| Stylesheet | `css/style.css` | |
| Font declarations | `css/fonts.css` | Optional |
| Cover image | `images/cover.jpg` | |
| Package document | `content.opf` | |

All filenames use lowercase, hyphens for word separation, and no spaces.

---

## 19. Metadata for Distribution Platforms

### 19.1 Amazon KDP

- Requires cover image >= 2500px on longest side.
- Requires `dc:language` and `dc:title`.
- Subtitle goes in a separate metadata field during upload, not in `dc:title`.
- Categories and keywords are set during KDP upload, not in EPUB metadata.

### 19.2 Apple Books

- Requires `dc:identifier` (ISBN preferred, UUID acceptable).
- Supports `ibooks:specified-fonts` meta property for font embedding.
- Add `<meta property="ibooks:specified-fonts">true</meta>` if embedding fonts.

### 19.3 Google Play Books

- Accepts EPUB 3.2 directly.
- Requires ISBN for commercial distribution.
- Metadata in `content.opf` is used for the store listing.

### 19.4 Kobo

- Accepts EPUB 3.2 directly.
- Test with Kobo Desktop or a Kobo e-reader for kepub-specific rendering.

---

This concludes the Markdown-to-EPUB conversion guidelines. The agent should follow these instructions precisely to produce a professional-grade EPUB that meets modern accessibility standards and renders correctly across all major reading platforms.
