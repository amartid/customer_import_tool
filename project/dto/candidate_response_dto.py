class CandidateResponseDTO:
    def __init__(self, response):
        # Extract candidate data from the response
        candidate_data = response.get('candidate', {})
        self.id = candidate_data.get('id')
        self.name = candidate_data.get('name')
        self.firstname = candidate_data.get('firstname')
        self.lastname = candidate_data.get('lastname')
        self.headline = candidate_data.get('headline')
        self.image_url = candidate_data.get('image_url')
        self.account = candidate_data.get('account', {})
        self.job = candidate_data.get('job', {})
        self.stage = candidate_data.get('stage')
        self.disqualified = candidate_data.get('disqualified')
        self.disqualified_at = candidate_data.get('disqualified_at')
        self.disqualification_reason = candidate_data.get('disqualification_reason')
        self.hired_at = candidate_data.get('hired_at')
        self.sourced = candidate_data.get('sourced')
        self.profile_url = candidate_data.get('profile_url')
        self.address = candidate_data.get('address')
        self.phone = candidate_data.get('phone')
        self.email = candidate_data.get('email')
        self.outbound_mailbox = candidate_data.get('outbound_mailbox')
        self.domain = candidate_data.get('domain')
        self.uploader_id = candidate_data.get('uploader_id')
        self.created_at = candidate_data.get('created_at')
        self.updated_at = candidate_data.get('updated_at')
        self.cover_letter = candidate_data.get('cover_letter')
        self.summary = candidate_data.get('summary')
        self.education_entries = candidate_data.get('education_entries', [])
        self.experience_entries = candidate_data.get('experience_entries', [])
        self.skills = candidate_data.get('skills', [])
        self.answers = candidate_data.get('answers', [])
        self.resume_url = candidate_data.get('resume_url')
        self.tags = candidate_data.get('tags', [])
        self.location = candidate_data.get('location', {})
        self.originating_candidate_id = candidate_data.get('originating_candidate_id')

        # Additional attributes for the talent pool type of candidate
        self.talent_pool = candidate_data.get('talent_pool', {})

    def to_json(self):
        # Convert the attributes to a JSON-compatible dictionary
        json_data = {
            'id': self.id,
            'name': self.name,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'headline': self.headline,
            'image_url': self.image_url,
            'account': self.account,
            'job': self.job,
            'stage': self.stage,
            'disqualified': self.disqualified,
            'disqualified_at': self.disqualified_at,
            'disqualification_reason': self.disqualification_reason,
            'hired_at': self.hired_at,
            'sourced': self.sourced,
            'profile_url': self.profile_url,
            'address': self.address,
            'phone': self.phone,
            'email': self.email,
            'outbound_mailbox': self.outbound_mailbox,
            'domain': self.domain,
            'uploader_id': self.uploader_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'cover_letter': self.cover_letter,
            'summary': self.summary,
            'education_entries': self.education_entries,
            'experience_entries': self.experience_entries,
            'skills': self.skills,
            'answers': self.answers,
            'resume_url': self.resume_url,
            'tags': self.tags,
            'location': self.location,
            'originating_candidate_id': self.originating_candidate_id,
            'talent_pool': self.talent_pool  # Include talent_pool attribute if present
        }
        return json.dumps(json_data, indent=4)

    @classmethod
    def from_json(cls, data):
        # Create an instance of CandidateResponseDTO using the response data
        return cls(data)


    # @classmethod
    # def from_json(cls, data):
    #     candidate_data = data.get('candidate', {})
    #     return cls(
    #         id=candidate_data.get('id'),
    #         name=candidate_data.get('name'),
    #         firstname=candidate_data.get('firstname'),
    #         lastname=candidate_data.get('lastname'),
    #         headline=candidate_data.get('headline'),
    #         image_url=candidate_data.get('image_url'),
    #         account=candidate_data.get('account'),
    #         job=candidate_data.get('job'),
    #         stage=candidate_data.get('stage'),
    #         disqualified=candidate_data.get('disqualified'),
    #         disqualified_at=candidate_data.get('disqualified_at'),
    #         disqualification_reason=candidate_data.get('disqualification_reason'),
    #         hired_at=candidate_data.get('hired_at'),
    #         sourced=candidate_data.get('sourced'),
    #         profile_url=candidate_data.get('profile_url'),
    #         address=candidate_data.get('address'),
    #         phone=candidate_data.get('phone'),
    #         email=candidate_data.get('email'),
    #         outbound_mailbox=candidate_data.get('outbound_mailbox'),
    #         domain=candidate_data.get('domain'),
    #         uploader_id=candidate_data.get('uploader_id'),
    #         created_at=candidate_data.get('created_at'),
    #         updated_at=candidate_data.get('updated_at'),
    #         cover_letter=candidate_data.get('cover_letter'),
    #         summary=candidate_data.get('summary'),
    #         education_entries=candidate_data.get('education_entries'),
    #         experience_entries=candidate_data.get('experience_entries'),
    #         skills=candidate_data.get('skills'),
    #         answers=candidate_data.get('answers'),
    #         resume_url=candidate_data.get('resume_url'),
    #         tags=candidate_data.get('tags'),
    #         location=candidate_data.get('location'),
    #         originating_candidate_id=candidate_data.get('originating_candidate_id')
    #     )
