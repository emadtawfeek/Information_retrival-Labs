# Lab 0 - Python and Course Requirements

This folder contains the official Python 3.13.15 Windows x64 installer,
`requirements.txt`, and the full [setup guide](Setup_Guide.pdf)
([Markdown version](Setup_Guide.md)). Python 3.10 or later is sufficient.
The requirements file also links to the official Python 3.13.15 release,
Windows installer, and CPython source-code archive.

From the extracted course root in PowerShell, install Python if needed:

```powershell
.\Lab_00_Setup\python-3.13.15-amd64.exe
```

In the installer, select **Add python.exe to PATH** if shown and choose
**Install Now**. Open a new PowerShell window, return to the course root, and run:

```powershell
py -3.13 --version
py -3.13 -m pip install --no-index -r .\Lab_00_Setup\requirements.txt
py -3.13 -c "import json, math, os, re, sys; print('Course requirements ready')"
py -3.13 .\Week_01_File_Manipulation\lab01_file_manipulation.py
```

The requirements file lists **all modules imported by the lab code**. Five
are Python standard-library modules (`json`, `math`, `os`, `re`, `sys`); seven
are local modules included in the week folders. There are no external packages
for pip to download. The `--no-index` option confirms setup works offline.

If you already have Python 3.10 or later, skip the installer and replace
`py -3.13` in these commands with your working Python command, such as `py -3`.
