# Prom Motion Skill

A portable skill for coherent video work in Claude Code, Codex or another assistant that can read local Markdown. It covers evidence-backed story planning, complete-sentence editing, motivated transitions, multilingual subtitles, free local editing and technical handover.

The skill works with your chosen editor. It does not include a render engine, paid model access, footage, fonts or application dependencies. It does not automatically upload, spend or publish anything.

## Install or use directly

Keep this `prom-motion` folder together. Copy it into your assistant's configured skill directory. Common locations are `~/.claude/skills/prom-motion/` for Claude Code and `~/.codex/skills/prom-motion/` for Codex. You can also ask the assistant to read `SKILL.md` directly without installing it.

Example prompt:

> Use Prom Motion Skill. Read my current brief and inspect the supplied media inventory. Build a coherent paper edit with source IDs, exact timecodes and a reason for each transition. Keep gaps and unreviewed footage explicit. Do not render or generate yet.

For a local proof:

> Use Prom Motion Skill's free local workflow. Reuse the existing research and source IDs. Show a short beat list, then build a representative proof using selected footage and local tools. Give me a playable MP4, editable shot and caption data, a restartable preview and the exact rerender command. Explain the steps briefly. Do not buy services or upload client media.

Read [free local workflow](references/free-local-workflow.md) for the FFmpeg and SV Motion/HyperFrames route. This adds no mandatory editor purchase. Existing agent usage, optional services and final delivery requirements remain separate.

For a revision:

> Use Prom Motion Skill to fix this opening. Preserve the approved body and ending. Listen to the selected sentence in context, propose the smallest repair, then check that the closing thought and retained timings remain intact.

For finishing:

> Use Prom Motion Skill to check my agreed delivery matrix, caption cue data and final export. Report what was verified, what remains unreviewed and the exact files to hand over.

## Contents

`SKILL.md` routes to five focused workflows. `references/` holds detailed methods. `assets/` provides fictional JSON examples for a paper edit and multilingual cue data. The examples are not real source evidence or approved translations.

The instructions were distilled from documented editing lessons. They are intended to help an editor reason through the current film, not reproduce an old project's visual style or settings. Verify current provider schemas, tool flags, asset licences and approvals when using external tools.

## Keeping a copy current

Update this whole skill folder together so its relative references stay valid. An installed symlink follows its checkout; a copied skill or handover ZIP stays at the version it contained until you replace it. Preserve any local customizations before updating.

## Licence

The original text and templates in this package are licensed under MIT. This does not grant rights to any footage, music, fonts, models, applications or third-party skills used alongside it.
