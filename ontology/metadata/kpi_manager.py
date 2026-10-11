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