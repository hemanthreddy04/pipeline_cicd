def get_relationships(ontology: dict) -> list:
    """
    Return all relationships.
    """
    return ontology.get("relationships", [])


def get_relationship_by_name(
    ontology: dict,
    relationship_name: str
) -> dict:
    """
    Return a specific relationship.
    """
    for relationship in ontology.get("relationships", []):
        if relationship["name"] == relationship_name:
            return relationship

    return None