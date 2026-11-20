---
name: duplicate-file-report
description: Report byte-identical files in a folder the user names. Read-only. Do not delete or move anything.
---

This PC is Windows 11 Pro, an Intel Core i9-14900F (24 cores, 32 threads), 64 GB DDR5-5600, and an RTX 4070 with 12 GB (driver 610.60). About 1.5 TB is free on the fast NVMe. Hash on the CPU. Do not start Ollama, ComfyUI, or whisper for this report.

Use this when the user asks about duplicate files. Confirm the folder is visible to the file tool. Inspect immediate children unless the user asked for subfolders. Skip symlinks, reparse points, and offline files. Apply the same skips before entering a directory on a recursive request. Report skipped items as incomplete coverage.

Group regular files by byte length. Inside each group of two or more, hash with `Get-FileHash -LiteralPath -Algorithm SHA256`. Report groups that share a hash. Include relative names, byte length, and the hash. Sum `(count - 1) * length` per group as logical duplicate bytes. Recoverable disk space can differ for hard links and compressed files. Report read errors and files whose size or modification time changed during the hash. Leave every file in place.
