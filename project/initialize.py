# initialize.py
import os
import time
from logs.logging_config import configure_logging
'''
This code initializes logging for the project by creating a timestamped log file.
It first ensures the existence of a directory for log files.
Then, it generates a current timestamp using the time.strftime() function and appends it to the log file name.
Each log file created has a unique name based on the timestamp when the project is run.
Finally, it configures logging using the provided log file path.
'''
# Set up logging with a timestamped log file
log_directory = 'project/logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
log_file_path = os.path.join(log_directory, f'customer_{current_time}.log')  # Unique log file path with timestamp
# if path is wrong file will not be created !
configure_logging(log_file_path)

