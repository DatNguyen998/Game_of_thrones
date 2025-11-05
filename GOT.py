import matplotlib.pyplot as plt
import numpy as np

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
    "Daenerys Targaryen": [8,7,6,7,6,6,7]
}

# Radar chart setup
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

for name, values in characters.items():
    values += values[:1]
    ax.plot(angles, values, linewidth=2, label=name)
    ax.fill(angles, values, alpha=0.15)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)
ax.set_yticklabels([])
ax.set_title("Character Skill Profiles – Game of Thrones", size=14, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.5, 1.1))

plt.show()
