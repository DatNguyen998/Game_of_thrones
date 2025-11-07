import React, { useMemo, useState } from "react";
import { Chess } from "chess.js";
import { Chessboard } from "react-chessboard";

/**
 * Westeros Chess – map GoT characters onto a standard chess ruleset.
 * - Uses chess.js for the rules and react-chessboard for UI.
 * - Custom piece renderers show character initials + tooltip with full name & role.
 * - Starting position is our curated mapping from the chat.
 */

// --- Piece ↔ Character mapping (by color + type) ---
const WHITE = {
  K: { name: "Jon Snow", role: "King (Trắng)", color: "#1e293b" },
  Q: { name: "Daenerys Targaryen", role: "Queen", color: "#334155" },
  R1: { name: "Eddard Stark", role: "Rook", color: "#0f766e" },
  R2: { name: "Brienne of Tarth", role: "Rook", color: "#0f766e" },
  B1: { name: "Maester Aemon", role: "Bishop", color: "#1d4ed8" },
  B2: { name: "Samwell Tarly", role: "Bishop", color: "#1d4ed8" },
  N1: { name: "Arya Stark", role: "Knight", color: "#a21caf" },
  N2: { name: "(empty)", role: "Knight", color: "#a21caf" },
  P: [
    { name: "Davos Seaworth", role: "Pawn", color: "#166534" },
    { name: "Podrick Payne", role: "Pawn", color: "#166534" },
    { name: "Grenn", role: "Pawn", color: "#166534" },
    { name: "Davos Seaworth", role: "Pawn", color: "#166534" },
    { name: "Podrick Payne", role: "Pawn", color: "#166534" },
    { name: "Grenn", role: "Pawn", color: "#166534" },
    { name: "Davos Seaworth", role: "Pawn", color: "#166534" },
    { name: "Podrick Payne", role: "Pawn", color: "#166534" },
  ],
};

const BLACK = {
  K: { name: "Cersei Lannister", role: "King (Đen)", color: "#111827" },
  Q: { name: "Petyr Baelish (Littlefinger)", role: "Queen", color: "#111827" },
  R1: { name: "Tywin Lannister", role: "Rook", color: "#7c2d12" },
  R2: { name: "Roose Bolton", role: "Rook", color: "#7c2d12" },
  B1: { name: "Melisandre", role: "Bishop", color: "#991b1b" },
  B2: { name: "High Sparrow", role: "Bishop", color: "#991b1b" },
  N1: { name: "Sandor Clegane (The Hound)", role: "Knight", color: "#6b7280" },
  N2: { name: "(empty)", role: "Knight", color: "#6b7280" },
  P: [
    { name: "Ramsay Bolton", role: "Pawn", color: "#7f1d1d" },
    { name: "Joffrey Baratheon", role: "Pawn", color: "#7f1d1d" },
    { name: "Qyburn", role: "Pawn", color: "#7f1d1d" },
    { name: "Ramsay Bolton", role: "Pawn", color: "#7f1d1d" },
    { name: "Joffrey Baratheon", role: "Pawn", color: "#7f1d1d" },
    { name: "Qyburn", role: "Pawn", color: "#7f1d1d" },
    { name: "Ramsay Bolton", role: "Pawn", color: "#7f1d1d" },
    { name: "Joffrey Baratheon", role: "Pawn", color: "#7f1d1d" },
  ],
};

// Helper to make a round token for each piece with initials and a tooltip
function token(label: string, bg: string, title: string) {
  return (
    <div
      title={title}
      className="w-12 h-12 rounded-full flex items-center justify-center text-white text-xs font-semibold shadow-md"
      style={{ background: bg }}
    >
      {label}
    </div>
  );
}

// Derive initials from the character name
function initials(name: string) {
  if (!name || name === "(empty)") return "";
  return name
    .split(/\s+/)
    .filter(Boolean)
    .slice(0, 2)
    .map((w) => w[0]!.toUpperCase())
    .join("");
}

// Custom renderer map for react-chessboard
function useCustomPieces() {
  return useMemo(() => {
    return {
      wK: () => token(initials(WHITE.K.name), WHITE.K.color, `${WHITE.K.name} • ${WHITE.K.role}`),
      wQ: () => token(initials(WHITE.Q.name), WHITE.Q.color, `${WHITE.Q.name} • ${WHITE.Q.role}`),
      wR: () => token(initials(WHITE.R1.name), WHITE.R1.color, `${WHITE.R1.name} • ${WHITE.R1.role}`),
      wB: () => token(initials(WHITE.B1.name), WHITE.B1.color, `${WHITE.B1.name} • ${WHITE.B1.role}`),
      wN: () => token(initials(WHITE.N1.name), WHITE.N1.color, `${WHITE.N1.name} • ${WHITE.N1.role}`),
      wP: () => token("PW", WHITE.P[0].color, `Pawn • Davos/Podrick/Grenn`),

      bK: () => token(initials(BLACK.K.name), BLACK.K.color, `${BLACK.K.name} • ${BLACK.K.role}`),
      bQ: () => token(initials(BLACK.Q.name), BLACK.Q.color, `${BLACK.Q.name} • ${BLACK.Q.role}`),
      bR: () => token(initials(BLACK.R1.name), BLACK.R1.color, `${BLACK.R1.name} • ${BLACK.R1.role}`),
      bB: () => token(initials(BLACK.B1.name), BLACK.B1.color, `${BLACK.B1.name} • ${BLACK.B1.role}`),
      bN: () => token(initials(BLACK.N1.name), BLACK.N1.color, `${BLACK.N1.name} • ${BLACK.N1.role}`),
      bP: () => token("PW", BLACK.P[0].color, `Pawn • Ramsay/Joffrey/Qyburn`),
    };
  }, []);
}

// Build the FEN for our custom starting layout (standard chess orientation)
// We'll place pieces per our mapping, leaving empty slots where needed.
const START_FEN = (() => {
  // Rank 8 (black back rank): a8..h8 → Tywin (R), The Hound (N), Melisandre (B), Littlefinger (Q), Cersei (K), High Sparrow (B), (empty Knight -> use The Hound only at g8), Roose (R)
  const r8 = "rnbqkbr".split("");
  // But we want: a8 Tywin (r), b8 (n) The Hound, c8 (b) Mel, d8 (q) Littlefinger, e8 (k) Cersei, f8 (b) High Sparrow, g8 (n) The Hound actually is at b8; keep g8 knight as 'n' to allow movement but token identical; h8 (r) Roose.
  const rank8 = "rnbqkbnr"; // keep standard to satisfy rules; visuals map names.

  // Rank 7 (black pawns): use standard pawns
  const rank7 = "pppppppp";

  // Rank 2 (white pawns)
  const rank2 = "PPPPPPPP";

  // Rank 1 (white back rank): a1 Ned (R), b1 Arya (N), c1 Aemon (B), d1 Daenerys (Q), e1 Jon (K), f1 Sam (B), g1 (empty -> keep knight), h1 Brienne (R)
  const rank1 = "RNBQKBNR";

  // Empty ranks 3–6
  const empty = "8";

  const fen = `${rank8}/${rank7}/${empty}/${empty}/${empty}/${empty}/${rank2}/${rank1} w KQkq - 0 1`;
  return fen;
})();

// Side panel card for Varys + legend
function Legend() {
  return (
    <div className="space-y-4">
      <div className="p-4 rounded-2xl shadow bg-white/80 backdrop-blur">
        <h2 className="text-lg font-semibold">Legend – Who is who?</h2>
        <ul className="mt-2 text-sm leading-6 list-disc ml-5">
          <li><b>White</b>: Jon (K), Daenerys (Q), Ned & Brienne (R), Aemon & Sam (B), Arya (N), Davos/Podrick/Grenn (P)</li>
          <li><b>Black</b>: Cersei (K), Littlefinger (Q), Tywin & Roose (R), Melisandre & High Sparrow (B), The Hound (N), Ramsay/Joffrey/Qyburn (P)</li>
        </ul>
      </div>
      <div className="p-4 rounded-2xl shadow bg-white/80 backdrop-blur flex items-center gap-3">
        <div className="w-10 h-10 rounded-full bg-black text-white flex items-center justify-center text-xs">VA</div>
        <div>
          <div className="font-medium">Varys</div>
          <div className="text-sm text-slate-600">Master of the Board (observer)</div>
        </div>
      </div>
    </div>
  );
}

export default function WesterosChess() {
  const [game, setGame] = useState(() => new Chess(START_FEN));
  const customPieces = useCustomPieces();
  const [history, setHistory] = useState<string[]>([]);

  function safeGameMutate(mod) {
    setGame((g) => {
      const update = new Chess(g.fen());
      mod(update);
      return update;
    });
  }

  function onDrop(sourceSquare: string, targetSquare: string) {
    let moveMade = false;
    safeGameMutate((game) => {
      const move = game.move({ from: sourceSquare, to: targetSquare, promotion: "q" });
      if (move) {
        moveMade = true;
        setHistory((h) => [
          `${move.color === "w" ? "White" : "Black"}: ${move.san}`,
          ...h,
        ]);
      }
    });
    return moveMade;
  }

  function reset() {
    setGame(new Chess(START_FEN));
    setHistory([]);
  }

  return (
    <div className="min-h-screen w-full bg-gradient-to-br from-slate-100 to-slate-200 p-6">
      <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 space-y-4">
          <div className="flex items-center justify-between">
            <h1 className="text-2xl font-bold">Westeros Chess – Prototype</h1>
            <div className="flex gap-2">
              <button onClick={reset} className="px-3 py-2 rounded-xl bg-slate-900 text-white shadow hover:opacity-90">Reset</button>
            </div>
          </div>
          <div className="rounded-2xl shadow overflow-hidden bg-white/70 p-4">
            <Chessboard
              id="westeros-board"
              position={game.fen()}
              onPieceDrop={onDrop}
              customBoardStyle={{ borderRadius: 16 }}
              customLightSquareStyle={{ backgroundColor: "#f1f5f9" }}
              customDarkSquareStyle={{ backgroundColor: "#94a3b8" }}
              customPieces={customPieces}
              animationDuration={150}
              boardWidth={560}
            />
          </div>
        </div>
        <div className="space-y-4">
          <Legend />
          <div className="p-4 rounded-2xl shadow bg-white/80 backdrop-blur">
            <h2 className="text-lg font-semibold">Move history</h2>
            <ol className="mt-3 space-y-1 text-sm text-slate-700 max-h-72 overflow-auto">
              {history.length === 0 ? (
                <li className="text-slate-500">No moves yet. Drag a piece to start.</li>
              ) : (
                history.map((h, i) => <li key={i}>• {h}</li>)
              )}
            </ol>
          </div>
        </div>
      </div>
    </div>
  );
}
