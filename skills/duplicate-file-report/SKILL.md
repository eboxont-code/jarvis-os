---
name: duplicate-file-report
description: Report byte-identical files in a folder the user names. Read-only. Do not delete or move anything.
---

Use this when the user asks about duplicate files. Confirm the folder is visible to the file tool. Inspect immediate children unless the user asked for subfolders. Skip symlinks, reparse points, and offline files. Apply the same skips before entering a directory on a recursive request. Report skipped items as incomplete coverage.

Group regular files by byte length. Inside each group of two or more, hash with `Get-FileHash -LiteralPath -Algorithm SHA256`. Report groups that share a hash. Include relative names, byte length, and the hash. Sum `(count - 1) * length` per group as logical duplicate bytes. Recoverable disk space can differ for hard links and compressed files. Report read errors and files whose size or modification time changed during the hash. Leave every file in place.
