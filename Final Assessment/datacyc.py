import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create a figure for the flow diagram
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

# Define box positions and sizes
box_width = 3
box_height = 1
spacing = 1.5

# Define the stages
stages = [
    "Acquire Data",
    "Prepare Data",
    "Analyze Data",
    "Report Insights",
    "Act on Insights"
]

# Define box positions
y_positions = [spacing * i for i in range(len(stages))][::-1]
boxes = [(0, y) for y in y_positions]

# Add arrows and labels
for i, (x, y) in enumerate(boxes):
    # Draw a rectangle for each stage
    rect = mpatches.Rectangle((x - box_width / 2, y - box_height / 2),
                              box_width, box_height, facecolor='lightblue',
                              edgecolor='black', lw=2)
    ax.add_patch(rect)
    # Add text for each stage
    ax.text(x, y, stages[i], ha='center', va='center', fontsize=10, fontweight='bold')
    # Draw an arrow to the next stage (if not the last stage)
    if i < len(boxes) - 1:
        next_y = boxes[i + 1][1]
        ax.arrow(x, y - box_height / 2, 0, next_y - y + box_height,
                 head_width=0.3, head_length=0.2, fc='black', ec='black')

# Add title
plt.title("", fontsize=12, fontweight='bold')

# Save and show the diagram
plt.tight_layout()
plt.savefig('flow_diagram.png')
plt.show()
