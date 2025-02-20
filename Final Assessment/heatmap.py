import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import seaborn as sns

# Generate mock traffic congestion data for the heatmap
locations = ["  Intersections", "  Flyovers", "  Roundabouts", "  Major Roads", "  Minor Roads"]
times = ["6 AM", "9 AM", "12 PM", "3 PM", "6 PM", "9 PM"]
congestion_data = np.random.randint(0, 100, size=(len(locations), len(times)))

# Create the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(congestion_data, annot=True, fmt="d", cmap="Reds", xticklabels=times, yticklabels=locations)
plt.title("Traffic Congestion Heatmap", fontsize=14, fontweight='bold')
plt.xlabel("Time of Day", fontsize=12)
plt.ylabel("Locations", fontsize=12)

# Save and display the heatmap
plt.tight_layout()
plt.savefig('heatmap.png')
plt.show()