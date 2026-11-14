# CLAUDE.md — System instructions for Claude Code (docs routines)

This file is loaded as system context for every Claude Code session in this
repository, including sessions started by Routines. Part 1 is the source
content, kept verbatim. Part 2 turns each item of Part 1 into directives that
Claude must execute. Part 3 records lessons learned from earlier sessions and
from how the repo owner works; it overrides Part 2 where they conflict.

## Part 1 — Source content (verbatim, do not edit)

```text
Challenges with proactive agents
Where to run

* Hosting, data persistence, and authentication; everything outside my prompt.

When to run

* No clean way to start an agent because a PR opened or an alert fired.

How to partner

* Headless means invisible; no way to watch, steer, or bound it.

Routines: define the prompt, repo, connectors, and triggers; Claude Code handles the rest.
Always available with managed infrastructure

* Routines run on Claude Code's cloud with hosting, session state, and connector auth handled; nothing depends on my laptop being open.

Work proactively with customizable triggers

* Kick off on a schedule, from any HTTP call, or on GitHub events - with the event payload loaded as context.

Interactive and steerable agent teammates

* Every run is Claude Code session I can open, watch, follow up on, and pause from the web, CLI, and desktop.

Three decisions for any routine:
The trigger: when does it run?
Schedule-based

* Weekly review of GitHub issues that mention docs.

Release-based

* When a release is cut, diff the release branch against the docs for new features and behavior changes.

Label-based

* Let engineers proactively tag PRs that need documentation.

The context: what does it need to know?
Codebase repositories

* Dive into the source to understand flags, defaults, and usage instructions.

Connectors

* Attach to relevant tools and data sources.

Marketing briefs

* Understand how we talk about the feature so the docs sound like us.

Steerability: how do we ensure quality?
Agent-on-agent review

* Routines can review another before a human looks.

Human in the loop, not at the keyboard

* Open the live session from web or CLI, ask what it's doing, change the plan mid-run.

Verification

* Run the thing; execute the Claude Code CLI, render the page, check the output matches the doc.
```

## Part 2 — Executable directives

### 2.1 Where / when / how to run (from "Challenges with proactive agents")

- **Where to run:** Run as a Claude Code Routine on Claude Code's cloud. Do not
  depend on any local machine. Keep all state in the repository (branches,
  commits, PRs, issue comments), never in local files outside it.
- **When to run:** Start only from a configured trigger (schedule, HTTP call,
  or GitHub event). When started by an event, read the event payload first
  and treat it as the task input.
- **How to partner:** Never work invisibly. At the start of each run, state the
  trigger, the plan, and the files you expect to touch. Keep progress visible in
  the session so a human can open, watch, follow up, steer, or pause it.

### 2.2 Routine definition (prompt, repo, connectors, triggers)

| Field      | Value                                                        |
|------------|--------------------------------------------------------------|
| Repo       | `mito2404/graphify-demo`                                     |
| Connectors | GitHub (required); add other tools/data sources when needed  |
| Docs       | `README.md` and any `docs/` directory                        |
| Source     | `demo.py` and any other source files in the repo             |
| Output     | A draft PR with doc changes, or an issue comment if no change |

### 2.3 The trigger: when does it run?

1. **Schedule-based — weekly docs issue review**
   - Trigger: once a week.
   - Do: list open GitHub issues whose title or body mentions `docs`,
     `documentation` or `README`. For each, decide: already documented /
     needs a doc change / not a docs issue. Make the needed doc changes on one
     branch and open one draft PR that links every issue it addresses. Post a
     short summary comment on each reviewed issue.

2. **Release-based — release diff against docs**
   - Trigger: GitHub event `release` (published) or a new release branch/tag.
   - Do: diff the release branch/tag against the previous release. List every
     new feature, changed flag, changed default and changed behavior. Check
     each one against the docs. Update the docs for anything missing or wrong
     and open a draft PR titled `docs: update for <release>`.

3. **Label-based — PRs tagged as needing documentation**
   - Trigger: GitHub event `pull_request` labeled `needs-docs`.
   - Do: read the PR diff and description, write the documentation for the
     change, and push it as a follow-up draft PR (or a commit on the PR branch
     only if its author asked for that). Comment on the original PR with a
     link. Remove nothing and change no code outside the docs.

### 2.4 The context: what does it need to know?

- **Codebase repositories:** Read the source before writing docs. Take flags,
  defaults, function signatures and usage instructions from the code, not from
  memory or the existing docs.
- **Connectors:** Use the attached connectors (GitHub first) to read issues,
  PRs, releases and any other attached tools and data sources.
- **Marketing briefs:** If a marketing brief or style guide exists in the repo
  (for example `docs/brief.md` or `docs/style.md`), read it first and match
  its terminology and tone so the docs sound like us. If none exists, keep the
  tone of the current `README.md`.

### 2.5 Steerability: how do we ensure quality?

- **Agent-on-agent review:** Before requesting human review, have a second
  routine/agent review the doc PR for accuracy against the source, broken
  examples and tone. Address its findings, then mark the PR ready for a human.
- **Human in the loop, not at the keyboard:** Keep the run interruptible.
  When a human asks what you are doing, answer with the current step and plan.
  When they change the plan mid-run, follow the new plan.
- **Verification:** Run the thing before finishing:
  - execute every command and code example the docs show (for this repo:
    `python demo.py` and check that its output matches the doc);
  - when docs mention the Claude Code CLI, execute it and compare output;
  - render changed Markdown/pages and check they display correctly;
  - if any output does not match the doc, fix the doc (or report the mismatch)
    before opening the PR. Report results faithfully in the PR description.

## Part 3 — Lessons learned (from session memory and owner behavior)

Evidence: session `session_01PdD9ibbX7RKHZFUunzEsb7` (2026-11-13), routine
state from `list_triggers` and PR list on 2026-11-14. Items marked
*(unverified)* were never confirmed; do not state them as fact.

### 3.1 How the owner works — do this

- **Language and tone:** reply in Vietnamese by default, short and direct. The
  owner writes short imperative requests ("... giúp mình"); act on them without
  extra confirmation unless the decision is genuinely theirs.
- **Truthfulness:** never invent information or fill gaps; label anything
  unverified; cite the direct source (tool result, file path, PR, session).
  Review the answer before sending.
- **Verbatim means verbatim:** when the owner says to keep source content as is
  ("giữ nguyên gốc nội dung"), keep it byte-identical in its own section, put
  the executable interpretation in a separate section, and confirm with `diff`.
- **Set up → test-run → report:** after creating or changing anything
  (routine, label, config, docs), the owner always asks to run it and check the
  result. Do it proactively: run once, read the result, and report a table of
  check item / ✅ or ❌ / detail, plus duration and cost when known.
- **Verify the owner's "done":** when the owner says they fixed something in a
  UI ("mình đã gắn/sửa/bật xong"), check the real state with tools before acting.
  On 2026-11-13 09:39 the owner said the repo was attached but all three
  routines still had an empty repo list; Claude reported that instead of running
  a test that would fail.
- **Offer a concrete workaround when a tool cannot do something**, and let the
  owner pick (the owner chose "create a temporary issue" to create a label).
- **Protect cost and noise:** if something will fail repeatedly (scheduled runs,
  notifications), say so and offer to pause it. The owner asked to pause all
  three routines until the repo was attached.
- **Outward actions only on explicit request in the current turn:** merge,
  enable/disable/fire a routine, create issues or labels. A PR is merged only
  when the owner asks (PR #1 was merged on request; PR #3 was not).
- **Clean up after yourself:** once a test result is read, delete the now
  redundant `send_later` check-in; stop PR check-ins when nothing is left to do.
- **Portability:** the owner also uses ChatGPT/Codex. `AGENTS.md` mirrors this
  file for Codex (draft PR #3, not merged as of 2026-11-14). When this file
  changes, say whether `AGENTS.md` needs the same change.

### 3.2 Platform facts learned — rely on these

- A routine created with `create_trigger` has **no repository and no
  connectors**. Its run fails with HTTP 403 "GitHub access to this repository is
  not enabled for this session". Fix: the owner opens claude.ai/code → Routines,
  adds `mito2404/graphify-demo` with write access, and saves. After creating any
  routine, fire one test run to confirm repo access before relying on it.
- `create_trigger` cannot create GitHub-event triggers. The release and
  `needs-docs` routines therefore poll daily and de-duplicate by PR title
  (`docs: update for <tag>`, `docs: document #N`); latency is up to about a day.
- `list_triggers` did not show the two routines the owner created in the UI on
  2026-11-13; the cause is *(unverified)*.
- The GitHub MCP tools here cannot create or edit labels. Workaround used:
  create a temporary issue carrying the label (this creates the label), then
  close the issue. The owner set the `needs-docs` description and color in the UI.
- A test run of each routine took about 15–20 s and cost about 0.27–0.29 USD
  (2026-11-13).

Routine state on 2026-11-14 (all enabled, last run succeeded):

| Routine | Schedule (Asia/Ho_Chi_Minh) |
|---|---|
| Weekly docs issue review | Monday 08:38 |
| Daily release docs check | Daily 09:38 |
| Daily needs-docs PR check | Daily 13:39 |

### 3.3 Open decisions — ask the owner, do not act alone

- **First release:** the release routine diffs against the previous tag; the
  repo has no tags yet. Proposal (awaiting the owner): diff the first release
  against the repository's first commit.
- **PR #3 (`AGENTS.md`):** draft, awaiting the owner's merge decision.
- **Weekly routine prompt** still mentions branch `claude/fervent-goldberg-snfjt3`
  as a fallback for `CLAUDE.md`; that work is merged into `main`. Harmless while
  the branch exists; propose removing the reference when the routine is next edited.
