# initialize.py
from logs.logging_config import configure_logging

# Set up logging
log_file_path = 'project/logs/customer.log'  # Adjusted log file path
# if path is wrong file will not be created !
configure_logging(log_file_path)