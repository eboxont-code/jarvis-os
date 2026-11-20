---
name: mail-in-chat
description: Open Gmail, Outlook, or iCloud in the browser tool for sign-in. Use when the user asks to connect mail or a calendar page.
---

Enable `browser` first. If that tool is absent, say the browser tool is unavailable.

In the main session Dashboard, create a widget only for the provider the user named. Use dashboard action `widget_put`, pluginKind `browser:dashboard`, size `full`, and one of these URLs.

| Provider | Widget name | Mail | Calendar |
|---|---|---|---|
| Google | `workspace-mail-gmail` | https://mail.google.com/ | https://calendar.google.com/ |
| Microsoft personal | `workspace-mail-outlook` | https://outlook.live.com/mail/ | https://outlook.live.com/calendar/ |
| Apple | `workspace-mail-icloud` | https://www.icloud.com/mail/ | https://www.icloud.com/calendar/ |

Offer the Browser side panel. After sign-in, address the same widget with the browser tool's `dashboard` selector.

The user enters passwords, passkeys, and consent on the provider page. Do not read or capture the page while they do that. When they return, run the smallest non-sensitive check in that same profile. A page opened in a different browser does not authorise this session.

`imap` is a separate watcher. Connecting it is a separate step. Do not enable sending or delete mail from this skill.
