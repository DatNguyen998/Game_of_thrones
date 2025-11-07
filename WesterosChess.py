# Westeros Chess (Python, no external deps)
# - Renders a chessboard with GoT character labels using matplotlib.
# - Supports simple UCI-style moves (e2e4, g8f6, etc.) without legality checks.
# - Saves a reusable script to /mnt/data/westeros_chess.py

import matplotlib.pyplot as plt
from typing import Dict, Tuple, List
import textwrap

# --- Piece → Character mapping (labels kept short for clarity) ---
WHITE_MAP = {
    "K": "Jon",
    "Q": "Dany",
    "R": ["Ned", "Brie"],
    "B": ["Aem", "Sam"],
    "N": ["Ary", "Ary"],  # duplicate label for both knights
    "P": ["Dav", "Pod", "Gre", "Dav", "Pod", "Gre", "Dav", "Pod"],
}
BLACK_MAP = {
    "K": "Cers",
    "Q": "LF",
    "R": ["Tyw", "Roos"],
    "B": ["Mel", "HSpr"],
    "N": ["Hnd", "Hnd"],
    "P": ["Ram", "Jof", "Qyb", "Ram", "Jof", "Qyb", "Ram", "Jof"],
}

# Starting placement uses standard chess, we map labels visually.
def starting_board() -> Dict[Tuple[int, int], str]:
    board = {}
    # Black back rank (8): a8..h8 -> r n b q k b n r
    back_black = ["r","n","b","q","k","b","n","r"]
    labels_b = {
        "r": iter(BLACK_MAP["R"]),
        "n": iter(BLACK_MAP["N"]),
        "b": iter(BLACK_MAP["B"]),
    }
    for x, p in enumerate(back_black):
        if p in "rnb":
            lab = next(labels_b[p])
        elif p == "q":
            lab = BLACK_MAP["Q"]
        elif p == "k":
            lab = BLACK_MAP["K"]
        board[(x,7)] = f"b{p.upper()}:{lab}"
    # Black pawns (7)
    for x in range(8):
        board[(x,6)] = f"bP:{BLACK_MAP['P'][x]}"
    # White pawns (2)
    for x in range(8):
        board[(x,1)] = f"wP:{WHITE_MAP['P'][x]}"
    # White back rank (1): a1..h1 -> R N B Q K B N R
    back_white = ["R","N","B","Q","K","B","N","R"]
    labels_w = {
        "R": iter(WHITE_MAP["R"]),
        "N": iter(WHITE_MAP["N"]),
        "B": iter(WHITE_MAP["B"]),
    }
    for x, p in enumerate(back_white):
        if p in "RNB":
            lab = next(labels_w[p])
        elif p == "Q":
            lab = WHITE_MAP["Q"]
        elif p == "K":
            lab = WHITE_MAP["K"]
        board[(x,0)] = f"w{p}:{lab}"
    return board

def uci_to_xy(m: str) -> Tuple[Tuple[int,int], Tuple[int,int]]:
    files = "abcdefgh"
    sx, sy = files.index(m[0]), int(m[1]) - 1
    tx, ty = files.index(m[2]), int(m[3]) - 1
    return (sx, sy), (tx, ty)

def apply_moves(board: Dict[Tuple[int,int], str], moves: List[str]) -> None:
    """Very naive mover: just relocates piece if source exists (allows captures)."""
    for m in moves:
        if len(m) != 4:
            continue
        (sx, sy), (tx, ty) = uci_to_xy(m)
        piece = board.get((sx, sy))
        if piece is None:
            continue
        board[(tx, ty)] = piece
        del board[(sx, sy)]

def draw_board(board: Dict[Tuple[int,int], str], title="Westeros Chess (Python)"):
    fig, ax = plt.subplots(figsize=(7.2,7.2))
    # Squares
    for x in range(8):
        for y in range(8):
            color = "#f1f5f9" if (x+y)%2==0 else "#94a3b8"
            rect = plt.Rectangle((x, y), 1, 1, facecolor=color)
            ax.add_patch(rect)
    # Grid lines
    ax.set_xlim(0,8); ax.set_ylim(0,8)
    ax.set_xticks([i+0.5 for i in range(8)]); ax.set_yticks([i+0.5 for i in range(8)])
    ax.set_xticklabels(list("abcdefgh")); ax.set_yticklabels([str(i) for i in range(1,9)])
    ax.tick_params(length=0)
    # Pieces
    for (x,y), tag in board.items():
        side_piece, label = tag.split(":")
        side = side_piece[0] # w/b
        # Token style
        fc = "#0f172a" if side=="w" else "#111827"
        ec = "white"
        circ = plt.Circle((x+0.5, y+0.5), 0.38, color=fc)
        ax.add_patch(circ)
        ax.text(x+0.5, y+0.5, label, ha="center", va="center", color=ec, fontsize=10, fontweight="bold")
    ax.set_title(title, pad=12)
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.show()

# Demo: start + a few moves
board = starting_board()
draw_board(board, "Westeros Chess – Start")

demo_moves = ["e2e4", "e7e5", "g1f3", "b8c6"]
apply_moves(board, demo_moves)
draw_board(board, "After moves: e2e4, e7e5, g1f3, b8c6")

# Save a reusable script for local use
script = r'''
import matplotlib.pyplot as plt

WHITE_MAP = {
    "K": "Jon", "Q": "Dany",
    "R": ["Ned", "Brie"], "B": ["Aem", "Sam"], "N": ["Ary","Ary"],
    "P": ["Dav","Pod","Gre","Dav","Pod","Gre","Dav","Pod"],
}
BLACK_MAP = {
    "K": "Cers", "Q": "LF",
    "R": ["Tyw","Roos"], "B": ["Mel","HSpr"], "N": ["Hnd","Hnd"],
    "P": ["Ram","Jof","Qyb","Ram","Jof","Qyb","Ram","Jof"],
}

def starting_board():
    board = {}
    back_black = ["r","n","b","q","k","b","n","r"]
    labels_b = {"r": iter(BLACK_MAP["R"]), "n": iter(BLACK_MAP["N"]), "b": iter(BLACK_MAP["B"])}
    for x,p in enumerate(back_black):
        if p in "rnb": lab = next(labels_b[p])
        elif p=="q": lab = BLACK_MAP["Q"]
        else: lab = BLACK_MAP["K"]
        board[(x,7)] = f"b{p.upper()}:{lab}"
    for x in range(8):
        board[(x,6)] = f"bP:{BLACK_MAP['P'][x]}"
        board[(x,1)] = f"wP:{WHITE_MAP['P'][x]}"
    back_white = ["R","N","B","Q","K","B","N","R"]
    labels_w = {"R": iter(WHITE_MAP["R"]), "N": iter(WHITE_MAP["N"]), "B": iter(WHITE_MAP["B"])}
    for x,p in enumerate(back_white):
        if p in "RNB": lab = next(labels_w[p])
        elif p=="Q": lab = WHITE_MAP["Q"]
        else: lab = WHITE_MAP["K"]
        board[(x,0)] = f"w{p}:{lab}"
    return board

def uci_to_xy(m):
    files = "abcdefgh"
    return (files.index(m[0]), int(m[1])-1), (files.index(m[2]), int(m[3])-1)

def apply_moves(board, moves):
    for m in moves:
        if len(m)!=4: continue
        (sx,sy),(tx,ty) = uci_to_xy(m)
        piece = board.get((sx,sy))
        if not piece: continue
        board[(tx,ty)] = piece
        del board[(sx,sy)]

def draw_board(board, title=\"Westeros Chess\"):
    fig, ax = plt.subplots(figsize=(7.2,7.2))
    for x in range(8):
        for y in range(8):
            color = \"#f1f5f9\" if (x+y)%2==0 else \"#94a3b8\"
            ax.add_patch(plt.Rectangle((x,y),1,1,facecolor=color))
    ax.set_xlim(0,8); ax.set_ylim(0,8)
    ax.set_xticks([i+0.5 for i in range(8)]); ax.set_yticks([i+0.5 for i in range(8)])
    ax.set_xticklabels(list(\"abcdefgh\")); ax.set_yticklabels([str(i) for i in range(1,9)])
    ax.tick_params(length=0)
    for (x,y), tag in board.items():
        side_piece, label = tag.split(\":\")
        side = side_piece[0]
        fc = \"#0f172a\" if side==\"w\" else \"#111827\"
        circ = plt.Circle((x+0.5, y+0.5), 0.38, color=fc)
        ax.add_patch(circ)
        ax.text(x+0.5, y+0.5, label, ha=\"center\", va=\"center\", color=\"white\", fontsize=10, fontweight=\"bold\")
    ax.set_title(title, pad=12); ax.set_aspect(\"equal\"); plt.tight_layout(); plt.show()

if __name__ == \"__main__\":
    b = starting_board()
    draw_board(b, \"Start\")
    demo = [\"e2e4\",\"e7e5\",\"g1f3\",\"b8c6\"]
    apply_moves(b, demo)
    draw_board(b, \"After: \" + \",\".join(demo))
'''
with open("/mnt/data/westeros_chess.py", "w", encoding="utf-8") as f:
    f.write(script)

print("Saved: /mnt/data/westeros_chess.py")
