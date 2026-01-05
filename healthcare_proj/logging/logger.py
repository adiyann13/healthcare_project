import os
import logging
from datetime import datetime

def setup_logger(log_level=logging.INFO):
    """
    Sets up a logger with a log folder named after the current date.

    Args:
        log_level: The logging level (default: logging.INFO)

    Returns:
        logger: Configured logger instance
    """
    # Get current date in YYYY-MM-DD format
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_dir, exist_ok=True)

    # Create date-specific subdirectory
    date_dir = os.path.join(logs_dir, current_date)
    os.makedirs(date_dir, exist_ok=True)

    # Create log file path with timestamp
    timestamp = datetime.now().strftime("%H-%M-%S")
    log_file = os.path.join(date_dir, f"log_{timestamp}.log")

    # Configure logging
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        
    )

 


