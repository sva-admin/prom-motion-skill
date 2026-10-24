#!/usr/bin/env python3
"""Package the reviewed plugin files. No install, upload or network access."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / '.claude-plugin/plugin.json').read_text())
version = manifest['version']
files = [root / n for n in ['README.md', 'QUICKSTART.md', 'CHANGELOG.md', 'LICENSE']]
for folder in ['.claude-plugin', 'skills', 'scripts']:
    files += [p for p in (root / folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc']
out = root / 'dist' / f'prom-motion-{version}.zip'
out.parent.mkdir(exist_ok=True)
with ZipFile(out, 'w', compression=ZIP_DEFLATED) as archive:
    for file in sorted(files):
        relative = file.relative_to(root)
        assert not file.is_symlink(), f'Review symlink before packaging: {relative}'
        record = ZipInfo('prom-motion/' + relative.as_posix(), (2026, 10, 24, 0, 0, 0))
        record.compress_type = ZIP_DEFLATED
        record.external_attr = 0o100644 << 16
        archive.writestr(record, file.read_bytes())
print(f'{len(files)} files, {out.stat().st_size} bytes')
print(f'SHA-256 {hashlib.sha256(out.read_bytes()).hexdigest()}')
