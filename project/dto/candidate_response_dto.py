class CandidateResponseDTO:
    def __init__(self, id, name, firstname, lastname, headline, image_url, account, job, stage,
                 disqualified, disqualified_at, disqualification_reason, hired_at, sourced,
                 profile_url, address, phone, email, outbound_mailbox, domain, uploader_id,
                 created_at, updated_at, cover_letter, summary, education_entries, experience_entries,
                 skills, answers, resume_url, tags, location, originating_candidate_id):
        self.id = id
        self.name = name
        self.firstname = firstname
        self.lastname = lastname
        self.headline = headline
        self.image_url = image_url
        self.account = account
        self.job = job
        self.stage = stage
        self.disqualified = disqualified
        self.disqualified_at = disqualified_at
        self.disqualification_reason = disqualification_reason
        self.hired_at = hired_at
        self.sourced = sourced
        self.profile_url = profile_url
        self.address = address
        self.phone = phone
        self.email = email
        self.outbound_mailbox = outbound_mailbox
        self.domain = domain
        self.uploader_id = uploader_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.cover_letter = cover_letter
        self.summary = summary
        self.education_entries = education_entries
        self.experience_entries = experience_entries
        self.skills = skills
        self.answers = answers
        self.resume_url = resume_url
        self.tags = tags
        self.location = location
        self.originating_candidate_id = originating_candidate_id

    @classmethod
    def from_json(cls, data):
        candidate_data = data.get('candidate', {})
        return cls(
            id=candidate_data.get('id'),
            name=candidate_data.get('name'),
            firstname=candidate_data.get('firstname'),
            lastname=candidate_data.get('lastname'),
            headline=candidate_data.get('headline'),
            image_url=candidate_data.get('image_url'),
            account=candidate_data.get('account'),
            job=candidate_data.get('job'),
            stage=candidate_data.get('stage'),
            disqualified=candidate_data.get('disqualified'),
            disqualified_at=candidate_data.get('disqualified_at'),
            disqualification_reason=candidate_data.get('disqualification_reason'),
            hired_at=candidate_data.get('hired_at'),
            sourced=candidate_data.get('sourced'),
            profile_url=candidate_data.get('profile_url'),
            address=candidate_data.get('address'),
            phone=candidate_data.get('phone'),
            email=candidate_data.get('email'),
            outbound_mailbox=candidate_data.get('outbound_mailbox'),
            domain=candidate_data.get('domain'),
            uploader_id=candidate_data.get('uploader_id'),
            created_at=candidate_data.get('created_at'),
            updated_at=candidate_data.get('updated_at'),
            cover_letter=candidate_data.get('cover_letter'),
            summary=candidate_data.get('summary'),
            education_entries=candidate_data.get('education_entries'),
            experience_entries=candidate_data.get('experience_entries'),
            skills=candidate_data.get('skills'),
            answers=candidate_data.get('answers'),
            resume_url=candidate_data.get('resume_url'),
            tags=candidate_data.get('tags'),
            location=candidate_data.get('location'),
            originating_candidate_id=candidate_data.get('originating_candidate_id')
        )
