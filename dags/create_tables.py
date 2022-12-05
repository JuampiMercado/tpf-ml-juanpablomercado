"""Script to create DB tables."""
from dbManager import dbFactory
import logging
logging.basicConfig(level=logging.INFO)

def main():
    """Program entrypoint."""
    # Logic to create tables goes here.
    # https://docs.sqlalchemy.org/en/14/orm/tutorial.html#create-a-schema
    logging.info('Starting model creation...')
    logging.info('Connecting database...')
    db = dbFactory('postgresql').get_db()
    logging.info('Create database if not exists...')
    db.create_database()
    logging.info('Create model...')
    db.create_model()
    logging.info('Operation finished.')

    

if __name__ == "__main__":
    main()
