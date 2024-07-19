import logging  # Import the logging module
from logging.handlers import TimedRotatingFileHandler  # Import the TimedRotatingFileHandler class for timed log rotation

logger = None  # Initialize a global logger variable to None


def Logs():
    global logger  # Use the global logger variable

    if logger is None:  # Check if the logger has not been initialized yet
        logger = logging.getLogger(__name__)  # Create a new logger with the name of the current module
        logger.setLevel(logging.DEBUG)  # Set the logging level to DEBUG

        # Create a formatter to format log messages
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

        # Create a timed rotating file handler to write logs to a file
        # The log file will rotate every 30 days, and up to 2 backup files will be kept
        file_handler = TimedRotatingFileHandler(filename='file.log', when='D', interval=30, backupCount=2)
        file_handler.setLevel(logging.DEBUG)  # Set the file handler logging level to DEBUG
        file_handler.setFormatter(formatter)  # Set the formatter for the file handler
        logger.addHandler(file_handler)  # Add the file handler to the logger

    return logger  # Return the initialized logger
