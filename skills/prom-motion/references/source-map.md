# Source and beat records

Keep one data source for the editor, storyboard, captions and review page. Generate mirrors from it rather than maintaining competing copies.

A source record needs: stable ID; relative or external path; remote file ID where relevant; bytes and checksum; original versus proxy; duration and timebase; orientation and color metadata; audio presence; date or event context; what was actually reviewed; rights or identity restrictions; uncertainty.

A beat needs: purpose; source ID; source in/out; timeline in/out; audio source and its own in/out; exact spoken line; factual claim and evidence; on-screen text; subtitle cues; transition rationale; status and reviewer.

Use source seconds for finding the recording and integer timeline frames for the edit. Declare the frame rate. Record speed changes and offsets explicitly. Do not silently mix source time, interview-master time and finished-film time.

Keep a terminology sheet for names, titles, products and translations. If a source contradicts another, retain both and name the unresolved decision. A partner portfolio proves the partner's work unless the client's role is separately documented.

The example JSON contains invented transcript text and synthetic paths. Its `fictional_practice` flag prevents it from being mistaken for client evidence. Replace it with reviewed observations for real work.
