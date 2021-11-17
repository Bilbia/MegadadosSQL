import os 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Column
from sqlalchemy import ForeignKey
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import Session
from sqlalchemy import desc

from . import models, schemas


def get_disciplina(db: Session, nome: str):
    return db.query(models.Disciplina).filter(models.Disciplina.nome == nome).first()


def get_disciplinas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Disciplina).offset(skip).limit(limit).all()


def create_disciplina(db: Session, disc: schemas.Disciplina):
    disciplina = models.Disciplina(nome= disc.nome, professor= disc.professor, anotacao= disc.anotacao)
    db.add(disciplina)
    db.commit()
    db.refresh(disciplina)
    return disciplina


def update_disciplina(db: Session, nome: str, disc: schemas.Disciplina):
    db.query(models.Disciplina).filter(models.Disciplina.nome == nome).update({models.Disciplina.nome: disc.nome, models.Disciplina.professor: disc.professor, models.Disciplina.anotacoes: disc.anotacao})
    db.commit()
    return models.Disciplina(nome= nome, professor= disc.professor, anotacao= disc.anotacao)

def delete_disciplina(db: Session, nome: str):
    db.query(models.Disciplina).filter(models.Disciplina.nome == nome).delete()
    db.commit()
    return 1

def get_nota(db: Session, idNota: int):
    return db.query(models.Nota).filter(models.Nota.nota_id == idNota).first()

def get_notas(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Nota).offset(skip).limit(limit).all()
    
def get_notas_disciplina(db: Session, discNome: str):
    return db.query(models.Nota).filter(models.Nota.disc_nome == discNome).all()

def create_nota(db: Session, nota: schemas.Nota):
    new_nota = models.Nota(disc_nome = nota.disc_nome, nota = nota.nota, entrega = nota.entrega)
    db.add(new_nota)
    db.commit()
    return(new_nota)

def update_nota(db: Session, idNota: int, nota:schemas.Nota):
    db.query(models.Nota).filter(models.Nota.nota_id == idNota).update({models.Nota.disc_nome: nota.disc_nome, models.Nota.nota: nota.nota, models.Nota.entrega: nota.entrega})
    db.commit()
    return 1

def delete_nota(db: Session, idNota: int):
    db.query(models.Nota).filter(models.Nota.nota_id == idNota).delete()
    db.commit()
    return 1