from ontology.query_engine import query_entity


def get_customer_data(
    spark,
    ontology
):
    return query_entity(
        spark,
        ontology,
        "Customer"
    )


def get_customer_metrics(
    spark,
    ontology
):
    return query_entity(
        spark,
        ontology,
        "CustomerMetrics"
    )