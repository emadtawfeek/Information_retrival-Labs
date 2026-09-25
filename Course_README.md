# Information Retrieval Practical Laboratories

Faculty of Computers and Information Systems

Ten undergraduate laboratories, each designed for approximately two practical hours.
Begin with local file manipulation and finish with an integrated command-line search engine.

## Requirements and first run

Use Python 3.10 or later. The complete student package uses only the Python
standard library and included local modules. No third-party pip packages,
internet access, external search library, or machine-learning framework are
required. Word or another DOCX reader is needed only
to edit laboratory sheets; the matching PDFs can be read without Word.

Begin with `Lab_00_Setup`. For new Windows x64 installations, it includes the
official Python 3.13.15 installer and a `requirements.txt` documenting every
module the lab code imports. Follow `Lab_00_Setup/README.md` for copyable
commands and `Lab_00_Setup/Setup_Guide.pdf` or `.md` for complete installation,
verification, first-run, and troubleshooting steps. Students who already have
Python 3.10+ may skip the installer. The requirements file has no third-party
package entries because all imports are standard-library or included modules.

Extract Information_Retrieval_Labs.zip before running code. Open PowerShell or a terminal
in the extracted Information_Retrieval_Labs folder. Run the commands below. If your
Windows installation provides the Python launcher, replace python with py -3.
Paths are anchored to each script, so an absolute path to a script also works from
another working directory.

## Weekly schedule and commands

| Week | Topic | Command from the package root |
|---|---|---|
| 01 | Python File Manipulation for Information Retrieval | `python "Week_01_File_Manipulation/lab01_file_manipulation.py"` |
| 02 | Regular Expressions for Text Processing | `python "Week_02_Regex_Text_Processing/lab02_regex.py"` |
| 03 | Text Preprocessing and Tokenization | `python "Week_03_Preprocessing/lab03_solution.py"` |
| 04 | Term-Document Incidence Matrix | `python "Week_04_Term_Document_Matrix/lab04_solution.py"` |
| 05 | Boolean Retrieval Using Binary Vectors | `python "Week_05_Boolean_Retrieval/lab05_solution.py"` |
| 06 | Inverted Index and Posting Lists | `python "Week_06_Inverted_Index/lab06_solution.py"` |
| 07 | Term Frequency Document Frequency and TF-IDF | `python "Week_07_TF_IDF/lab07_solution.py"` |
| 08 | Vector Space Model and Cosine Similarity | `python "Week_08_Vector_Space_Model/lab08_solution.py"` |
| 09 | Evaluation of Information Retrieval Systems | `python "Week_09_Retrieval_Evaluation/lab09_solution.py"` |
| 10 | Integrated Mini Search Engine | `python "Week_10_IR_Project/main.py"` |

Weeks 5, 6, and 10 accept --interactive after the script name. Type quit to exit.
Weeks 8 and 10 accept a quoted free-text query after the script name, for example:

```text
python "Week_08_Vector_Space_Model/lab08_solution.py" "python data analysis"
python "Week_10_IR_Project/main.py" --interactive
```

Weeks 5 and 6 support [NOT] term (AND [NOT] term)*. AND and NOT are case-insensitive
operator words. Terms use ASCII letters. OR, parentheses, and implicit AND are outside
the baseline grammar. Week 10 accepts free text; Boolean search is an optional exercise.

## Files in each week

Each week contains an editable A4 DOCX lab sheet, a matching PDF, a working Python
demonstration/solution, an exercise starter, data or docs, README.txt, and expected_output.txt.
Each sheet includes the required eleven teaching sections and the exact main Python listing.
Week 10 also prints every required module. Week 9 imports retrieval.py, an unchanged copy
of Week 8's full program; the Week 8 sheet contains that helper's complete listing.

Week 1 uses lab01_file_manipulation.py and exercises_lab01.py, and Week 2 uses
lab02_regex.py and exercises_lab02.py, preserving the specifically requested filenames.
Weeks 3-9 use labXX_solution.py and labXX_exercises.py. Week 10 uses main.py,
six supporting modules, and lab10_exercises.py. Starters run successfully and clearly
announce that their TODO functions are unfinished. They do not contain hidden solutions.

expected_output.txt is a captured default run, not data used by any program. Numerical
scores and metrics are always computed from the documents. A DOCX/PDF may show an excerpt
or wrap a long output line for readability.

## Preparing and maintaining the collection

Keep each docs directory beside its Python files. Files must be UTF-8 and use the lowercase
.txt suffix. The loader uses the filename without that suffix as its document ID. Only
ordinary .txt files are loaded; subdirectories and other extensions are skipped.

Week 1 creates three starter documents if absent, preserves existing document edits, and
resets data/notes.txt for its write/append demonstration. data/welcome.txt is a reading sample.
Week 2 includes the supplied sales paragraph and a separate pattern-practice file.
Weeks 3-5 retain the original five-document collection from the supplied Python files.
Weeks 6-10 use those same five documents plus five short original teaching documents about
databases, networks, information retrieval, data analysis, and search evaluation. Each later
week contains its own identical copy so that it can run independently.

Document IDs are doc1 through doc10. Lexicographic sorting places doc10 between doc1 and doc2;
all vectors, postings, rankings, and judgments use a consistent ID order. Do not compare
raw vector positions across a five-document and ten-document collection without their labels.

Weeks 3-9 use the five original fallback samples if docs is missing or empty, following
section-2.py. Shipped expected outputs for Weeks 6-9 assume the ten files exist. Week 10
deliberately reports a missing/empty docs collection rather than silently using fallback data.

When adding documents, keep IDs unique, rebuild the model, and review relevance judgments.
For experiments across weeks, copy the same edited collection to every compared week.

## Teaching continuity and source alignment

- Week 1 prepares students for the os-based loaders in both supplied scripts.
- Week 2 follows Regex-in-Python-A-Practical-Guide.pptx slides 2-11: raw strings,
  pattern symbols, findall, sub, extraction, cleaning, and the exact slide 11 paragraph.
- Week 3 retains re.findall(r"[a-z]+", text.lower()) and the supplied stop-word set.
- Weeks 4-5 retain the dictionary-of-binary-rows representation and Boolean operations in 5.py.
- Week 6 retains set-based posting construction, sorted postings, two-pointer intersection,
  and complement over all documents from section-2.py.
- Week 7 uses the Week 6 collection and raw TF with math.log(N / DF), without smoothing.
- Week 8 reuses Week 7 TF-IDF and implements cosine manually.
- Week 9 evaluates actual Week 8 rankings against explicit teaching judgments.
- Week 10 integrates the earlier functions into small modules.

Small corrections are explicit: loaders use UTF-8, stable ordering, .txt/file filtering,
script-relative paths, and consistent IDs. Boolean parsing uses word boundaries rather than
splitting inside words such as pandas. Unsupported syntax is rejected. The regex sheet clarifies
that raw strings are the recommended pattern notation, not the only possible notation; normal
escaped strings also work. Python's default string regex character classes are Unicode-aware,
while the required tokenizer deliberately selects ASCII letters. The simple email pattern
from the slides is labeled as an email-like extractor and its punctuation limitation is taught.

Supplied source files: Regex-in-Python-A-Practical-Guide.pptx, section-2.py, and 5.py.
They were inspected as teaching references; they are not runtime dependencies of this package.

Supplementary playlist supplied by the course owner:
[YouTube playlist](https://www.youtube.com/playlist?list=PLbAUSpKv_DMxFcTIM8Vnp9j7uC2l0R1mz).
Access was attempted on 25 September 2026, but fetching was throttled. Its video contents
were not inspected. No lab content is attributed to the playlist, and no topic alignment
is claimed. It remains an optional instructor-provided link; all labs work offline.

## Numerical and evaluation conventions

TF is the retained token count. DF counts distinct documents. IDF is the natural logarithm
of N/DF with no smoothing. Unknown terms have no coordinate; no division by zero is attempted.
Query vectors reuse document IDF. Zero-magnitude vectors receive cosine 0.0. Equal scores
sort by document ID. Week 8 displays every document; Weeks 9-10 retain positive-score results
for their reported retrieval output.

Relevance judgments in data/relevance.json are explicit teaching assumptions tied to the listed
query intents. They are not inferred from the scores. Both methods in Week 9 use identical
queries, relevance sets, and k=3. Precision/recall/F1 use the available top-three unique IDs.
P@k always divides by k; a short list has nonrelevant unfilled positions. Recall@k divides
by the full relevance-set size. Empty-denominator metrics report 0.0 by convention. Nonpositive
k raises ValueError. Deduplication keeps the first ranked occurrence of each ID.

The mini engine checks that judged IDs exist. A changed document may still invalidate a judgment
semantically, so instructors should review judgment content after collection edits. Unjudged
queries can be searched without evaluation. Results support conclusions about these queries
and this collection only.

## Duration and assessment suggestion

Suggested two-hour structure: 15 minutes concept review, 25 demonstration, 50 guided
implementation, 20 selected exercises, and 10 review. Choose two or three exercises during
class and complete remaining exercises afterward. Challenges are optional extensions.
Week 10 assumes reuse of prior functions, so the session focuses on integration and checking.

Suggested course-lab assessment: 45% weekly implementations, 15% test evidence and hand
calculations, 10% practical participation/review, and 30% final mini project. Suggested project
rubric: 40% working pipeline, 25% correct ranking/evaluation, 20% code clarity and reproducibility,
and 15% explanation of results and limitations. Adjust weights to institutional policy.

For each lab, submit the completed exercise code, required data, output evidence, and the
specific written answers listed in section 9. Instructor solutions are supplied for demonstration
and checking; students should develop and explain their own implementations.

## Validation records

Validation_Report.md records execution, mathematical checks, document/PDF checks, and a
per-week deliverable table. Directory_Tree.txt lists the final package files. All .py files,
including starters and helper modules, were run; starter completion is intentionally left
to students. PDFs were exported from the corresponding DOCX files so their substantive
content is identical.
