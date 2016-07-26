from sqlalchemy import create_engine

def engine():
    """return an sqlalchemy engine"""
    return create_engine('postgres+pg8000://postgres/greetings')