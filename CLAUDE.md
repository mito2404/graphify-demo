# CLAUDE.md — System instructions for Claude Code (docs routines)

This file is loaded as system context for every Claude Code session in this
repository, including sessions started by Routines. Part 1 is the source
content, kept verbatim. Part 2 turns each item of Part 1 into directives that
Claude must execute.

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
