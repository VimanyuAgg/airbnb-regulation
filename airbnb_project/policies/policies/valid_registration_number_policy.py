from ..models.policy_model import Policy
import re

class ValidRegistrationNumberPolicy(Policy):
  def is_valid_registration_number(self, registration_number: str) -> bool:
    if not registration_number:
      return False
    
    valid_registration_pattern = re.compile(r"^[0-9]{2}-[0-9]{6}$")
    START_YEAR = 13
    END_YEAR = 24

    if valid_registration_pattern.match(registration_number):
        registration_year = int(registration_number[0:2])
        if registration_year > END_YEAR or registration_year < START_YEAR:
            return False
        else:
            return True
    else:
        return False
    
  def get_evaluation_result(self, registration_number: str) -> bool:
    return self.is_valid_registration_number(registration_number)