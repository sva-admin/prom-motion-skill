# Prom Motion Skill

A portable video editing skill for Claude Code and Codex. It teaches story planning from source evidence, complete-sentence cuts, motivated transitions, multilingual captions, free local editing with FFmpeg and SV Motion/HyperFrames, and reproducible finishing.

The package contains original instructions and fictional examples. It contains no client files, credentials, footage, paid model access or copied third-party skill code.

## Plugin or standalone skill

This repository now includes a Claude Code plugin manifest and a local marketplace. The same skill folder still works as a standalone skill in Claude Code or Codex. No services, hooks or media files run automatically.

For local testing, from this folder:

```bash
claude plugin validate . --strict
claude --plugin-dir .
```

Then invoke `/prom-motion:prom-motion` in Claude Code. Read [Quickstart](QUICKSTART.md) for the marketplace installation commands, planning prompts, a small proof and revision checks. If you have an older standalone checkout, update it first so it contains `.claude-plugin/plugin.json`.

Claude Code 2.1.275 or later also supports:

```text
/plugin install prom-motion --marketplace sva-admin/prom-motion-skill
```

## Standalone use

Download this repository or clone it:

```bash
git clone https://github.com/sva-admin/prom-motion-skill.git
```

Read [the skill](skills/prom-motion/SKILL.md), or copy the complete `skills/prom-motion` folder into your configured skills directory, such as `~/.claude/skills/` or `~/.codex/skills/`. Keep its references and assets together. Public downloads do not require a GitHub account or token.

Example prompt:

> Use Prom Motion Skill. Read my current brief and media inventory. Build a paper edit with source IDs, exact timecodes and a reason for each transition. Keep gaps explicit. Do not render or generate yet.

For an authorized local proof:

> Use Prom Motion Skill's free local workflow. Reuse my existing brief, transcripts and source map. Show the beat list, then make a short playable proof from selected footage without new production spending. Deliver the MP4, editable shot/caption data, local preview and rerender command. Keep original media unchanged.

Read [the free local workflow](skills/prom-motion/references/free-local-workflow.md) for tool checks, selective proxies, browser captions, sound and section-based rendering. Local rendering has no per-render service fee; coding-agent usage and optional assets or services may still cost money. Respect an explicit editor choice or planning-only request.

The skill works with your chosen editor. It does not install applications or grant permission to upload, spend or publish. Read [usage examples and package details](skills/prom-motion/README.md).

## Update

For a marketplace installation, run these commands in your terminal, then restart Claude Code:

```bash
claude plugin marketplace update prom-motion-marketplace
claude plugin update prom-motion@prom-motion-marketplace
```

If you use a Git clone, pull the latest permitted branch and update the installed `skills/prom-motion` folder from that checkout. A copy inside an older handover archive is a snapshot and does not update automatically.

## License

MIT for the original instructions and templates. Rights to footage, music, fonts, tools and third-party material remain separate.

## Package locally

Run `python3 scripts/package.py` to create the ZIP in `dist/`. It packages only the plugin manifests, skill, documentation and packaging script. It does not upload or publish the result.
