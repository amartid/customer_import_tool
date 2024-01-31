# logging/logging_config.py
import logging

def configure_logging(log_file_path):
    try:
        logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    except FileNotFoundError as e:
        # Log the error to a separate error log file
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f"Error setting up logging: Log file path '{log_file_path}' not found: {e}")
    except PermissionError as e:
        # Log the error to a separate error log file
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f"Error setting up logging: Permission denied for '{log_file_path}': {e}")
    except Exception as e:
        # Log the error to a separate error log file
        error_logger = logging.getLogger('error_logger')
        error_logger.exception("Error setting up logging:")
        # Print a generic error message
        print("An error occurred while setting up logging. Please check the log files for details.")
