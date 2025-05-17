import logging
from logging.handlers import RotatingFileHandler
import os

# Ensure logs directory exists
LOG_FILE = os.path.join("logs", "app.log")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Create a logger
logger = logging.getLogger("CyberRiskAnalyzer")
logger.setLevel(logging.DEBUG)  # Log everything from DEBUG level and above

# Define formatter for logs
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Console handler for output to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Console logs INFO and above
console_handler.setFormatter(formatter)

# Rotating file handler for logging to file with rotation
file_handler = RotatingFileHandler(
    LOG_FILE, maxBytes=5*1024*1024, backupCount=3
)
file_handler.setLevel(logging.DEBUG)  # File logs DEBUG and above
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Helper functions to log at various levels

def log_debug(message: str):
    logger.debug(message)

def log_info(message: str):
    logger.info(message)

def log_warning(message: str):
    logger.warning(message)

def log_error(message: str):
    logger.error(message)

def log_critical(message: str):
    logger.critical(message)
