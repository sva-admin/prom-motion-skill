# Technical checks

## Source inspection

If FFmpeg is already installed, this read-only probe shows useful metadata:

```bash
ffprobe -v error -show_streams -show_format -of json "source.mp4"
```

Record display dimensions, rotation, duration, frame rate/timebase, audio sample rate/channels and color tags. Confirm a representative frame and audible source. A missing tag is an unknown, not proof of upright SDR footage.

## Output review

- Dimensions and aspect match the delivery matrix; vertical crop keeps the relevant action.
- Timeline frame counts and source trims agree. Speed changes include enough source handles.
- Dialogue sync is checked after isolation, limiting, resampling and export. Processing can add latency even when durations match.
- Captions have positive duration, ordered non-overlapping times, matching language cue IDs and required text in each language. Intentional exceptions are recorded.
- Font files load and support Thai marks and Chinese characters. No tofu boxes, clipped accents or unexpected fallback.
- Transparent graphics retain alpha in the actual decoder/compositor. Some video pipelines silently discard it; test a small overlay before the batch.
- Scene changes, final words, generated joins and any loop wrap pass normal-speed playback. A frame-difference metric supports review but does not establish visual quality.
- A QR, if requested, decodes from the final encoded frames at intended viewing size. A QR in the source artwork is not enough.
- The delivered file opens and seeks in its intended player. A custom review server needs byte-range support for large video seeking.

## Reproducibility

Record source and output hashes, edit version, command or renderer settings, font versions and approval status. An output named final may still be a draft. Do not overwrite a previously approved export while experimenting.

Do not carry old recipes blindly: one crop's mirror, one shoot's transpose direction, one HDR conversion, one microphone's filter or one renderer's alpha workaround may be wrong for the next input. Test a small representative sample first.
