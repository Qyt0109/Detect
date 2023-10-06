from Backend.Database.Components.db_models import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Env.env import db_path, db_engine

# Create an SQLite engine
# echo = True to logging any SQL query to console
engine = create_engine(db_engine + db_path, echo=True)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)
default_session = Session()