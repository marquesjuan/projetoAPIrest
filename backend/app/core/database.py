from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#configurações para o SQLAlchemy:

#salva a url do db
DATABASE_URL = "mysql+pymysql://root:5912@mysql:3306/projetoapi"

#cria conexão com o db
engine = create_engine(DATABASE_URL)

#cria sessão para interagir com o db
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#base para os modelos alchemy
base = declarative_base()

