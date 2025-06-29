import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())


def build_sample_tree():
    """
    We create a small tree for demonstration.
    """
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    return root


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_colored_tree(root, visited_order, cmap_name="Blues"):
    """
    Visualizes a tree by coloring the nodes in traversal order.
    """
    G = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(G, root, pos)

    cmap = plt.get_cmap(cmap_name)
    norm_factor = len(visited_order) - 1 if len(visited_order) > 1 else 1

    node_colors = {}
    for i, node in enumerate(visited_order):
        # The further down the traversal order, the lighter the color.
        node_colors[node.id] = cmap(i / norm_factor)

    colors = [node_colors.get(n, "#cccccc") for n in G.nodes()]
    labels = {n: G.nodes[n]["label"] for n in G.nodes()}

    plt.figure(figsize=(8, 5))
    nx.draw(
        G,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2000,
        node_color=colors,
        font_color="white",
        font_weight="bold"
    )
    plt.show()


def dfs_traversal(root):
    """
    DFS traversal using a stack.
    """
    stack = [root]
    visited = []

    while stack:
        node = stack.pop()
        visited.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited


def bfs_traversal(root):
    """
    BFS traversal using a queue.
    """
    queue = deque([root])
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited


tree_root = build_sample_tree()

print("DFS traversal...")
dfs_nodes = dfs_traversal(tree_root)
draw_colored_tree(tree_root, dfs_nodes, cmap_name="Blues")

print("BFS traversal...")
bfs_nodes = bfs_traversal(tree_root)
draw_colored_tree(tree_root, bfs_nodes, cmap_name="Greens")
