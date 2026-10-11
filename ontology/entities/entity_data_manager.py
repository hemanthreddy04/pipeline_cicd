def get_entity_dataframe(spark, entity: dict):
    """
    Read actual data for an entity from its source table.
    """

    catalog = entity["source"]["catalog"]
    schema = entity["source"]["schema"]
    table = entity["source"]["table"]

    return spark.table(f"{catalog}.{schema}.{table}")