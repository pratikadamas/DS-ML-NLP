import matplotlib.pyplot as plt

class KDNode:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def build_kd_tree(points, depth=0):
    if not points:
        return None

    k = len(points[0])  # Dimension
    axis = depth % k

    points.sort(key=lambda x: x[axis])
    median = len(points) // 2

    return KDNode(
        point=points[median],
        left=build_kd_tree(points[:median], depth + 1),
        right=build_kd_tree(points[median + 1:], depth + 1)
    )

def draw_kd_tree(node, depth=0, bounds=[0, 20, 0, 20], ax=None):
    if not node:
        return

    x, y = node.point
    axis = depth % 2

    if axis == 0:
        # Vertical split (x)
        ax.plot([x, x], [bounds[2], bounds[3]], color='red', linestyle='--')
        draw_kd_tree(node.left, depth + 1, [bounds[0], x, bounds[2], bounds[3]], ax)
        draw_kd_tree(node.right, depth + 1, [x, bounds[1], bounds[2], bounds[3]], ax)
    else:
        # Horizontal split (y)
        ax.plot([bounds[0], bounds[1]], [y, y], color='blue', linestyle='--')
        draw_kd_tree(node.left, depth + 1, [bounds[0], bounds[1], bounds[2], y], ax)
        draw_kd_tree(node.right, depth + 1, [bounds[0], bounds[1], y, bounds[3]], ax)

    # Plot the point
    ax.plot(x, y, 'ko')
    ax.text(x + 0.3, y + 0.3, f"{node.point}")

# Example usage
points = [(3, 6), (17, 15), (13, 15), (6, 12), (9, 1), (2, 7), (10, 19)]
kd_tree = build_kd_tree(points)

# Plot
fig, ax = plt.subplots()
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_title("k-d Tree 2D Space Partitioning")

draw_kd_tree(kd_tree, ax=ax)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()



