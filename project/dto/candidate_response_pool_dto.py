class CandidateResponsePoolDTO:

    def __init__(self, response):
        self.status = response['status']
        
        candidate = response['candidate']
        self.candidate_id = candidate['id']
        self.candidate_name = candidate['name']
        self.firstname = candidate['firstname']
        self.lastname = candidate['lastname']
        self.headline = candidate['headline']
        self.image_url = candidate['image_url']
        self.account = candidate['account']
        self.talent_pool = candidate['talent_pool']
        self.stage = candidate['stage']
        self.disqualified = candidate['disqualified']
        self.disqualified_at = candidate['disqualified_at']
        self.disqualification_reason = candidate['disqualification_reason']
        self.hired_at = candidate['hired_at']
        self.sourced = candidate['sourced']
        self.profile_url = candidate['profile_url']
        self.address = candidate['address']
        self.phone = candidate['phone']
        self.email = candidate['email']
        self.outbound_mailbox = candidate['outbound_mailbox']
        self.domain = candidate['domain']
        self.uploader_id = candidate['uploader_id']
        self.created_at = candidate['created_at']
        self.updated_at = candidate['updated_at']
        self.cover_letter = candidate['cover_letter']
        self.summary = candidate['summary']
        self.education_entries = candidate['education_entries']
        self.experience_entries = candidate['experience_entries']
        self.skills = candidate['skills']
        self.answers = candidate['answers']
        self.resume_url = candidate['resume_url']
        self.tags = candidate['tags']
        self.location = candidate['location']
        self.job = candidate.get('job')  # Setting job attribute or None if it doesn't exist

    @classmethod
    def from_json(cls, data):
        candidate_data = data.get('candidate', {})
        return cls(
            response={
                'status': data.get('status'),
                'candidate': {
                    'id': candidate_data.get('id'),
                    'name': candidate_data.get('name'),
                    'firstname': candidate_data.get('firstname'),
                    'lastname': candidate_data.get('lastname'),
                    'headline': candidate_data.get('headline'),
                    'image_url': candidate_data.get('image_url'),
                    'account': candidate_data.get('account'),
                    'talent_pool': candidate_data.get('talent_pool'),
                    'stage': candidate_data.get('stage'),
                    'disqualified': candidate_data.get('disqualified'),
                    'disqualified_at': candidate_data.get('disqualified_at'),
                    'disqualification_reason': candidate_data.get('disqualification_reason'),
                    'hired_at': candidate_data.get('hired_at'),
                    'sourced': candidate_data.get('sourced'),
                    'profile_url': candidate_data.get('profile_url'),
                    'address': candidate_data.get('address'),
                    'phone': candidate_data.get('phone'),
                    'email': candidate_data.get('email'),
                    'outbound_mailbox': candidate_data.get('outbound_mailbox'),
                    'domain': candidate_data.get('domain'),
                    'uploader_id': candidate_data.get('uploader_id'),
                    'created_at': candidate_data.get('created_at'),
                    'updated_at': candidate_data.get('updated_at'),
                    'cover_letter': candidate_data.get('cover_letter'),
                    'summary': candidate_data.get('summary'),
                    'education_entries': candidate_data.get('education_entries'),
                    'experience_entries': candidate_data.get('experience_entries'),
                    'skills': candidate_data.get('skills'),
                    'answers': candidate_data.get('answers'),
                    'resume_url': candidate_data.get('resume_url'),
                    'tags': candidate_data.get('tags'),
                    'location': candidate_data.get('location'),
                    'originating_candidate_id': candidate_data.get('originating_candidate_id')
                }
            }
        )
