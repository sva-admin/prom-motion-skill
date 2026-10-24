# Multilingual video finishing

Confirm the delivery matrix first: duration, aspect ratio, resolution, frame rate, narration language, subtitle languages, combined versus separate subtitle editions, clean or music versions, and editable handover files. Do not multiply exports when languages are meant to appear together.

Use `technical-checks.md` for media checks and `../assets/caption-cues-template.json` for a shared caption record.

## Prepare picture and sound

Inspect rotation metadata and a visible frame. Some camera clips are sideways with no flag; the correct direction can differ between shoots. Do not apply a blanket transpose or mirror from another project. Inspect color primaries, transfer and bit depth. Convert HDR for an SDR deliverable only when needed, and compare skin, whites and highlights on the actual output.

Listen to original and processed dialogue. High-pass filtering or denoising should solve an audible problem without changing the voice. Record and compensate processing latency. Measure loudness and peaks against the agreed target, then listen again. A previous project's LUFS target is a starting point to confirm, not a universal broadcast specification.

## One subtitle source

Keep cue IDs, source/timeline times, original speech, approved translations, speaker and uncertainty in one JSON or spreadsheet. Generate SRTs and burned captions from that source. Do not repair several exported SRTs independently.

Check actual language before transcription. Machine Thai word timestamps may split written words, so choose readable phrase boundaries. Maintain a reviewed glossary for names, titles and technical terms. Mark unclear hearing or translation for review instead of silently choosing a plausible meaning. Simplified and Traditional Chinese are distinct choices.

For combined languages, establish a consistent order and sufficient reading time. In a three-language layout, shorten captions into consecutive phrase cues before shrinking type. Check Thai combining marks and Chinese glyph coverage with licensed fonts. Wait for fonts to load before measuring or rendering text. Preserve English narration meaning across translations and obtain the nominated language approver's review.

Place subtitles away from faces, mouths, nameplates and platform controls. Use aspect-specific layouts. Check a phone-size viewing copy and the actual delivery context; old safe-area pixel values are not permanent platform rules.

## Finish and hand over

Export a short stress test containing the longest caption, longest name, a bright frame, a dark frame, dialogue and a transition. Verify the actual encoded file, not only the composition preview. Then export the full film and check beginning, ending, every changed boundary, caption overflow, sync and playback.

Keep source/proxy mapping, edit data, cue data, font names and licence notes, tool versions, render settings, output hashes and a concise review log. Run one heavy decode, transcription or render job at a time on a constrained machine. Stop a failed batch, inspect its cause and resume from the recorded completed items rather than blindly restarting.
