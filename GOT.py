import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from pathlib import Path

# Character portraits live in avatars/, generated offline with DiceBear
# (github.com/dicebear/dicebear, MIT licensed) from each character's name —
# original illustrated avatars, not photos of the actors or show artwork.
# See avatars/README.md to regenerate them.
AVATAR_DIR = Path(__file__).parent / "avatars"


def avatar_path(name):
    slug = name.lower().replace("lord ", "").replace(" ", "_")
    return AVATAR_DIR / f"{slug}.png"


# Define the categories and the characters
categories = ["Leadership", "Combat", "Scheming", "Strategy", "Planning", "Analysis", "Origin"]
N = len(categories)

# Scores for selected characters
characters = {
    "Jon Snow": [9, 8, 4, 7, 7, 9, 6],
    "Tywin Lannister": [9, 6, 8, 10, 9, 9, 9],
    "Lord Varys": [7, 2, 10, 9, 9, 10, 8],
    "Arya Stark": [6, 10, 7, 7, 6, 8, 5],
    "Sansa Stark": [7, 2, 8, 8, 8, 9, 7],
    "Daenerys Targaryen": [8, 7, 6, 7, 6, 6, 7],
}

# Radar chart setup
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig = plt.figure(figsize=(12, 8))
ax = plt.subplot(111, polar=True)

colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

for (name, values), color in zip(characters.items(), colors):
    values = values + values[:1]
    ax.plot(angles, values, linewidth=2, label=name, color=color)
    ax.fill(angles, values, alpha=0.15, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)
ax.set_yticklabels([])
ax.set_title("Character Skill Profiles – Game of Thrones", size=14, pad=20)

# Avatar legend: each character's portrait next to their name, colored to
# match their radar line, instead of matplotlib's plain-text legend.
legend_ax = fig.add_axes([0, 0, 1, 1])
legend_ax.set_xlim(0, 1)
legend_ax.set_ylim(0, 1)
legend_ax.axis("off")

legend_x, top_y, row_h = 0.8, 0.85, 0.11
for i, ((name, _), color) in enumerate(zip(characters.items(), colors)):
    y = top_y - i * row_h
    path = avatar_path(name)
    if path.exists():
        thumbnail = OffsetImage(mpimg.imread(path), zoom=0.19)
        legend_ax.add_artist(AnnotationBbox(
            thumbnail, (legend_x, y), frameon=True,
            bboxprops=dict(edgecolor=color, linewidth=2.5, boxstyle="circle"),
        ))
    legend_ax.text(legend_x + 0.055, y, name, va="center", fontsize=9.5, color=color, fontweight="bold")

plt.subplots_adjust(left=0.05, right=0.72)
plt.show()
