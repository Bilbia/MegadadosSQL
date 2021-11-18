from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

try:
    accountFile = open("account.txt", "r")
    LOGIN = accountFile.readline().rstrip("\n")
    PASSWORD = accountFile.readline().rstrip("\n")
    accountFile.close()
except:
    print("Erro ao tentar ler arquivo de conta do MYSQL. Checar formatação e se o arquivo 'account.txt' está presente.")
    exit(1)

print(f"Credentials found: {LOGIN=},{PASSWORD=}")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{LOGIN}:{PASSWORD}@localhost/projetoSQL"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()