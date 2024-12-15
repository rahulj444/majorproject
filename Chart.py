import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.cm import get_cmap

# Data
Accuracy = [78.41, 98.0]
Precision = [99.0, 95.2]
Recall = [79.2, 92.6]
FScore = [87.5, 93.6]

# Parameters
n = 2
r = np.arange(n)
width = 0.20
bar_gap = 0.05  # Gap between bars

# Define colors with gradients
cmap = get_cmap("viridis")
accuracy_colors = [cmap(0.2), cmap(0.4)]
precision_colors = [cmap(0.5), cmap(0.6)]
recall_colors = [cmap(0.7), cmap(0.8)]
fscore_colors = [cmap(0.9), cmap(1.0)]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars with individual colors and advanced styles
bars1 = plt.bar(r, Accuracy, color=accuracy_colors, width=width, edgecolor='black', label='Accuracy', alpha=0.9, hatch='//')
bars2 = plt.bar(r + width + bar_gap, Precision, color=precision_colors, width=width, edgecolor='black', label='Precision', alpha=0.9, hatch='\\')
bars3 = plt.bar(r + 2 * (width + bar_gap), Recall, color=recall_colors, width=width, edgecolor='black', label='Recall', alpha=0.9, hatch='x')
bars4 = plt.bar(r + 3 * (width + bar_gap), FScore, color=fscore_colors, width=width, edgecolor='black', label='FScore', alpha=0.9, hatch='*')

# Add annotations on top of bars
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),  # Offset for text
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, color='black', weight='bold')

# Add labels and title
plt.xlabel("Comparison Algorithms", fontsize=14, labelpad=15, weight='bold', color='darkblue')
plt.ylabel("Performance Value (%)", fontsize=14, labelpad=15, weight='bold', color='darkblue')
plt.title("Advanced Performance Comparison of Algorithms", fontsize=18, weight='bold', pad=20, color='darkgreen')

# Customize the x-axis
plt.xticks(r + 1.5 * (width + bar_gap), ['SVM', 'DT'], fontsize=12, weight='bold', rotation=15, color='darkred')

# Add a grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.5, color='gray')

# Improve the legend with custom patches
legend_patches = [
    mpatches.Patch(color=cmap(0.2), label='Accuracy', alpha=0.9, hatch='//'),
    mpatches.Patch(color=cmap(0.5), label='Precision', alpha=0.9, hatch='\\'),
    mpatches.Patch(color=cmap(0.7), label='Recall', alpha=0.9, hatch='x'),
    mpatches.Patch(color=cmap(0.9), label='FScore', alpha=0.9, hatch='*')
]
plt.legend(handles=legend_patches, fontsize=12, loc='upper left', frameon=True, shadow=True, borderpad=1, title="Metrics", title_fontsize=13)

# Add advanced axis effects
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_color('darkblue')
ax.spines['bottom'].set_color('darkblue')

# Add background gradient
ax.set_facecolor('#f0f8ff')
ax.set_alpha(0.95)

# Add watermark
plt.text(1.5, -10, 'Generated with Matplotlib', fontsize=12, color='gray', alpha=0.5, ha='center', va='center', rotation=0)

# Fine-tune layout
plt.tight_layout()

# Show the plot
plt.show()
