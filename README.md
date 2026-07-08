# Game_of_thrones
This is simply an idea to evaluate some characters in GoT.

# Westeros Chess

A fully playable chess game skinned with Game of Thrones characters — open
`westeros_chess.html` in any browser, no build step or install required.

- Standard chess rules (legal moves, check/checkmate/stalemate/draw detection,
  castling, en passant, pawn promotion) via the bundled [chess.js](https://github.com/jhlywa/chess.js)
  engine.
- Click a piece to see its legal moves highlighted, then click a destination
  square to move. Each of the 32 pieces is a named GoT character whose
  identity follows it through captures, castling, and promotion.
- Move history, a "Fallen" panel for captured pieces, undo, and a board-flip
  toggle are all built in.

# Map of Westeros

An interactive map of Westeros — open `westeros_map.html` in any browser, no
build step or install required.

- Built with [Leaflet](https://leafletjs.com) in `CRS.Simple` mode (a flat
  coordinate plane rather than real-world lat/lng), bundled inline so it
  needs no network access to run.
- The coastline, rivers, forests, mountains and the Wall are original vector
  shapes drawn for this project — not a trace of the show's map artwork.
- 14 clickable seats (Winterfell, King's Landing, Casterly Rock, Sunspear,
  and more) with popups tying each one back to the character roster used in
  Westeros Chess. A region legend in the sidebar flies the map to any region.

# Radar chart

`GOT.py` plots a radar chart comparing characters across traits like
Leadership, Combat, and Scheming (scores chosen subjectively — feel free to
tweak them). Its legend shows each character's portrait instead of plain
text: circular avatars generated offline with [DiceBear](https://www.dicebear.com)
(MIT licensed) from the character's name — original illustrations, not show
photos. See `avatars/README.md` to regenerate or add more.

```
pip install matplotlib numpy pillow
python GOT.py
```

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
# characters.do_some_analysis(...
