# Changelog

All notable changes to this repository are documented in this file, newest
first. The format loosely follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

This project didn't tag releases as it went, so the version numbers below
were assigned retroactively, one per shipped feature/PR, using each change's
commit date. There is no published package — "version" here just means "a
point in the repo's history worth naming." A rendered, browsable copy of
this file lives in [`changelog.html`](changelog.html).

## [0.8.0] - 2026-08-14

### Added
- `CHANGELOG.md` (this file) — full version history of the repo.
- `changelog.html` — a styled, filterable page to browse the same history
  in a browser, matching the look of the other standalone pages.

**Impacted:** `README.md` (new "Changelog" link). No runtime/game code changed.

## [0.7.0] - 2026-08-04

### Added
- `westeros_chronicle.html` — a maester's-chronicle recap of the whole
  story: five narrative eras (Ned Stark's execution through the Battle of
  Winterfell and the fall of King's Landing), a fate ledger for all eight
  great houses plus the Night's Watch, and arcs for the seven characters
  who decided most of it.
- A brass-astrolabe canvas animation behind the header, driven by
  `drawRing()`, that respects `prefers-reduced-motion`.
- Fraunces/Newsreader webfonts bundled inline as base64 so the page needs
  no network access.

### Changed
- `README.md` — new "Chronicle of Westeros" section.

**Impacted:** `westeros_chronicle.html` (new — era timeline, house ledger
table, character arc cards, `drawRing()`), `README.md`.

## [0.6.1] - 2026-07-08

### Changed
- `GOT.py` — the radar chart's legend switched from matplotlib's plain-text
  legend to circular character-portrait thumbnails, ringed in each
  character's line color.

### Added
- `avatar_path()` in `GOT.py` — resolves a character's name to their
  portrait file under `avatars/`.
- `avatars/*.png` — six DiceBear-generated circular portraits (Jon Snow,
  Tywin Lannister, Lord Varys, Arya Stark, Sansa Stark, Daenerys
  Targaryen) composited onto parchment and circle-cropped with Pillow.
- `avatars/README.md` — documents how to regenerate the portraits.

**Impacted:** `GOT.py` (`avatar_path()`, the legend-drawing loop on
`legend_ax`), `avatars/` (new directory), `README.md`.

## [0.6.0] - 2026-07-08

### Added
- `westeros_map.html` — an interactive map of Westeros built with
  [Leaflet](https://leafletjs.com) in `CRS.Simple` mode. Coastline,
  rivers, forests, mountains and the Wall are original vector shapes.
- 14 clickable seats (Winterfell, King's Landing, Casterly Rock,
  Sunspear, and more) with popups tied to the character roster from
  Westeros Chess, plus a sidebar region legend that flies the map to any
  region.
- Helper functions `toLatLng()`, `pathD()`, `el()`, and `makeIcon()`.

### Changed
- `README.md` — new "Map of Westeros" section.

**Impacted:** `westeros_map.html` (new), `README.md`.

## [0.5.0] - 2026-07-08

### Added
- `westeros_chess.html` — a fully playable, self-contained chess game
  skinned with Game of Thrones characters, built on a bundled chess.js
  engine (legal moves, check/checkmate/stalemate/draw detection,
  castling, en passant, pawn promotion).
- App-level UI functions: `buildInitialPieces()`, `renderBoard()`,
  `renderAll()`, `renderHistory()`, `renderGraveyard()`,
  `renderPromotionPicker()`, `updateStatus()`, `initials()`.
- Move history panel, a "Fallen" panel for captured pieces, undo, and a
  board-flip toggle.

### Removed
- `Got.jsx` and `WesterosChess.py` — the earlier React and Python
  prototypes, superseded by the single-file HTML game.

### Changed
- `README.md` — "Westeros Chess" section rewritten to describe the
  shipped game instead of the prototypes.

**Impacted:** `westeros_chess.html` (new), `Got.jsx` (removed),
`WesterosChess.py` (removed), `README.md`.

## [0.4.0] - 2025-11-10

### Added
- `got_python/__init__.py` and `got_python/README.md` — package scaffold
  for future Python analysis modules, establishing the `got_python`
  import boundary.

### Changed
- `README.md` — documents the suggested `got_python` structure and
  example usage.

**Impacted:** `got_python/` (new package), `README.md`.

## [0.3.0] - 2025-11-07

### Added
- `Got.jsx` — a React prototype for a GoT-skinned chess UI.
- `WesterosChess.py` — a Python prototype exploring the chess logic.

> Both prototypes were removed in `0.5.0` once `westeros_chess.html`
> shipped as the finished game.

**Impacted:** `Got.jsx` (new, later removed), `WesterosChess.py` (new,
later removed).

## [0.2.0] - 2025-11-05

### Changed
- `GOT.py` — renamed `"Varys"` to `"Lord Varys"` in the `characters` dict,
  added a `"Daenerys Targaryen"` entry, and moved the legend's
  `bbox_to_anchor` from `(1.3, 1.1)` to `(1.5, 1.1)` to fit the wider
  legend.
- `README.md` — added a "Westeros Chess" section ahead of the game
  actually shipping.

**Impacted:** `GOT.py` (`characters` dict, `ax.legend()` call),
`README.md`.

## [0.1.0] - 2025-10-31

### Added
- Initial commit — `README.md` project description.
- `GOT.py` — the first radar chart, comparing five characters (Jon Snow,
  Tywin Lannister, Varys, Arya Stark, Sansa Stark) across seven traits
  (Leadership, Combat, Scheming, Strategy, Planning, Analysis, Origin)
  using a matplotlib polar plot.

**Impacted:** `README.md` (new), `GOT.py` (new).

[0.8.0]: #080---2026-08-14
[0.7.0]: #070---2026-08-04
[0.6.1]: #061---2026-07-08
[0.6.0]: #060---2026-07-08
[0.5.0]: #050---2026-07-08
[0.4.0]: #040---2025-11-10
[0.3.0]: #030---2025-11-07
[0.2.0]: #020---2025-11-05
[0.1.0]: #010---2025-10-31
