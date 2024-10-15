from great_expectations.core.batch import BatchRequest
import re

def run_validation(context):
    # Create an Expectation Suite
    expectation_suite_name = "postcode_format"
    context.create_expectation_suite(expectation_suite_name, overwrite_existing=True)

    # Build a BatchRequest for your table in PostgreSQL
    batch_request = BatchRequest(
        datasource_name="pg_datasource",
        data_connector_name="default_inferred_data_connector_name",
        data_asset_name="public.postcode_directory_edinburgh",  # Schema + table name
        limit=10000,  # Optional: limit the number of rows retrieved
    )

    # Create a Validator and load the batch for validation
    validator = context.get_validator(batch_request=batch_request, expectation_suite_name=expectation_suite_name)


    UK_POSTCODE_REGEX = r"^(GIR 0AA|(?:[A-Z]{1,2}[0-9][0-9]?[A-Z]?) ?[0-9][A-Z]{2})$"

    # Add validations
    validator.expect_column_values_to_match_regex("pcd", UK_POSTCODE_REGEX)
    
    # You can add more expectations here
    # For example:
    # validator.expect_column_values_to_not_be_null("timestamp")
    # validator.expect_column_values_to_be_between("efficiency", min_value=0, max_value=100)

    # Save the expectation suite
    validator.save_expectation_suite(discard_failed_expectations=False)

    return batch_request, expectation_suite_name