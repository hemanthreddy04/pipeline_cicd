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


def get_kpis(ontology: dict) -> list:
    """
    Return all KPIs.
    """
    return ontology.get("kpis", [])


def get_kpi_by_name(
    ontology: dict,
    kpi_name: str
) -> dict:
    """
    Return a specific KPI.
    """
    for kpi in ontology.get("kpis", []):
        if kpi["name"] == kpi_name:
            return kpi

    return None