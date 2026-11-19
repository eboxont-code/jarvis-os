---
name: mail-in-chat
description: Start or resume Gmail, Outlook and iCloud Mail setup from native OpenClaw Chat using the existing browser tool. Use when asked to connect or open mail or calendars.
---

Take the actions from the current conversation. In the main session's Dashboard, reuse the saved browser widgets `workspace-mail-gmail`, `workspace-mail-outlook` and `workspace-mail-icloud`. These are live Agent browser pages within the OpenClaw Control UI. To create one in another session, use the dashboard tool with action `widget_put`, the corresponding name, provider title, pluginKind `browser:dashboard`, props containing the official URL below, and size `full`. Offer to show the Browser side panel for a temporary view. Use the browser tool's `dashboard` selector to address the same widget after sign-in. Avoid sending the operator to a separate mail client.

| Provider | Mail | Calendar |
|---|---|---|
| Google | https://mail.google.com/ | https://calendar.google.com/ |
| Microsoft personal | https://outlook.live.com/mail/ | https://outlook.live.com/calendar/ |
| Apple | https://www.icloud.com/mail/ | https://www.icloud.com/calendar/ |

Open the requested service, then report which provider page or sign-in screen actually opened. The operator completes passwords, passkeys, two-factor checks and consent privately on the provider page. Do not inspect or capture the page while credentials are being entered. When the operator returns to chat, verify access in the same profile with the smallest non-sensitive check and continue their requested task. A link opening in a different browser does not authorise the OpenClaw session. A browser session and the IMAP watcher require separate verification. If visible handoff fails, say what failed and keep account status unverified. Never enable a sender, send or delete mail as part of setup.
