# Lab 0: Python and Course Setup Guide

Information Retrieval Practical Laboratories — Windows classroom setup

## What you need

- A Windows 10 or 11 computer with a 64-bit Intel or AMD processor. The included
  installer is for **Windows x64**. If your computer uses Windows on ARM, macOS,
  or Linux, obtain the appropriate Python installer from
  <https://www.python.org/downloads/> instead.
- Python **3.10 or later**. This package includes the official **Python 3.13.15**
  Windows x64 installer: `python-3.13.15-amd64.exe`.
- Enough free space to extract the course ZIP and install Python. Keep the entire
  `Information_Retrieval_Labs` folder together.
- PowerShell, Windows Terminal, or Command Prompt. A code editor is useful but
  optional. A PDF reader is useful for the lab sheets.

The course uses Python's **standard library and included local modules only**.
`Lab_00_Setup/requirements.txt` lists every module imported by the lab code;
it has no third-party package entries. No online account, API key, database
server, or paid software is needed. The labs work offline after setup.

## 1. Extract the course package

Right-click `Information_Retrieval_Labs.zip` and choose **Extract All**. Work in
the extracted folder. Do not run the laboratory scripts directly inside the ZIP.
Its `docs` and `data` folders must stay beside the corresponding scripts.

## 2. Install Python (skip if Python 3.10+ already works)

1. Check **Settings > System > About > System type**. Continue with the included
   installer if it says **64-bit operating system, x64-based processor**.
2. From the extracted course root, run this PowerShell command to open the
   included installer (or double-click the file in `Lab_00_Setup`):

   ```powershell
   .\Lab_00_Setup\python-3.13.15-amd64.exe
   ```
3. On the first installer screen, select **Add python.exe to PATH** if shown.
   Choose **Install Now**. The default installation includes `pip`, the standard
   library, and the Python launcher. You do not need to select optional
   free-threaded binaries or debug symbols for this course.
4. Finish the installer and open a **new** PowerShell or terminal window so it
   sees the updated command path.

If Python 3.10 or later is already installed, you may use that installation.
Installing this exact version is not required for the course.

## 3. Confirm your installation

In a new PowerShell window, run:

```powershell
py -3.13 --version
py -3.13 -c "import re, os, math, json; print('Course Python ready')"
```

The first command should print `Python 3.13.15` for the included installer;
the second should print `Course Python ready`. If you kept an existing Python
3.10+ installation, replace `py -3.13` with `py -3`, `python`, or `python3`
as appropriate. Check that `python --version` reports at least Python 3.10.

## 4. Install and check course requirements

From the extracted course root, run:

```powershell
py -3.13 -m pip install --no-index -r .\Lab_00_Setup\requirements.txt
py -3.13 -c "import json, math, os, re, sys; print('Course requirements ready')"
```

The requirements file documents all lab imports: `json`, `math`, `os`, `re`,
and `sys` are included with Python; `evaluation`, `file_utils`, `indexing`,
`preprocessing`, `ranking`, `retrieval`, and `tfidf` are local modules supplied
in the week folders. **There is nothing additional to download or install with
pip.** The `--no-index` option makes that check work offline. If you use an
existing Python 3.10+ installation, replace `py -3.13` with your Python command.

## 5. Run the first lab

Open PowerShell in the extracted `Information_Retrieval_Labs` folder. One way is
to open that folder in File Explorer, click its address bar, type `powershell`,
and press Enter. Then run:

```powershell
py -3.13 .\Week_01_File_Manipulation\lab01_file_manipulation.py
py -3.13 .\Week_02_Regex_Text_Processing\lab02_regex.py
```

Compare each result with the `expected_output.txt` file in that week's folder.
The Week 1 program creates sample files inside its own `data` folder. For all
ten weekly commands, see `Course_README.md` at the course package root.

To try the final search engine after working through the course:

```powershell
py -3.13 .\Week_10_IR_Project\main.py
py -3.13 .\Week_10_IR_Project\main.py --interactive
```

In interactive mode, type `quit` to exit. Every program finds its own data
relative to the script file, so keep each week's files together.

## Common problems

| Symptom | What to do |
|---|---|
| `py` is not recognized | Close and reopen PowerShell. Try `python --version`. If that also fails, rerun the included installer and enable **Add python.exe to PATH**. |
| `python` opens the Microsoft Store | Use `py -3.13` for the course commands, or disable the Python app execution aliases in Windows Settings. |
| `No such file or directory` or a missing `docs` folder | Extract the ZIP completely, open a terminal at the extracted package root, and keep each week's `docs` or `data` directory next to its scripts. |
| The included installer will not run on the computer | Check **System type**. This file is Windows x64 only; choose the matching installer at <https://www.python.org/downloads/>. |
| A lab reports a Python error | Confirm `py -3.13 --version` (or your chosen Python command) first, then use the exact weekly command in `Course_README.md`. |

## Installer provenance and optional checksum check

Included file: `python-3.13.15-amd64.exe` (29,452,944 bytes)

Official release: <https://www.python.org/downloads/release/python-31315/>

Official direct download: <https://www.python.org/ftp/python/3.13.15/python-3.13.15-amd64.exe>

SHA-256 published by Python.org and verified for the included file:

```text
EDEC09C4853AEAE9AC36EFB8C9F95B6B8E2FEE65EEE56D9767A8B7C69C574403
```

To check your copy from the `Information_Retrieval_Labs` folder:

```powershell
(Get-FileHash .\Lab_00_Setup\python-3.13.15-amd64.exe -Algorithm SHA256).Hash
```

The displayed hash should equal the one above. The included executable also
has a valid Windows digital signature from the Python Software Foundation.

Python's Windows installation documentation:
<https://docs.python.org/3.13/using/windows.html>
