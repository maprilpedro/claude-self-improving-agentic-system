# _inbox — drop zone

Drop raw captures here (transcripts, Slack copies, email exports, canvases) without
thinking about routing. Swept at session start and by `/ingest-transcript` (no-arg
form checks here first, then the vault `Meeting Notes/`). After ingestion the file
moves to its real home (vault `Meeting Notes/`) or gets deleted — this folder should
be empty most of the time.

Contents are gitignored (raw internal material belongs in the vault, not this repo);
this README is the only committed file.
