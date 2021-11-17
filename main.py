#André Rocco e Beatriz Muniz

from typing import Optional, List

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import Null
from . import crud, models, schemas
from .database import SessionLocal, engine


def ja_existe():
    raise HTTPException(status_code=400, detail="Disciplina já existe")
    
def nao_existe():
    raise HTTPException(status_code=400, detail="Disciplina não existe")

def ja_existe_nota():
    raise HTTPException(status_code=400, detail="Nota já existe")

def nao_existe_nota():
    raise HTTPException(status_code=400, detail="Nota não existe")


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# disciplinas = []
# nomes_disciplinas = []
# notas = []


# lista todas as disciplinas
@app.get("/")
def list_disc(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    disciplinas = crud.get_disciplinas(db, skip=skip, limit=limit)
    if disciplinas is None:
        return {"retorno": "Nenhuma disciplina adicionada"}
    else:
        return disciplinas

# mostra detalhes de uma disciplina
@app.get("/{disc_nome}")
def show_disc(disc_nome: str, db: Session = Depends(get_db)):
    disciplina = crud.get_disciplina(db, nome=disc_nome)
    if disciplina:
        return disciplina
    nao_existe()

# cria uma nova disciplina
@app.post("/")
def create_disc(disc: schemas.Disciplina, db: Session = Depends(get_db)):
    disciplina = crud.get_db_disciplina(db, nome=disc.nome)
    if disciplina:
        ja_existe()
    return crud.create_disciplina(db, disc = disciplina)

# atualiza disciplina
@app.put("/{disc_nome}")
def update_disc(disc_nome: str, disc: schemas.Disciplina, db: Session = Depends(get_db)):
    # se voce pretende mudar o nome da disciplina
    if disc_nome != disc.nome:
        disciplina = crud.get_disciplina(db, nome=disc.nome)
        if disciplina:
            ja_existe()
    
    disciplina = crud.get_disciplina(db, nome=disc_nome)
    if disciplina is None: 
        nao_existe()

    return crud.update_disc(db, nome = disc_nome, disc = disc)

# deleta a disciplina
@app.delete("/{disc_nome}")
def delete_disc(disc_nome: schemas.Disciplina.nome, db: Session = Depends(get_db)):
    disciplina = crud.get_db_disciplina(db, nome=disc_nome)
    if disciplina is None:
        nao_existe()
    crud.delete_disciplina(db, nome = disc_nome)
    return {"retorno":f"{disc_nome} apagado(a)"}

# lista as notas das disciplinas
@app.get("/notas/")
def list_nota(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    notas = crud.get_notas(db, skip=skip, limit=limit)
    if notas is None:
        return {"retorno": "Nenhuma nota adicionada"}
    else:
        return notas

# lista as notas de uma disciplina especifica
@app.get("/notas/{disc_nome}")
def list_notas_disciplina(disc_nome: str, db: Session = Depends(get_db)):
    disciplina = crud.get_disciplina(db, nome=disc_nome)
    if disciplina is None:
        nao_existe()
    notas = crud.get_notas_disciplinas(db, discNome = disc_nome)
    if notas is None:
        return {"retorno": "Nenhuma nota adicionada"}
    else:
        return notas

    
# adiciona nota a uma disciplina
@app.post("/notas/")
def create_nota(rnota: schemas.Nota, db: Session = Depends(get_db)):
    disciplina = crud.get_disciplina(db, nome=rnota.disc_nome)
    if disciplina is None:
        nao_existe()
    nota = crud.get_nota(db, idNota = rnota.nota_id)
    if nota is not None:
        ja_existe_nota()
    return crud.create_nota(db, nota=rnota)


# modifica uma nota de uma disciplina
@app.put("/notas/{rnota_id}")
def update_nota(rnota_id: int, rnota: schemas.Nota, db: Session = Depends(get_db)):
    nota = crud.get_nota(db, idNota = rnota.id_nota)
    if nota:
        return crud.update_nota(db, nota=rnota)
    nao_existe_nota()

#deleta uma nota de uma disciplina
@app.delete("/notas/{rnota_id}")
def delete_nota(rnota_id: int, db: Session = Depends(get_db)):
    nota = crud.get_nota(db, idNota = rnota_id)
    if nota:
        crud.delete_nota(db, idNota = rnota_id)
        return {"retorno":f"nota de {nota.disc_nome} apagada"}
    nao_existe_nota()