import os
import sys
import logging

# Define the logging format with placeholders for timestamp, log level, module name, and message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory where the log files will be stored
log_dir = "logs"
# Create the full path to the log file
log_filepath = os.path.join(log_dir, "logging.log")
# Ensure the log directory exists, create it if it doesn't
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO, # setting the logging level to INFO
    format=logging_str, # setting the logging format
    handlers=[
        logging.FileHandler(log_filepath), # logging to a file
        logging.StreamHandler(sys.stdout), # logging to the console
    ]
)

# Create a logger instance with a custom name
logger = logging.getLogger("previsorlogger")