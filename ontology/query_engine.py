from ontology.entities.entity_manager import get_entity_by_name
from ontology.entities.entity_data_manager import get_entity_dataframe


def query_entity(
    spark,
    ontology,
    entity_name: str
):
    """
    Fetch data for an entity using ontology.
    """

    entity = get_entity_by_name(
        ontology,
        entity_name
    )

    return get_entity_dataframe(
        spark,
        entity
    )