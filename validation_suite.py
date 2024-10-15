from validations.postcode_validation import run_postcode_validation
from validations.solar_validation import run_solar_validation

def run_combined_validation(context):

    # Run validations
    solar_batch_request, solar_expectation_suite_name = run_solar_validation(context)
    postcode_batch_request, postcode_expectation_suite_name = run_postcode_validation(context)

    # Return batch requests for the above
    # to-do - dynamically parse from validations folder
    return [
        (solar_batch_request, solar_expectation_suite_name),
        (postcode_batch_request, postcode_expectation_suite_name)
    ]
