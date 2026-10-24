# From footage to a coherent edit

## Load the local plugin

Clone the public repository and enter its folder:

```bash
git clone https://github.com/sva-admin/prom-motion-skill.git
cd prom-motion-skill
```

Then run:

```bash
claude plugin validate . --strict
claude --plugin-dir .
```

In that Claude Code session, invoke `/prom-motion:prom-motion`. Loading a plugin does not install FFmpeg, download models, or provide an editing service. The agent needs access to your files and a suitable editor or local rendering tools. Tell it if it should only plan.

Install from the public GitHub marketplace with these commands inside Claude Code:

```text
/plugin marketplace add sva-admin/prom-motion-skill
/plugin install prom-motion@prom-motion-marketplace
```

These are Claude Code slash commands. Do not use the marketplace instructions against an older revision containing only the standalone skill. Confirm that `.claude-plugin/plugin.json` is present first.

For Codex, copy `skills/prom-motion` into your configured skills directory and invoke `$prom-motion`. Plugin manifest formats differ between hosts; this package's plugin manifest targets Claude Code. The skill folder remains portable.

## 1. Give a brief

> Use Prom Motion. Make a 45 to 60 second story for people who have never heard of this project. The takeaway is that a small team solved one recognisable problem. Use the footage in the folder I provide. Keep real speech and complete sentences, use Thai above English subtitles, and do not add music or generated scenes. First return a storyboard with exact source ranges. Do not render yet.

Also provide your intended audience, destination, available source files and anything the film must preserve. State whether source media may leave your computer.

## 2. Ask for the logic

> Give me three opening lines that actually exist in the footage. For each, show the source timecodes, the question it creates, the later shot that answers it, and any uncertain transcription. Choose one and explain why each following beat belongs. Mark unread or unheard material explicitly.

Use [the paper edit template](skills/prom-motion/assets/paper-edit-template.json). Do not accept invented quotations, labels such as "best moment" with no source, or an ending that answers a different question.

## 3. Approve a small proof

> Render the opening and one representative speech-to-B-roll join from the approved storyboard. Use my existing footage and local tools. Show the playable export with its subtitle cues, source map and rerender command. Do not buy assets or upload my media.

Watch with sound at normal speed. Check the opening, every sentence ending, speaker identity and caption readability. A transcription or waveform is supporting evidence, not proof that a sentence sounds complete.

## 4. Give a narrow revision

> At 00:28 the speaker is cut off before completing the thought. Find the complete sentence in the source. Extend the thought or replace the whole sentence, keep the approved ending, and update both subtitle languages. Report the changed time range and recheck the actual export.

Specific feedback is more useful than "make it cinematic". Name the problem, the time and the part that should stay.

## 5. Finish and keep the source

Deliver the video, editable cut data, subtitle cues, source ranges and version notes together. Confirm which file was reviewed and which was published. Do not assume a file named `final` is the uploaded version.

Local rendering has no per-render service fee. Agent subscriptions, API usage, optional generated media and licensed assets may cost money. Set a budget separately if you want them.
