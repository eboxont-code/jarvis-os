---
name: duplicate-file-report
description: Find byte-identical file candidates within a folder the user selects and produce a read-only duplicate and space report.
---

Use when the user asks about duplicate files or storage cleanup. Confirm the selected folder is accessible through the authorised file tool. Use the user's exact folder, respect tool permissions and inspect just its immediate files unless the user specifies subfolders. Skip symlinks, reparse points and offline files. For a recursive request apply the same exclusions before entering each directory. Report skipped or inaccessible items as incomplete coverage.

Group regular files by byte length first. Within each group containing two or more files, compute SHA-256 using Get-FileHash -LiteralPath. Group the results by hash within the size group. Report only groups containing at least two files, with relative filenames, byte length and matching hash. Sum (count minus one) times byte length per group as the logical duplicate bytes. Actual recoverable disk space may differ for hard links or compressed files. Report read errors and files whose size or modification time changed during hashing. Keep all files in place.
