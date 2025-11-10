```markdown
# got_python

This folder is intended to hold all Python code related to Game of Thrones analysis for the repository.

Purpose
- Organize Python modules that analyze or evaluate characters and other data related to GoT.
- Provide a clear package boundary so Python code can be imported as `got_python`.

Suggested structure
- got_python/
  - __init__.py
  - characters.py        # character classes, loaders, analyzers
  - utils.py             # helper utilities (parsing, common constants)
  - data/                 # optional: packaged or example data
  - tests/                # unit tests for the Python modules

Example usage
```py
# from the repository root (or after installing as a package)
from got_python import characters
# characters.do_some_analysis(...)
```

Contributing
- Add Python modules under `got_python/`.
- Add tests under `got_python/tests/`.
- Keep top-level imports in `__init__.py` minimal to avoid heavy imports on package import.

License & provenance
- Follow the repository's existing license and contribution guidelines.
```
