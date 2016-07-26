from sqlalchemy import create_engine

def engine():
    """return an sqlalchemy engine"""
    return create_engine('postgresql+pg8000://postgres@postgres/greetings')