# AI Agents

Prompts for every active Complete360 AI agent in GoHighLevel (Complete360 sub-account).
**This folder is the source of truth.** Change a prompt here first, then paste it into
GHL (AI Agents → Voice AI → the agent → prompt field), or ask Claude to push it.

Each file has the agent's GHL ID, where it runs, its knowledge base and actions, the
welcome message, any open items, and the full prompt inside a ```` ```text ```` block
ready to copy.

| File | Agent | Runs on | Last changed |
|---|---|---|---|
| `dakota-website-chat.md` | Dakota | Website chat widget (voice) | 2026-11-09 |
| `riley-ai-agents-page.md` | Riley (EN) | /ai-agents demo widget | 2026-11-09 |
| `riley-ai-agents-page-es.md` | Riley (ES) | /ai-agents Spanish widget | 2026-11-09 |
| `jessica-onboarding-line.md` | Jessica | Onboarding line (520) 492-0951 | 2026-09-21 |
| `jessica-backup-reception.md` | Jessica | Backup line (520) 556-7400 | 2026-09-21 |
| `sarah-voice-drop-callback.md` | Sarah | Voice-drop callbacks | — |

## Not in this folder
- **Website text chat (Conversation AI):** the text replies in the website chat widget
  come from Conversation AI, which the GHL API connection can't read. Paste its prompt
  here as `website-chat-text.md` so it's tracked too.
- **Inactive agents:** "Gabriel AI Asst. (DO NOT USE)" and "Luis AI Asst. (DO NOT USE)".
  Consider deleting them in GHL — the Gabriel one has an action that tells callers
  their cancellation has been processed.

## Policy every agent must match
Taken from the Terms of Service and Return Policy (v2.1). If the policy changes,
update the agents that state it (Dakota, Riley EN/ES).
- Non-refundable from the time of purchase; exceptions case by case, by management only.
- Recurring services: cancel at least 10 days before the next billing date, in writing.
- Satisfaction guarantee: GBP Management and all ad campaigns — campaign extended at no charge if eligible.
- Billing, refunds and cancellations: customer service (800) 863-2541. Sales: (866) 527-6205.

## Knowledge base
Dakota, both Jessicas and Sarah share knowledge base `9xrTMivBdEHfIIRhf0GM`, trained
from the live site on 2026-07-25. Retrain the pages you change after pasting them into GHL.
