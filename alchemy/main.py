# from sqlalchemy import create_engine
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
#
# DeclarativeBase = declarative_base()
#
# engine = create_engine('postgresql://postgres:root@localhost:5432/test')
#
# connection = engine.connect()
# connection = connection.execution_options(
#     isolation_level="READ COMMITTED"
# )
#


import alchemy.role_pipeline as role_pipeline
import alchemy.model.role as role
pipeline = role_pipeline.RolePipeline()
print(pipeline.get_all())
print(pipeline.find_by_name('TEST'))
print(pipeline.update({'name' : 'TEST1', 'id' : '1'}))
print(pipeline.delete(1))
print(pipeline.save({'name' : 'TEST1'}))
print(pipeline.get_all())