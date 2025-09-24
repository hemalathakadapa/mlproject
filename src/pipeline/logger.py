import logging
import os
from datetime import datetime

# Create logs directory if it doesn’t exist
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

# Generate a unique log file with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
