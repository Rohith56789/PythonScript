import logging

logging.basicConfig(
    filename='app.log',
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
# Create named logger
logger = logging.getLogger("rohith")

# Use the named logger
logger.debug('This is a debug message')