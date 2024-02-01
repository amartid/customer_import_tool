# main_script.py
import initialize # needs it for logging
from configs import headers,base_url
from dto.jobs_dto import JobsDTO
from dto.candidate_dto import CandidateDTO
from dto.candidate_response_dto import CandidateResponseDTO
import random
import time
import logging
import csv
import json
import requests
import random
from pathlib import Path

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
    current_time = int(time.time())
    random.seed(current_time)
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


def import_candidate(candidates_data, headers):
    responses = []
    
    # importing shortcode in the POST url
    url = f'{base_url}jobs/{candidates_data.job["shortcode"]}/candidates'
    print("Importing candidate ", {candidates_data.name})
    candidate_json = candidates_data.to_json()
    
    while True:
        # Set response parameters
        response = requests.post(url, candidate_json, headers=headers)
        # Check response status
        if response.status_code == 201:

            # Response as JSON
            response_json = json.loads(response.text)
            logging.info(json.dumps(response_json, indent=4))
            
            # Convert JSON response to DTO object
            candidate_response = CandidateResponseDTO.from_json(response_json)
            # Add response to the list of responses
            responses.append(candidate_response)
            
            # Print response details
            # print(json.dumps(response_json, indent=4))
            print(f'Candidate ID: {candidate_response.id}')
            print(f'Candidate Name: {candidate_response.name}')
            print(f'Candidate Imported successfully!')
            logging.info('Candidate ID: %s', candidate_response.id)
            logging.info('Candidate Name: %s', candidate_response.name)
            logging.info(f'Candidate {candidates_data.name} imported successfully!')
            logging.info('Response: %s', candidate_response.to_json)
            break  # Exit the loop since the candidate is imported successfully
        elif response.status_code == 429:  # Rate limit exceeded
            remaining_time = int(response.headers.get('Retry-After', '10'))  # Default to 10 seconds
            print(f"Rate limit exceeded. Retrying in {remaining_time} seconds...")
            time.sleep(remaining_time)
        else:
            logging.error(f'Failed to import candidate {candidates_data.name}.')
            print(f'Failed to import candidate {candidates_data.name}.')
            print('Response:', response.text)
            logging.error('Response: %s', response.text)
            print('Response status:', response.status_code)
            logging.error('Response status: %d', response.status_code)
            # Break the loop since the request failed and there's no need to retry
            break

    return responses


import time

def import_candidate_to_pool(candidates_data, headers):
    responsespool = []
    # importing shortcode in the POST url
    if candidates_data.sourced:
        stage = "Applied"
    else:
        stage = "Sourced"
    url = f'{base_url}talent_pool/{stage}/candidates'
    print(url)
    print("Importing candidate ", {candidates_data.name})
    
    payload = candidates_data.to_json()

    while True:
        # Make the POST request
        response = requests.post(url, payload, headers=headers)

        if response.status_code == 201:  # Successful candidate import
            response_json = json.loads(response.text)
            candidate_response = CandidateResponseDTO.from_json(response_json)
            responsespool.append(candidate_response)
            # Print response details
            # print(json.dumps(response_json, indent=4))
            print(f'Candidate ID: {candidate_response.id}')
            print(f'Candidate Name: {candidate_response.name}')
            print(f'Candidate Imported successfully!')
            logging.info('Candidate ID: %s', candidate_response.id)
            logging.info('Candidate Name: %s', candidate_response.name)
            logging.info(f'Candidate {candidates_data.name} imported successfully!')
            logging.info('Response: %s', candidate_response.to_json)
            break  # Exit the loop since the candidate is imported successfully
        elif response.status_code == 429 or response.status_code == 503:  # Rate limit exceeded or Service Unavailable
            retry_after = int(response.headers.get('Retry-After', '10'))  # Default to 10 seconds
            print(f"Rate limit exceeded or Service Unavailable. Retrying in {retry_after} seconds...")
            time.sleep(retry_after)
        else:  # Other error status codes
            print(f'Failed to import candidate {candidates_data.name}.')
            print('Response status:', response.status_code)
            break  # Exit the loop since there's no need to retry for other error codes

    return responsespool




# Get request based on {id}
def get_candidate_info(base_url, id, headers):
    url = f'{base_url}candidates/{id}'  # url = f'{base_url}{shortcode}/candidates/{id}'
    logging.info("URL: %s", url)
    try:
        # Send the GET request
        response = requests.get(url, headers=headers)
        
        # Check the response status code
        if response.status_code == 200:
            logging.info(response.text)
            print("Response:")
            print(response.text)
        else:
            print(f"Error: {response.status_code} - {response.reason}")
            logging.error("Error: %d - %s", response.status_code, response.reason)
    except requests.exceptions.RequestException as e:
        logging.error("Error: %s", e)

search_candidate_by_id = lambda responses, id: next((response.__dict__ for response in responses if response.id == id), None)

# Main function
def main():
    
    logging.info('Script started')

    # Read CSV file and process data
    file_path = Path('project/customer_import.csv')
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
    logging.info('Creating job objects from given data')
    for job in jobs:
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

    logging.info('Creating candidate objects from given data')
    # Print the CandidateDTO objects
    for candidate in candidates: # Print object attributes as dictionary
        logging.info(f"Candidate: {candidate.name}")

    # at this point i have objects of this requested form:

    # {
    #         "name": "John Doe",
    #         "email": "jdo_john.doe@email810.com",
    #         "phone": "123-456-7890",
    #         "address": "123 Main St, Anytown, CA, United States, 12345",
    #         "job": {
    #             "shortcode": "F8D1EA3849",
    #             "title": "Data Architect"
    #         },
    #         "domain": "Employee referral",
    #         "disqualified": false,
    #         "sourced": false
    #     }

    # i can send the objects in JSON form for both post requests
        
    # Prompt the user to select the endpoint
    print("\nSelect an endpoint to send a POST request:")
    print("\n1. /jobs/{shortcode}/candidates")
    print("\n2. /talent_pool/{stage}/candidates")

    choice = input("\nEnter your choice (1 or 2): ")

    responses = []  # Declare and initialize the responses list before using it

    if choice == '1':
        print("\nImporting candidates by POST in Candidates endpoint ...")
        for candidate in candidates:
            responses += import_candidate(candidate, headers)  # Use += to append the responses

    elif choice == '2':
        print("\nImporting candidates by POST in talent_pool endpoint ...")
        for candidate in candidates:
            responses += import_candidate_to_pool(candidate, headers)
    else:
        print("Invalid choice. Please select either 1 or 2.")

    # Prompt the user to perform a GET request
    print("\nDo you want to perform a GET request?")
    print("\n1. Yes")
    print("\n2. No")

    get_choice = input("\nEnter your choice (1 or 2): ")

    if get_choice == '1':
        
        print("\nExecuting GET request...")
        logging.info("Executing GET request...")
        # Iterate through the list of responses
        logging.info(responses)
        for index, response in enumerate(responses, start=1):
            id = response.id
            name = response.name
            try:
                if response.job:
                    job_shortcode = response.job['shortcode'] if response.job else "N/A"
                    print(f"{index}. Name: {name}, ID: {id}, Job Shortcode: {job_shortcode}")
                    logging.info(f"{index}. Name: {name}, ID: {id}, Job Shortcode: {job_shortcode}")
                else:
                    print(f"{index}. Name: {name}, ID: {id}")
                    logging.info(f"{index}. Name: {name}, ID: {id}")
            except Exception as e:
                print(f"Error processing response {index}: {str(e)}")
                logging.error(f"Error processing response {index}: {str(e)}")

        
        # Ask the user to input a number corresponding to a candidate
        selected_number = input("\nEnter the number corresponding to your choice: ")

        # Validate the user input and retrieve the selected candidate details
        try:
            selected_index = int(selected_number)
            if 1 <= selected_index <= len(responses):
                selected_candidate = responses[selected_index - 1]
                selected_id = selected_candidate.id
                # selected_shortcode = selected_candidate.job['shortcode']
                print(f"\nYou selected Candidate {selected_index}. ID: {selected_id}")
                logging.info(f"You selected Candidate {selected_index}. ID: {selected_id}")
            else:
                print("\nInvalid input: Please enter a number within the given range.")
                logging.error("Invalid input: Please enter a number within the given range.")
        except ValueError:
            print("\nInvalid input: Please enter a valid number.")
            logging.error("Invalid input: Please enter a valid number.")

        # id = selected_id
        # shortcode = selected_shortcode

        print("\nChoose an option:")
        print("\n1. Perform a GET request using the API")
        print("\n2. Print candidate data locally")
        choice = input("\nEnter your choice (1 or 2): ")

        if choice == '1':
            get_candidate_info(base_url, selected_id, headers)
        elif choice == '2':
            candidate_data = search_candidate_by_id(responses, selected_id)
            logging.info(candidate_data)
            print(candidate_data)
        else:
            print("Invalid choice. Please enter 1 or 2.")
            logging.error("Invalid choice. Please enter 1 or 2.")

    elif get_choice == '2':
        print("\nNo GET request executed.")
        logging.info("No GET request executed.")
    else:
        print("\nInvalid choice. Please select either 1 or 2.")
        logging.error("Invalid choice. Please select either 1 or 2.")

    input("Press enter to exit...")

if __name__ == "__main__":
    main()