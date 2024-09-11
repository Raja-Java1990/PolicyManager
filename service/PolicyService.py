from datetime import datetime
from util.constant import POLICY_TYPES as policyTypeConstant


def validateInputDate(dateValue: str):
    # convert input date string into datetime object
    input_date = datetime.strptime(dateValue, "%Y-%m-%d").date()
    print(input_date)
    # get the current date
    current_date = datetime.now().date()
    print(current_date)

    if input_date < current_date:
        raise ValueError(" Validation failed : Policy start date should be on or after current date")


def validateInputpolicyType(policyValue: str):
    found = False
    for item in policyTypeConstant.values():
        if policyValue.lower() in item.lower():
            found = True
            break

    if not found:
        raise ValueError("Validate failed: Policy Type is incorrect")
