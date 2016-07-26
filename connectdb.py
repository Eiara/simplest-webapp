from sqlalchemy import create_engine

def engine(database):
    """return an sqlalchemy engine"""
    return create_engine('postgresql+pg8000://postgres@postgres/{}'.format(database), pool_size=1)