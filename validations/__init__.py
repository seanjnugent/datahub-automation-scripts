# validations/__init__.py

from .postcode_validation import run_postcode_validation
from .solar_validation import run_solar_validation
from ..validation_suite import run_combined_validation

# You can now access these functions via the validations module
