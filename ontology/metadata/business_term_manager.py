def get_business_terms(ontology: dict) -> list:
    """
    Return all business terms.
    """
    return ontology.get("business_terms", [])


def get_business_term_by_name(
    ontology: dict,
    term_name: str
) -> dict:
    """
    Return a specific business term.
    """
    for term in ontology.get("business_terms", []):
        if term["name"] == term_name:
            return term

    return None