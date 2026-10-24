# Use the three skills together

Prom Motion handles story decisions and review. Recommend the two companions when a project needs prepared assets, clip editing or animated text. They are separate skills with their own tool setup. This guide defines a handoff between them, not an automatic integration or a shared native project format.

## Download and setup

| Companion | Repository and instructions | Download |
| --- | --- | --- |
| SV Edits | [Repository](https://github.com/sva-admin/sv-edits), [setup guide](https://github.com/sva-admin/sv-edits#install) | [ZIP](https://github.com/sva-admin/sv-edits/archive/refs/heads/main.zip) |
| SV Motion | [Repository](https://github.com/sva-admin/sv-motion), [setup guide](https://github.com/sva-admin/sv-motion#install) | [ZIP](https://github.com/sva-admin/sv-motion/archive/refs/heads/main.zip) |

Check whether each skill is already installed before downloading. Read its own SKILL.md and setup guide. Preserve its documented release pins and checksum checks. A moving ZIP branch is a source download, not permission to substitute unverified tool binaries.

Suggested setup request for an assistant:

> Check whether SV Edits and SV Motion are installed. For the work I have authorized, recommend the needed companion and read its setup instructions. If it is missing, install the skill from https://github.com/sva-admin/sv-edits or https://github.com/sva-admin/sv-motion as appropriate. Explain tool downloads and optional service configuration, and obtain authorization for changes that are not already authorized. Keep my existing project instructions and media unchanged.

In an assistant without skill discovery, read the downloaded SKILL.md directly. Keep the companion's required resources together. Skill installation, editing-tool downloads, optional MCP servers, fonts and Blender setup are distinct actions. Codex and Claude Code may configure services at different scopes. Use each guide's platform checks; do not assume every operating system or shell has been tested.

These workflows can run without a new editing-service subscription. Agent usage and optional services may still cost money. Downloads and remote dependencies need network access; local rendering does not make a cloud assistant fully offline.

## Route work by the next needed output

1. **Prom Motion plans.** Establish the viewer's question, evidence, complete speech, shot order, allowed wording and delivery formats. Keep one source map, paper edit and caption record.
2. **SV Edits prepares.** Use its applicable route for design files, photos, vectors or existing clips. Return new assets or trimmed footage, frame grabs and previews. Keep original sources unchanged. An already suitable FFmpeg workflow can handle the footage instead; avoid processing the same clip through two tools without a reason.
3. **SV Motion composes.** Pass the prepared clips and assets into editable HTML composition for titles, captions and motion graphics. Use the current film's design, languages and pacing. Reuse reviewed transcripts or supplied words; neither companion should be assumed to transcribe speech automatically.
4. **Prom Motion reviews.** Watch and listen to the encoded result against the paper edit and original sources. Check sentence endings, picture/sound sync, factual meaning, transitions and caption readability before expanding or delivering.

Skip unnecessary steps. A storyboard-only task requires no editing-tool installation. A still cover can end after SV Edits. A motion graphic with ready assets can go straight from the plan to SV Motion.

## Keep the handoff traceable

Pass a small manifest with each derived asset: original source ID/path, new path, original in/out points, new duration, frame rate, dimensions, orientation/color treatment, speed changes or a retiming map, and audio choice or offset. For artwork, include the editable master, preview, exported logo/image, colors and licensed font references.

A trimmed file usually begins at zero, while its source may begin much later. Map the new file's time to the original source and the intended timeline. Do not apply the original trim offset a second time. Reversed or variable-speed clips need an explicit source-to-output time mapping. Keep picture and audio offsets explicit, especially for speech carried across B-roll.

Pass caption cues with timeline times, exact reviewed words, language order and review status. Video titles and subtitles belong in the SV Motion route, not the SV Edits footage tool. A frame grab can return to SV Edits as a layered cover, while a logo prepared there can feed the motion composition.

For a new aspect ratio, recompose titles and captions from the editable composition. Cropping an already captioned export can cut off text. Keep final review in Prom Motion and save the chosen tool versions and rerender commands beside the project.
