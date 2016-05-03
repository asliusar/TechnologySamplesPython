from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class Role(DeclarativeBase):
    __tablename__ = 'roles'

    id = Column(Integer, Sequence('roles_id_seq'), primary_key=True)
    name = Column(String(128), name='role_name')

    def __repr__(self):
        return '<Role(name=%s)>' % (self.name)
