"""Canonical tag translation: mechanical slugging + tags.toml aliases/drops.
Import from harvest scripts; the same semantics are implemented in consumers."""
import fnmatch
import re
from pathlib import Path

try:
    import tomllib  # 3.11+
    def _load(p): return tomllib.loads(p.read_text())
except ImportError:
    import toml
    def _load(p): return toml.loads(p.read_text())


def slug(s: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


class TagMap:
    def __init__(self, repo_root: Path):
        d = _load(repo_root / 'tags.toml')
        self.drop = d.get('drop', [])
        self.aliases = d.get('aliases', {})

    def canonical(self, vendor_tags):
        """vendor tag strings -> ordered, deduped canonical tags"""
        out, seen = [], set()
        for raw in vendor_tags:
            s = slug(raw)
            if not s or any(fnmatch.fnmatch(s, pat) for pat in self.drop):
                continue
            for c in self.aliases.get(s, [s]):
                if c not in seen:
                    seen.add(c)
                    out.append(c)
        return out
