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

Create the Radar chart for some of the fav characters in GoT.
characters = {
    "Jon Snow": [9, 8, 4, 7, 7, 9, 6],
    "Tywin Lannister": [9, 6, 8, 10, 9, 9, 9],
    "Varys": [7, 2, 10, 9, 9, 10, 8],
    "Arya Stark": [6, 10, 7, 7, 6, 8, 5],
    "Sansa Stark": [7, 2, 8, 8, 8, 9, 7]
}

Use ChatGpt to evaluate characters based on their traits and giving relevant scores.
Finally, using Matlab to create a Radar Chart.

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
