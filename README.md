# customer import tool

## Overview

Tool for importing candidate data from CSV into Workable. Features include email modification, Workable API integration, error handling, and Talent Pool support. ctionality to add, edit, and delete person entries. App handles form validation, pagination (5 people per page) and search functionality for the list of people.

## Features

- Imports candidate data from CSV, process the data, keeps only the desired data and imports them as CandidateDTO.
- Name - (Concatenated First Name and Last Name)
- Email - (Generates an email suffix using the first letter oryour name,2 first letters of your surname and the character ‘_’)
- Phone - Phone
- Address - (Concatenated Address, Address 2, City, State, Country, Zip)
- Source - Referred By
- Job Title - Position (it should match exactly with the corresponding one in Workable - Fetch job data from get jobs request to the API. (https://workable.readme.io/reference/jobs) Create JobsDTO object for each job. Returns the job position for the given candidate data if it exists in the provided jobs list.
- Disqualified - Checks if the given candidate data indicates the candidate is disqualified, when Status has the value “Rejected”.
- No email notifications should be sent to candidates during the import process.(if sourced is not inclueded, candidate does receive the “thank you for applying” e-mail.)
- Provide options to import candidates in both endpoints and handles error responses.
- Makes a POST request to the candidate import endpoint, handles retry logic on rate limit errors, and returns a list of response objects.
- post https://{subdomain}.workable.com/spi/v3/jobs/{shortcode}/candidates 
- post https://{subdomain}.workable.com/spi/v3/talent_pool/{stage}/candidates
- imports response data of either one of the endpoints into CandidateResponseDTO for better data manipulation.
- Error Handling and Logging.
- Handles the rate limiting that is applied to Workable API calls according to the limitations on the website.(Recovers response data - X-Rate-Limit-Remaining. (https://workable.readme.io/reference/rate-limits))
- Creates logging and tracks the progress of the data import process.
- Logs successful imports, errors, and any other relevant information.
- After performing POST request it asks to retrieve a candidate's data either by performing a GET request based on id, either based on local data.

### Prerequisites

- Python 3

### Install required packages in virtual environment
- Prepare the Environment: Python installed on your system.
- Run command: pip install requests
- Run: touch requirements.txt
- pip install -r requirements.txt

### Packages used

- csv: Used for reading and writing CSV files.
- json: Required for JSON handling.
- os: Used for operating system related operations.
- random: Utilized for generating random numbers or making random selections.
- pathlib: Used for working with file paths in a more object-oriented way.
- time: Required for time-related functions like delays or timestamps.
- logging: Used for logging messages and tracking program behavior.
- requests: Used for making HTTP requests to APIs. (should be installed)

### Installation

- Place the Python script containing the provided code in your working directory.
- Place the .csv file customer_import.csv in Path('project/customer_import.csv')
- Open a terminal or command prompt.
- Run the script by executing the following command:
- python main_script.py

### Interact with the Tool:

- Follow the prompts provided by the tool in the terminal or command prompt.
- Make selections as instructed to import data from CSV file into data trasfer objects, choose and perform POST and GET requests.
- Provide input as required based on the prompts. (1 or 2 promts for selections, or based on the length of the Candidates in the CSV file.
- Review the output displayed in the terminal or command prompt, and in the log files created.
- After interacting with the tool, you'll be prompted to press enter to exit.