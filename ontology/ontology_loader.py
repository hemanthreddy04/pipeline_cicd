import yaml

ONTOLOGY_PATH = "/Workspace/Users/hemanthreddy040904@gmail.com/dev.sample_pipeline/ontology/customer_ontology.yaml"

def load_ontology() -> dict:
    with open(ONTOLOGY_PATH, "r") as f:
        ontology = yaml.safe_load(f)

    return ontology