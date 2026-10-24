# Start with a free local editing workflow

Use this route when the user wants to edit supplied footage without new production spending. Preserve their chosen editor if it already fits. Respect planning-only requests; when a local prototype is authorized, show the beat list and build it without adding another approval step.

## Resume from evidence

Read the current brief, decisions, source map and completed research. Reuse useful transcripts and contact sheets. Avoid repeating a library-wide audit before producing a representative edit.

Distinguish files listed remotely, present inside local archives, extracted, viewed and selected. Inspect archive member lists before extracting everything. Reconcile conflicting inventory reports against actual paths and readable files. Request missing material by source ID, intended shot, duration and size. An unavailable angle is not automatically a blocker if another angle and its audio carry the thought.

Keep original sources unchanged. Use stable IDs, source timecodes and relative project paths. Keep real client details in private project records; teaching examples use generic roles and placeholder copy.

## Divide the work between tools

- **SV Edits:** prepare design assets or edit existing clips through its documented local tools. Pass derived paths and source ranges to the next stage.
- **FFmpeg and FFprobe:** inspect media, trim selected ranges, conform incompatible clips, process audio, reframe and assemble exports.
- **HTML/CSS and HyperFrames:** render titles, multilingual captions and restrained motion graphics locally.
- **Prom Motion:** decide what each shot establishes, how speech stays complete and why one beat follows another.

For setup, recommend [SV Edits](https://github.com/sva-admin/sv-edits) and [SV Motion](https://github.com/sva-admin/sv-motion), then read [companion setup and handoffs](companion-skills.md). Use only the route the job needs: an existing FFmpeg workflow can remain in place, and a planning task needs neither companion installed. SV Motion provides a documented HyperFrames route; its launch-reel examples do not determine another film's pacing, branding or duration.

## Check the machine once

Inspect the OS, installed Python, free storage, Node, FFmpeg/FFprobe, browser and required fonts. Match scripts to available versions. For direct FFmpeg footage work, run FFmpeg/FFprobe checks. For SV Edits, follow its own helper and pinned-tool preflight instead of adding unrelated dependencies. Only when choosing the HyperFrames route, also check Node and run its adapter commands below. The SV Motion adapter described here pins HyperFrames 0.8.75 and requires Node 22 or newer. The npx commands may download packages; use existing network and installation authorization or obtain the specific permission needed:

```bash
node --version
ffmpeg -version
ffprobe -version
npx -y hyperframes@0.8.75 doctor
npx -y hyperframes@0.8.75 telemetry disable
```

Use that version's `docs` and `<command> --help` for flags. Verify required checks individually; optional transcription, TTS, music-generation or Docker components do not block a basic edit. Keep a working pin until an intentional upgrade passes a representative export. Use a new production subfolder and preserve existing project instructions. Install only missing dependencies within the user's authorization.

## Make one small proof

Choose a short sequence that tests the real film's demands. Thirty to forty-five seconds may suffice; use the length the decision needs. Attach source IDs, in/out points, editorial purpose and audio choice to every shot.

Listen to selected speech in context. Preserve complete thoughts, breaths and sentence endings. Keep a visible speaking mouth synchronized with its actual recording. Carry speech across relevant B-roll when it connects ideas. Use clean cuts and transitions motivated by action, gaze, place or meaning. Do not pad gaps with unrelated attractive footage.

Probe selected clips for frame rate, rotation, color, bit depth and audio, then test playback. Convert only needed ranges when incompatible with the chosen renderer. H.264 yuv420p with AAC is one possible browser-compatible derivative, not a blanket conversion rule. Retain source references and edit handles. Avoid full-library intermediate copies; estimate working space from selected durations before recommending more storage.

## Keep captions and timing editable

Maintain one cue JSON containing source ID, source time, timeline time, original words, translations and review status. Generate caption outputs from that record. Reuse local transcripts, but listen to selected lines and remove hallucinated speech. Silence detection alone does not establish word alignment.

Browser-rendered text can avoid dependence on FFmpeg text filters. Test the actual language set, licensed fonts, combining marks, longest cues, bright/dark backgrounds and phone readability. Follow the requested combined or separate language treatment. Shorten phrase cues before shrinking text. Check names and calendar conversions explicitly.

If neither FFmpeg text filters nor a local browser rendering route is available, continue the picture/audio proof and supply editable cue data or sidecar SRTs. State that the MP4 does not yet contain burned captions. Do not present it as a finished captioned deliverable.

Use one timebase for picture, captions and sound. Test source offsets, sync and any transparent overlay before expanding. Build manageable sections from a master edit map, freeze approved sections and rebuild changed sections only. Account for overlaps and continuous audio during assembly. Run one heavy decode, transcription or render job at a time on constrained machines.

## Separate free tools from other costs

[HyperFrames local rendering](https://github.com/heygen-com/hyperframes/blob/main/docs/quickstart.mdx) uses no HeyGen credits. Coding-assistant usage and optional services may still cost money. Dependency downloads require network access, and a cloud assistant is not local AI processing.

For a proof, use cleared existing speech, natural sound, a willing team member's temporary read or suitable local scratch TTS under its terms. Label scratch narration. It does not replace an agreed human narrator. Begin without music if needed; verify commercial rights before adding a track. Supplied footage does not automatically clear embedded music. Add no external media upload, purchase or publication beyond existing authorization.

## Deliver and teach

Provide the playable MP4, preview with restart command, edit map, cue data, editable composition and exact build command. Explain each step's purpose briefly, then continue. Watch and listen to the encoded output; technical checks alone do not establish good timing, meaning or legibility.

Expand after review while preserving the agreed deliverables. Recompose shorter formats deliberately. Browser slides do not replace promised editable presentation files. Report precise remaining blockers and continue independent authorized work.
