#!/usr/bin/env python3
"""Build the source-only .hnmod bundle for the offline Horizon release."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[2]
MOD = ROOT / "mods" / "veinminer"
manifest = json.loads((MOD / "horizon-native.json").read_text())
files = {"horizon-native.json": (MOD / "horizon-native.json").read_bytes()}
for name in ("horizon-mixin.toml", "runtime.rs", "mining.rs"):
    files[f"mixins/veinminer/{name}"] = (MOD / name).read_bytes()

out = ROOT / "target" / f"veinminer-{manifest['version']}.hnmod"
out.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as archive:
    for name, content in sorted(files.items()):
        info = zipfile.ZipInfo(name, (2026, 10, 30, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, content)
print(f"Created: {out}")
print(f"SHA-256: {hashlib.sha256(out.read_bytes()).hexdigest()}")
