from signLanguage.logger import logging

from signLanguage.exception import SignException


#logging.info("Welcome to the Project")

try:
    a =7 / '9'

except Exception as e:
    raise SignException(r, sys) from e