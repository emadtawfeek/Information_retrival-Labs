# Information Retrieval Laboratory Package Validation

Original course validation completed on 25 September 2026. Explained student worksheets
and final package validation completed on 26 September 2026.

| Week | Reference DOCX/PDF | Student DOCX/PDF | Solution PY | Exercise PY | Data | Tested | Reference pages | Student pages |
|---|---|---|---|---|---|---|---|---|
| 01 | Yes | Yes | Yes | Yes | Yes | Yes | 4 | 5 |
| 02 | Yes | Yes | Yes | Yes | Yes | Yes | 4 | 5 |
| 03 | Yes | Yes | Yes | Yes | Yes | Yes | 4 | 5 |
| 04 | Yes | Yes | Yes | Yes | Yes | Yes | 4 | 5 |
| 05 | Yes | Yes | Yes | Yes | Yes | Yes | 5 | 5 |
| 06 | Yes | Yes | Yes | Yes | Yes | Yes | 5 | 5 |
| 07 | Yes | Yes | Yes | Yes | Yes | Yes | 5 | 5 |
| 08 | Yes | Yes | Yes | Yes | Yes | Yes | 5 | 5 |
| 09 | Yes | Yes | Yes | Yes | Yes | Yes | 5 | 5 |
| 10 | Yes | Yes | Yes | Yes | Yes | Yes | 7 | 5 |

## Execution and numerical validation

- All 27 delivered Python files executed successfully using Python 3.14.5 on Windows,
  including ten main programs, ten starters, and seven helper modules.
- All files ran from an unrelated working directory. Interactive sessions in Weeks 5, 6,
  and 10 also completed successfully. All ten printed worked examples were executed.
- 317 automated checks covered execution, matrix/postings agreement, parser errors,
  sorted unique postings, 100 varied posting-list intersections against a set oracle,
  loader filtering/fallback, TF/DF/IDF hand calculations, cosine, zero vectors, mismatched
  vector lengths, query weighting, evaluation denominators, deduplication, and nonpositive k.
- Weeks 6-10 have byte-identical document collections. Week 9 retrieval.py is byte-identical
  to Week 8's solution. Week 10's model matches Week 8's model on the shipped collection.
- Expected-output files were captured from real default runs. Numerical results are computed,
  not hard-coded. The default ranked query starts with doc4 (0.5123), doc9 (0.4326), and
  doc1 (0.3466), using the complete ten-document collection.
- Exercise TODOs are deliberate. No solution/helper file contains TODO placeholders.

## Lab 0: Python installation and requirements

- Lab_00_Setup includes Python 3.13.15's official Windows x64 installer,
  requirements.txt, copyable installation commands, and a course-specific guide in PDF
  and Markdown. Python 3.10 or later is sufficient for all labs; no additional
  packages are needed. The guide PDF was rendered and visually checked.
- AST inspection of all 27 lab Python files found exactly five standard-library imports
  (json, math, os, re, sys) and seven included local modules (evaluation, file_utils,
  indexing, preprocessing, ranking, retrieval, tfidf). All twelve are named in
  requirements.txt; no third-party pip entries are present. The file names the Python
  3.10+ runtime requirement and links to the official Python 3.13.15 release,
  Windows installer, and CPython source-code archive.
- The installer is 29,452,944 bytes. Its SHA-256 matches the value published on the official
  Python release page: `EDEC09C4853AEAE9AC36EFB8C9F95B6B8E2FEE65EEE56D9767A8B7C69C574403`. Windows reports a valid Python Software
  Foundation digital signature.
- The guide covers installation, version and standard-library checks, first runs, data-folder
  placement, common setup errors, and alternate operating-system downloads.

## Document and PDF validation

- Ten original A4 DOCX files and ten PDFs contain the same substantive material. Each PDF was exported
  directly from its corresponding DOCX by Microsoft Word.
- Each laboratory has all eleven required numbered sections. Main code listings match the
  delivered Python source exactly; the Week 10 sheet also includes all supporting modules.
- All 48 pages were rendered through the document skill's Poppler rasterization path
  using Word-exported PDFs and reviewed as full-size page images. The runtime had no bundled
  LibreOffice, so Word supplied the DOCX-to-PDF conversion.
- Prose, code, section headings, and table text were checked against extracted PDF content.
  Wrapped table cells were additionally reviewed visually. Equations, page numbers, table fit,
  margins, code legibility, and page transitions were checked. No clipping, missing content,
  blank pages, or unresolved layout defects remain.
- Typography is consistent: 18 pt titles, 16 pt main headings, 14 pt subheadings, 11 pt body,
  and 9 pt monospace code. Code blank-line spacing is compacted without removing source lines.

## Explained English student worksheets

- Ten additional Word worksheets and ten matching PDFs are linked in Student_Lab_Sheets_Index.md.
  Each has five A4 pages; all 50 student worksheet pages were reviewed visually
  at their full rendered size using the document skill's Poppler rasterization path.
- The worksheets include explained background, executed worked examples and output, exact
  excerpts from the weekly program, guided activities, prediction checkpoints, a blank test
  record, common errors, independent exercises, submission instructions, and exit questions.
- All ten worked examples were executed. Each code excerpt matches the supplied program's
  function source. Paragraph content was compared with extracted PDF text; every page passed
  the margin/overflow checks and visual inspection for readable code, tables, answer space,
  page transitions, and missing glyphs. No clipping or unresolved layout defects remain.
- Student answer spaces and test observations are intentionally blank. The original full
  reference sheets, Python programs, data, and requirements remain available beside them.
- The complete package now contains 20 Word documents and 21 PDFs, including the Lab 0 guide.

## Source and scope checks

The supplied PPTX and both Python files are the primary references. Weeks 1-6 preserve their
teaching progression and data structures, with small corrections documented in Course_README.md.
The supplied playlist could not be fetched, so no uninspected video content is claimed as a source.
All later teaching passages are short original documents. No external academic references were invented.

All student programs use the standard library, work offline, and derive paths from their script
location. Relevance sets are explicit teaching assumptions. Evaluation conclusions are limited to
the judged queries and this collection.

## Final directory tree

The complete tree is also available in Directory_Tree.txt.

```text
Information_Retrieval_Labs/
|-- Lab_00_Setup/
|   |-- python-3.13.15-amd64.exe
|   |-- README.md
|   |-- requirements.txt
|   |-- Setup_Guide.md
|   `-- Setup_Guide.pdf
|-- Week_01_File_Manipulation/
|   |-- data/
|   |   |-- notes.txt
|   |   `-- welcome.txt
|   |-- docs/
|   |   |-- doc1.txt
|   |   |-- doc2.txt
|   |   `-- doc3.txt
|   |-- exercises_lab01.py
|   |-- expected_output.txt
|   |-- IR_Lab_01_File_Manipulation.docx
|   |-- IR_Lab_01_File_Manipulation.pdf
|   |-- lab01_file_manipulation.py
|   |-- README.txt
|   |-- Student_Lab_Sheet_Week_01_Explained.docx
|   `-- Student_Lab_Sheet_Week_01_Explained.pdf
|-- Week_02_Regex_Text_Processing/
|   |-- data/
|   |   |-- paragraph.txt
|   |   `-- pattern_practice.txt
|   |-- exercises_lab02.py
|   |-- expected_output.txt
|   |-- IR_Lab_02_Regex_Text_Processing.docx
|   |-- IR_Lab_02_Regex_Text_Processing.pdf
|   |-- lab02_regex.py
|   |-- README.txt
|   |-- Student_Lab_Sheet_Week_02_Explained.docx
|   `-- Student_Lab_Sheet_Week_02_Explained.pdf
|-- Week_03_Preprocessing/
|   |-- docs/
|   |   |-- doc1.txt
|   |   |-- doc2.txt
|   |   |-- doc3.txt
|   |   |-- doc4.txt
|   |   `-- doc5.txt
|   |-- expected_output.txt
|   |-- IR_Lab_03_Preprocessing.docx
|   |-- IR_Lab_03_Preprocessing.pdf
|   |-- lab03_exercises.py
|   |-- lab03_solution.py
|   |-- README.txt
|   |-- Student_Lab_Sheet_Week_03_Explained.docx
|   `-- Student_Lab_Sheet_Week_03_Explained.pdf
|-- Week_04_Term_Document_Matrix/
|   |-- docs/
|   |   |-- doc1.txt
|   |   |-- doc2.txt
|   |   |-- doc3.txt
|   |   |-- doc4.txt
|   |   `-- doc5.txt
|   |-- expected_output.txt
|   |-- IR_Lab_04_Term_Document_Matrix.docx
|   |-- IR_Lab_04_Term_Document_Matrix.pdf
|   |-- lab04_exercises.py
|   |-- lab04_solution.py
|   |-- README.txt
|   |-- Student_Lab_Sheet_Week_04_Explained.docx
|   `-- Student_Lab_Sheet_Week_04_Explained.pdf
|-- Week_05_Boolean_Retrieval/
|   |-- docs/
|   |   |-- doc1.txt
|   |   |-- doc2.txt
|   |   |-- doc3.txt
|   |   |-- doc4.txt
|   |   `-- doc5.txt
|   |-- expected_output.txt
|   |-- IR_Lab_05_Boolean_Retrieval.docx
|   |-- IR_Lab_05_Boolean_Retrieval.pdf
|   |-- lab05_exercises.py
|   |-- lab05_solution.py
|   |-- README.txt
|   |-- Student_Lab_Sheet_Week_05_Explained.docx
|   `-- Student_Lab_Sheet_Week_05_Explained.pdf
|-- Week_06_Inverted_Index/
|   |-- docs/
|   |   |-- doc1.txt
|   |   |-- doc10.txt
|   |   |-- doc2.txt
|   |   |-- doc3.txt
|   |   |-- doc4.txt
|   |   |-- doc5.txt
|   |   |-- doc6.txt
|   |   |-- doc7.txt
|   |   |-- doc8.txt
|   |   `-- doc9.txt
|   |-- expected_output.txt
|   |-- IR_Lab_06_Inverted_Index.docx
|   |-- IR_Lab_06_Inverted_Index.pdf
|   |-- lab06_exercises.py
|   |-- lab06_solution.py
|   |-- README.txt
|   |-- Student_Lab_Sheet_Week_06_Explained.docx
|   `-- Student_Lab_Sheet_Week_06_Explained.pdf
|-- Week_07_TF_IDF/
|   |-- docs/
|   |   |-- doc1.txt
|   |   |-- doc10.txt
|   |   |-- doc2.txt
|   |   |-- doc3.txt
|   |   |-- doc4.txt
|   |   |-- doc5.txt
|   |   |-- doc6.txt
|   |   |-- doc7.txt
|   |   |-- doc8.txt
|   |   `-- doc9.txt
|   |-- expected_output.txt
|   |-- IR_Lab_07_TF_IDF.docx
|   |-- IR_Lab_07_TF_IDF.pdf
|   |-- lab07_exercises.py
|   |-- lab07_solution.py
|   |-- README.txt
|   |-- Student_Lab_Sheet_Week_07_Explained.docx
|   `-- Student_Lab_Sheet_Week_07_Explained.pdf
|-- Week_08_Vector_Space_Model/
|   |-- docs/
|   |   |-- doc1.txt
|   |   |-- doc10.txt
|   |   |-- doc2.txt
|   |   |-- doc3.txt
|   |   |-- doc4.txt
|   |   |-- doc5.txt
|   |   |-- doc6.txt
|   |   |-- doc7.txt
|   |   |-- doc8.txt
|   |   `-- doc9.txt
|   |-- expected_output.txt
|   |-- IR_Lab_08_Vector_Space_Model.docx
|   |-- IR_Lab_08_Vector_Space_Model.pdf
|   |-- lab08_exercises.py
|   |-- lab08_solution.py
|   |-- README.txt
|   |-- Student_Lab_Sheet_Week_08_Explained.docx
|   `-- Student_Lab_Sheet_Week_08_Explained.pdf
|-- Week_09_Retrieval_Evaluation/
|   |-- data/
|   |   `-- relevance.json
|   |-- docs/
|   |   |-- doc1.txt
|   |   |-- doc10.txt
|   |   |-- doc2.txt
|   |   |-- doc3.txt
|   |   |-- doc4.txt
|   |   |-- doc5.txt
|   |   |-- doc6.txt
|   |   |-- doc7.txt
|   |   |-- doc8.txt
|   |   `-- doc9.txt
|   |-- expected_output.txt
|   |-- IR_Lab_09_Retrieval_Evaluation.docx
|   |-- IR_Lab_09_Retrieval_Evaluation.pdf
|   |-- lab09_exercises.py
|   |-- lab09_solution.py
|   |-- README.txt
|   |-- retrieval.py
|   |-- Student_Lab_Sheet_Week_09_Explained.docx
|   `-- Student_Lab_Sheet_Week_09_Explained.pdf
|-- Week_10_IR_Project/
|   |-- data/
|   |   `-- relevance.json
|   |-- docs/
|   |   |-- doc1.txt
|   |   |-- doc10.txt
|   |   |-- doc2.txt
|   |   |-- doc3.txt
|   |   |-- doc4.txt
|   |   |-- doc5.txt
|   |   |-- doc6.txt
|   |   |-- doc7.txt
|   |   |-- doc8.txt
|   |   `-- doc9.txt
|   |-- evaluation.py
|   |-- expected_output.txt
|   |-- file_utils.py
|   |-- indexing.py
|   |-- IR_Lab_10_IR_Project.docx
|   |-- IR_Lab_10_IR_Project.pdf
|   |-- lab10_exercises.py
|   |-- main.py
|   |-- preprocessing.py
|   |-- ranking.py
|   |-- README.txt
|   |-- Student_Lab_Sheet_Week_10_Explained.docx
|   |-- Student_Lab_Sheet_Week_10_Explained.pdf
|   `-- tfidf.py
|-- .gitattributes
|-- .gitignore
|-- Course_README.md
|-- Directory_Tree.txt
|-- README.md
|-- Student_Lab_Sheets_Index.md
`-- Validation_Report.md
```
