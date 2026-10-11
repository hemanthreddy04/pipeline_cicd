def join_entities(
    left_df,
    right_df,
    relationship: dict
):
    """
    Join two entity DataFrames using ontology relationship.
    """

    left_key = relationship["join"]["from_column"]
    right_key = relationship["join"]["to_column"]

    return left_df.join(
        right_df,
        left_df[left_key] == right_df[right_key],
        "inner"
    )