from great_expectations.core.batch import BatchRequest

def run_baby_name_validation(context):
    # Expectation declaration
    expectation_suite_name = "name_not_numeric"
    context.create_expectation_suite(expectation_suite_name, overwrite_existing=True)

    # Build a BatchRequest for the table in PostgreSQL
    batch_request = BatchRequest(
        datasource_name="pg_datasource",
        data_connector_name="default_inferred_data_connector_name",
        data_asset_name="public.babies_first_names_23_full_lists_girls",  # Schema + table name
        limit=10000,  # Limit the number of rows retrieved
    )

    # Create validator and load the batch
    validator = context.get_validator(batch_request=batch_request, expectation_suite_name=expectation_suite_name)

    # Non-numeric regex pattern (this ensures the value contains non-numeric characters)
    NON_NUMERIC_REGEX = r"^\D+$"  # Matches any string that contains no digits (non-numeric)

    # Validations
    validator.expect_column_values_to_match_regex("name", NON_NUMERIC_REGEX)
    validator.expect_column_values_to_be_between("number", min_value=1, max_value=None)

    # Save expectation suite
    validator.save_expectation_suite(discard_failed_expectations=False)

    return batch_request, expectation_suite_name
