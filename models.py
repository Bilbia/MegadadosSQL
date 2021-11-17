from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float

from .database import Base


class Disciplina(Base):
    __tablename__ = "disciplina"

    nome = Column(String, primary_key=True, index=True)
    professor = Column(String, nullable=True)
    anotacao = Column(String, nullable=True)

class Nota(Base):
    __tablename__ = "nota"

    nota_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    disc_nome = Column(String, ForeignKey("Disciplina.nome"), nullable=False, index=True)
    nota = Column(Float, index=True)
    entrega = Column(String, nullable=True)
