import json
from typing import Dict, List

# Define the CandidateDTO class
class CandidateDTO:
    def __init__(self, name: str, email: str, phone: str, address: str, job: Dict, domain: str, disqualified: bool, sourced: bool) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.job = job
        self.domain = domain
        self.disqualified = disqualified
        self.sourced = sourced # To prevent email notifications
    
    # Getter method for job
    def get_job(self) -> Dict:
        return self.job

    # Getter method for shortcode
    def get_shortcode(self) -> str:
        if 'shortcode' in self.job:
            return self.job['shortcode']
        else:
            return None
        
    def to_json(self) -> str:
        """
        Convert the CandidateDTO object to JSON format.
        """
        dto_dict = {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "job": {
                "shortcode": self.job['shortcode'],
                "title": self.job['title']
            },
            "domain": self.domain,
            "disqualified": self.disqualified,
            "sourced": self.sourced
        }
        return json.dumps(dto_dict, indent=4)
