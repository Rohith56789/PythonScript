import logging

# Create and configure named logger
logger = logging.getLogger("rohith")
logging.basicConfig(level=logging.INFO)

# Log messages using the named logger
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
