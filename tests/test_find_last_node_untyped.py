from bubble_sort import find_last_node_untyped


def test_happy_path():
    nodes = [{"id": 1}, {"id": 2}, {"id": 3}]
    edges = [{"source": 1, "target": 2}, {"source": 2, "target": 3}]
    assert find_last_node_untyped(nodes, edges) == {"id": 3}


def test_no_last_node_cycle():
    nodes = [{"id": 1}, {"id": 2}]
    edges = [{"source": 1, "target": 2}, {"source": 2, "target": 1}]
    assert find_last_node_untyped(nodes, edges) is None


def test_no_last_node_disconnected():
    nodes = [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}]
    edges = [{"source": 1, "target": 2}, {"source": 3, "target": 4}]
    result = find_last_node_untyped(nodes, edges)
    assert result in [{"id": 2}, {"id": 4}]


def test_single_node():
    nodes = [{"id": 1}]
    edges = []
    assert find_last_node_untyped(nodes, edges) == {"id": 1}


def test_empty_graph():
    nodes: list[dict[str, int]] = []
    edges: list[dict[str, int]] = []
    assert find_last_node_untyped(nodes, edges) is None


def test_node_with_no_outgoing_but_incoming():
    nodes = [{"id": 1}, {"id": 2}]
    edges = [{"source": 1, "target": 2}]
    assert find_last_node_untyped(nodes, edges) == {"id": 2}


def test_multiple_nodes_no_outgoing():
    nodes = [{"id": 1}, {"id": 2}, {"id": 3}]
    edges = [{"source": 1, "target": 2}]
    result = find_last_node_untyped(nodes, edges)
    assert result in [{"id": 2}, {"id": 3}]


def test_large_graph_with_last_node():
    num_nodes = 100
    nodes = [{"id": i} for i in range(1, num_nodes + 1)]
    edges = [{"source": i, "target": i + 1} for i in range(1, num_nodes)]
    assert find_last_node_untyped(nodes, edges) == {"id": num_nodes}


def test_large_graph_no_last_node_cycle():
    num_nodes = 100
    nodes = [{"id": i} for i in range(1, num_nodes + 1)]
    edges = [{"source": i, "target": i + 1} for i in range(1, num_nodes)]
    edges.append({"source": num_nodes, "target": 1})
    assert find_last_node_untyped(nodes, edges) is None


def test_large_graph_multiple_ends():
    num_nodes = 100
    nodes = [{"id": i} for i in range(1, num_nodes + 1)]
    edges = []
    # Create a graph where nodes 50 to 100 have no outgoing edges
    for i in range(1, 50):
        edges.append({"source": i, "target": i + 1})

    result = find_last_node_untyped(nodes, edges)
    assert result == {"id": 50}


def test_graph_with_intermediate_node_no_outgoing():
    nodes = [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}]
    edges = [{"source": 1, "target": 2}, {"source": 3, "target": 4}]
    result = find_last_node_untyped(nodes, edges)
    assert result in [{"id": 2}, {"id": 4}]


def test_empty_nodes_with_edges():
    nodes: list[dict[str, int]] = []
    edges = [{"source": 1, "target": 2}]
    assert find_last_node_untyped(nodes, edges) is None


def test_nodes_with_string_ids():
    nodes = [{"id": "a"}, {"id": "b"}, {"id": "c"}]
    edges = [{"source": "a", "target": "b"}, {"source": "b", "target": "c"}]
    assert find_last_node_untyped(nodes, edges) == {"id": "c"}


def test_large_number_of_edges_to_one_node():
    num_nodes = 100
    nodes = [{"id": i} for i in range(1, num_nodes + 1)]
    edges = [{"source": i, "target": num_nodes} for i in range(1, num_nodes)]
    assert find_last_node_untyped(nodes, edges) == {"id": num_nodes}
