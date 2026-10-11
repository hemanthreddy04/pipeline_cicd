def get_entities(ontology: dict) -> list:
    return ontology.get("entities", [])


def get_entity_by_name(ontology: dict, entity_name: str) -> dict:
    for entity in ontology.get("entities", []):
        if entity["name"] == entity_name:
            return entity
    return None


def get_entity_attributes(entity: dict) -> list:
    return entity.get("attributes", [])


def get_primary_key(entity: dict) -> str:
    return entity.get("primary_key")


def get_source(entity: dict) -> dict:
    return entity.get("source", {})