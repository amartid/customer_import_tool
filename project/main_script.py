# main_script.py
import csv
import initialize
import logging

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
# 
# Process each row of data
def process_data(data):
    for row in data:
        try:
            # Process each row of data here
            # For demonstration, just printing the row
            print(row)
            logging.info(f"Processed row: {row}")
        except Exception as e:
            logging.error(f"Error processing row: {row}. Error: {e}")

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
