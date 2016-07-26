from sqlalchemy import create_engine

def engine():
    """return an sqlalchemy engine"""
    return create_engine('sqlite:///app/test.db')