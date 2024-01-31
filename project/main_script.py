# main_script.py
import initialize # needs it for logging
from configs import headers,base_url
from dto.jobs_dto import JobsDTO
from dto.candidate_dto import CandidateDTO


import dto.candidate_response
import logging
import csv
import json
import requests
import csv
import random

logging.info('Script started')
# Read CSV file and return a list of dictionaries
def csv_to_dict_list(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
        logging.info('CSV file read successfully.')
        return data
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        return []

# Process each row of data
def process_data(data):
    for row_number, row in enumerate(data, start=1):
        try:
            # Process each row of data here
            logging.info(f"Processed row #{row_number}: {row}")
        except Exception as e:
            logging.error(f"Error processing row #{row_number}: {e}")

def generate_email_suffix(candidate_data):
    first_name = candidate_data['First Name'][0:1].lower()
    last_name = candidate_data['Last Name'][:2].lower()
    email = candidate_data['Email']
    random_integer = str(random.randint(100, 999))  # Generate a random integer between 100 and 999
    # Create the email format
    email_format = f"{first_name}{last_name}_{email[:-4]}{random_integer}{email[-4:]}"
    return email_format

def generate_full_address(candidate_data):
    address = candidate_data['Address']
    address_2 = candidate_data['Address 2']
    city = candidate_data['City']
    state = candidate_data['State']
    country = candidate_data['Country']
    zip_code = candidate_data['Zip']
    # Concatenate the address components
    full_address = ', '.join(filter(None, [address, address_2, city, state, country, zip_code]))
    return full_address

def is_disqualified(candidate_data):
    status = candidate_data['Status']
    # Check if the status is 'Rejected'
    disqualified = True if status == 'Rejected' else False
    return disqualified

def position(candidate_data, jobs):
    candidate_position = candidate_data['Position']
    for job in jobs:
        if candidate_position == job.title:
            return {
                "shortcode": job.shortcode,
                "title": job.title
            }
    return None




# Read CSV file and process data
file_path = 'customer_import.csv'
logging.info('Starting data import...')
print('Starting data import...')

csv_data = csv_to_dict_list(file_path)

if csv_data:
    print('CSV file read successfully.')
    logging.info('CSV file read successfully.')
    print('Importing Candidates Information from CSV file...')
    logging.info('Importing Candidates Information from CSV file...')
    process_data(csv_data)
    print('Data import completed.')
    logging.info('Data import completed.')
else:
    print('Error reading CSV file. Please check the log for details.')
    logging.error('Error reading CSV file. Data import aborted.')




# Fetch job data from get jobs request to the API
res = requests.get(base_url + 'jobs', headers=headers)
job_data = res.json()  # Parse JSON response

# Check if the response is successful
if res.status_code == 200:
    jobs = []
    for job in job_data['jobs']:
        # Create JobsDTO object for each job
        job_dto = JobsDTO(
            job['title'],
            job['shortcode'],
        )
        jobs.append(job_dto)

    # # Print the attributes of JobsDTO objects
    # for job in jobs:
    #     print(vars(job))  # Print object attributes as dictionary
else:
    print("Failed to fetch job data:", res.status_code)

# # Log the list of jobs
# logging.info(f"Jobs: {repr([str(job) for job in jobs])}")
for job in jobs:
    print('Creating job objects')
    logging.info(vars(job))

# Parse the CSV data and create CandidateDTO objects
candidates = []
for candidate_data in csv_data:
    candidate = CandidateDTO(
        candidate_data['First Name'] + ' ' + candidate_data['Last Name'],
        generate_email_suffix(candidate_data),
        candidate_data['Phone'],
        generate_full_address(candidate_data),
        position(candidate_data, jobs),
        candidate_data['Referred By'],
        is_disqualified(candidate_data),
        sourced=False  # Set sourced to False to prevent email notifications THIS MEANS CANDIDATE APPLIED
    )
    candidates.append(candidate)

# Print the CandidateDTO objects

# Print the CandidateDTO objects
for candidate in candidates:
    print('Creating candidate objects from given data')  # Print object attributes as dictionary
    logging.info(f"Candidate: {candidate.name}")


'''
at this point i have objects of this requested form:

{
        "name": "John Doe",
        "email": "jdo_john.doe@email810.com",
        "phone": "123-456-7890",
        "address": "123 Main St, Anytown, CA, United States, 12345",
        "job": {
            "shortcode": "F8D1EA3849",
            "title": "Data Architect"
        },
        "domain": "Employee referral",
        "disqualified": false,
        "sourced": false
    }
'''

responses = []
def import_candidate(candidates_data, headers):
    # importing shortcode in the POST url
    url = f'{base_url}jobs/{candidate.job["shortcode"]}/candidates'
    print("Importing candidate throught POST",{candidate.name})
    candidate_json = candidate.to_json()
    
    # Set response parameteres
    response = requests.post(url, candidate_json, headers=headers)
    
    # Check response status
    if response.status_code == 201:
        print(f'Candidate {candidate.name} imported successfully!')
        logging.info(f'Candidate {candidate.name} imported successfully!')
        
        # Response as JSON
        response_json = json.loads(response.text)
        print(json.dumps(response_json, indent=4))
        
        # # Check Remaining limit
        # remaining_limit = int(response.headers.get('x-rate-limit-remaining', 0)) # If the key 'x-rate-limit-remaining' is not found in the dictionary, the get() method returns the default value, which is 0 in this case.
        # print('Remaining limit:', remaining_limit)
        
        print(response.status_code)
        logging.info('Response status: %d', response.status_code)
        responses.append(response_json)
    else:
        logging.error(f'Failed to import candidate {candidate.name}.')
        print(f'Failed to import candidate {candidate.name}.')
        print('Response:', response.text)
        logging.error('Response: %s', response.text)
        print('Response status:', response.status_code)
        logging.error('Response status: %d', response.status_code)

print("Importing candidates by POST ...")
for candidate in candidates:
    import_candidate(candidates)



# Prompt the user to select the endpoint
print("Select an endpoint to send a POST request:")
print("1. jobs/{shortcode}/candidates")
print("2. /talent_pool/{stage}/candidates")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    shortcode = input("Enter the shortcode: ")
    import_candidate(shortcode)
# elif choice == '2':
#     stage = input("Enter the stage: ")
#     post_to_talent_pool_candidates(stage)
else:
    print("Invalid choice. Please select either 1 or 2.")
        
input("Press Enter to exit...")




# At the end of your script, add the following line to prompt the user to press Enter before closing the terminal window
input("Press Enter to exit...")
