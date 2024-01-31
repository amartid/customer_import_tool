# logging/logging_config.py
import logging

def configure_logging(log_file_path):
    try:
        logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    except Exception as e:
        print(f"Error setting up logging: {e}")
