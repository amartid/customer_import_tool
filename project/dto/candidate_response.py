import json

# Define the CandidateResponseDTO class
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