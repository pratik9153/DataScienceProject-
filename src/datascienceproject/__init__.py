import os
import logging
import sys

# Logging format
logging_str = "%(asctime)s: %(levelname)s: %(module)s: %(message)s"

# Log directory
logging_dir = "logs"

# Log file path
log_filepath = os.path.join(logging_dir, "logging.log")

# Create logs directory if it doesn't exist
os.makedirs(logging_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create logger
logger = logging.getLogger("MY data science project logs")