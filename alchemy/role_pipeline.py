from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from alchemy.models import *


class RolePipeline(object):

    def __init__(self):
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine, expire_on_commit=False)

    def save(self, item):

        session = self.Session()
        role = Role(**item)
        try:
            session.add(role)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.expunge_all()
            session.close()

        return role

    def update(self, item):
        session = self.Session()
        role = Role(**item)

        try:
            role = session.query(Role).filter_by(id=role.id).update({'name' : role.name})

            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.expunge_all()
            session.close()

        return role

    def get_all(self):
        session = self.Session()

        return session.query(Role).all()

    def delete(self, role_id):
        session = self.Session()

        try:
            result = session.query(Role).filter_by(id=role_id).delete()
            session.commit()
            return result
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def find_by_name(self, name):
        session = self.Session()
        return session.query(Role).from_statement(
            text("SELECT * FROM roles WHERE role_name=:name")).params(name=name).all()