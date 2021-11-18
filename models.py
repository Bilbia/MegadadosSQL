from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float

from database import Base


class Disciplina(Base):
    __tablename__ = "Disciplina"

    nome = Column(String(45), primary_key=True, index=True)
    professor = Column(String(45), nullable=True)
    anotacao = Column(String(45), nullable=True)

class Nota(Base):
    __tablename__ = "Nota"

    nota_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    disc_nome = Column(String(45), ForeignKey("Disciplina.nome"), nullable=False, index=True)
    nota = Column(Float, index=True)
    entrega = Column(String(45), nullable=True)
