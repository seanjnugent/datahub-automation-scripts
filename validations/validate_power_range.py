from great_expectations.core.batch import BatchRequest

def run_validation(context):
    # Create an Expectation Suite
    expectation_suite_name = "solar_power_suite"
    context.create_expectation_suite(expectation_suite_name, overwrite_existing=True)

    # Build a BatchRequest for your table in PostgreSQL
    batch_request = BatchRequest(
        datasource_name="pg_datasource",
        data_connector_name="default_inferred_data_connector_name",
        data_asset_name="public.upload_solar_20240726093401",  # Schema + table name
        limit=1000,  # Optional: limit the number of rows retrieved
    )

    # Create a Validator and load the batch for validation
    validator = context.get_validator(batch_request=batch_request, expectation_suite_name=expectation_suite_name)

    # Add validations
    validator.expect_column_values_to_be_between("power", min_value=0, max_value=1000)
    
    # You can add more expectations here
    # For example:
    # validator.expect_column_values_to_not_be_null("timestamp")
    # validator.expect_column_values_to_be_between("efficiency", min_value=0, max_value=100)

    # Save the expectation suite
    validator.save_expectation_suite(discard_failed_expectations=False)

    return batch_request, expectation_suite_name