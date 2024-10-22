from validations.name_validation import run_baby_name_validation

def run_combined_validation(context):

    # Run validations
    name_batch_request, name_expectation_suite_name = run_baby_name_validation(context)

    # Return batch requests for the above
    # to-do - dynamically parse from validations folder
    return [
        (name_batch_request, name_expectation_suite_name)
    ]
