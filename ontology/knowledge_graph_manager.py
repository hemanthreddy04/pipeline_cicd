def build_graph(ontology: dict):
    """
    Build graph nodes and edges from ontology.
    """

    nodes = []
    edges = []

    for entity in ontology.get("entities", []):
        nodes.append(entity["name"])

    for relationship in ontology.get("relationships", []):
        edges.append(
            (
                relationship["from_entity"],
                relationship["to_entity"],
                relationship["relationship_type"]
            )
        )

    return nodes, edges