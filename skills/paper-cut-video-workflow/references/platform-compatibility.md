# Platform Compatibility

Keep `SKILL.md`, `references/`, `assets/`, and `scripts/` together. Do not copy only the entry file because the workflow resolves supporting resources relative to the Skill directory.

## Codex

Install the complete folder at either project scope or user scope using the Skill directory supported by the active Codex environment. The canonical project layout is:

```text
.agents/skills/paper-cut-video-workflow/
```

Invoke by name or with a request matching the description.

## Claude Code

Install the complete folder at:

```text
.claude/skills/paper-cut-video-workflow/
```

Invoke with `/paper-cut-video-workflow` or a matching natural-language request.

## Trae

Install the complete folder at:

```text
.trae/skills/paper-cut-video-workflow/
```

Invoke by naming the Skill or asking for the complete paper-cut video workflow.

## Cursor

Keep the complete folder at:

```text
.cursor/skills/paper-cut-video-workflow/
```

Then copy `adapters/cursor/paper-cut-video-workflow.mdc` to:

```text
.cursor/rules/paper-cut-video-workflow.mdc
```

The rule is agent-requested and loads the canonical Skill only when the task matches.

## Generic File-Based Agents

Keep the complete folder at `skills/paper-cut-video-workflow/`. Copy `adapters/generic/AGENTS.md` to the project root, or merge its section into an existing root `AGENTS.md`.

## Degradation Rules

- If an agent cannot auto-discover Skills, explicitly ask it to read `SKILL.md` before acting.
- If the agent cannot execute Python, calculate durations manually using the same fields and formulas described by the script interface.
- If image, TTS, HyperFrames, or FFmpeg tools are unavailable, produce exact prompts, layer plans, timing sheets, and command-ready specifications without claiming media was generated.
- Never silently replace unavailable production steps with invented output.
