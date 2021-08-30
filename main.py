import logging
import datetime as dt

today = dt.datetime.today()
filename = f"{today.month:02d}-{today.day:02d}-{today.year:02d}.log" 
 
logging.basicConfig(level=logging.DEBUG)  

logger = logging.getLogger("p_4_Pathak") 

file_handler =logging.FileHandler(filename)
file_handler.setLevel(logging.WARNING)

formatter = logging.Formatter("%(ashtime)s: %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug("this is debuging")
logger.info("this is info") 

logger.error("this is a error") 
logger.warning("this is a basic warning")
logger.critical("this is critical")