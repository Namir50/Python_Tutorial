import logging
logging.basicConfig(
    filename = 'app.log',
    filemode = 'w',
    level=logging.DEBUG, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt = '%Y -%m- %D %H:%M:%S',
)
