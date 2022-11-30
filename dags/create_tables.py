"""Script to create DB tables."""
from dbManager import dbFactory


def main():
    """Program entrypoint."""
    # Logic to create tables goes here.
    # https://docs.sqlalchemy.org/en/14/orm/tutorial.html#create-a-schema
    db = dbFactory('postgresql').get_db()
    db.create_database()
    db.create_model()

    

if __name__ == "__main__":
    main()
