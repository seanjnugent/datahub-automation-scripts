from great_expectations.core.batch import BatchRequest

def run_postcode_validation(context):
    # Expectation declaration
    expectation_suite_name = "postcode_format"
    context.create_expectation_suite(expectation_suite_name, overwrite_existing=True)

    # Build a BatchRequest for table in PostgreSQL
    batch_request = BatchRequest(
        datasource_name="pg_datasource",
        data_connector_name="default_inferred_data_connector_name",
        data_asset_name="public.postcode_directory_edinburgh",  # Schema + table name
        limit=10000,  # limit the number of rows retrieved
    )

    # create validator and load the batch
    validator = context.get_validator(batch_request=batch_request, expectation_suite_name=expectation_suite_name)

    # UK postcode regex pattern
    UK_POSTCODE_REGEX = r"^(GIR 0AA|(?:[A-Z]{1,2}[0-9][0-9]?[A-Z]?) ?[0-9][A-Z]{2})$"

    # postcode validation
    validator.expect_column_values_to_match_regex("pcd", UK_POSTCODE_REGEX)

    # save expectation
    validator.save_expectation_suite(discard_failed_expectations=False)

    return batch_request, expectation_suite_name
