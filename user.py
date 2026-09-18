from datetime import datetime
# Database model will be connected in the next development step.
# For the first frontend version, this file is intentionally simple.

class User:
    def __init__(self, username, password, phone, email=None, address=None):
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.address = address
        self.created_at = datetime.utcnow()
        self.is_active = True
