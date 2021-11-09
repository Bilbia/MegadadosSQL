#André Rocco e Beatriz Muniz

from typing import Optional, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Disciplina(BaseModel):
    nome: str
    professor: Optional[str] = None
    anotacao: Optional[str] = None

class Nota(BaseModel):
    nota_id : int
    disc_nome: str
    nota: float
    entrega: Optional[str] = None


def ja_existe():
    raise HTTPException(status_code=400, detail="Disciplina já existe")
    
def nao_existe():
    raise HTTPException(status_code=400, detail="Disciplina não existe")

def ja_existe_nota():
    raise HTTPException(status_code=400, detail="Nota já existe")

def nao_existe_nota():
    raise HTTPException(status_code=400, detail="Nota não existe")


app = FastAPI()

disciplinas = []
nomes_disciplinas = []
notas = []

# lista os nomes de todas as disciplinas
@app.get("/")
def list_disc():
    if not disciplinas:
        return {"retorno": "Nenhuma disciplina adicionada"}
    else:
        return {"Disciplinas": nomes_disciplinas}

# mostra detalhes de uma disciplina
@app.get("/{disc_nome}")
def show_disc(disc_nome: str):
    for disc in disciplinas:
        if disc.nome == disc_nome:
            return disc
    nao_existe()

# cria uma nova disciplina
@app.post("/")
def create_disc(disciplina: Disciplina):
    for disc in disciplinas:
        if disc.nome == disciplina.nome:
            ja_existe()
    disciplinas.append(disciplina)
    nomes_disciplinas.append(disciplina.nome)
    return disciplina

# atualiza disciplina
@app.put("/{disc_nome}")
def update_disc(disc_nome: str, disciplina: Disciplina):
    for disc in disciplinas:
        if disc.nome == disc_nome:
            if disciplina.nome not in nomes_disciplinas:
                nome_index = nomes_disciplinas.index(disc.nome)
                nomes_disciplinas[nome_index] = disciplina.nome
                index = disciplinas.index(disc)
                disciplinas[index] = disciplina
                return disciplina
            else:
                ja_existe()
    nao_existe()

# deleta a disciplina
@app.delete("/{disc_nome}")
def delete_disc(disc_nome: str):
    for disc in disciplinas:
        if disc.nome == disc_nome:
            disciplinas.remove(disc)
            nomes_disciplinas.remove(disc.nome)
            return {"retorno":f"{disc.nome} apagado(a)"}
    nao_existe()

# lista as notas das disciplinas
@app.get("/notas/")
def list_nota():
    if not notas:
        return {"retorno": "Nenhuma nota adicionada"}
    else:
        return notas

# lista as notas de uma disciplina especifica
@app.get("/notas/{disc_nome}")
def list_notas_disciplina(disc_nome: str):
    if not notas:
        return {"retorno": "Nenhuma nota adicionada"}
    else:
        notas_disc = []
        for nota in notas:
            if nota.disc_nome == disc_nome:
                notas_disc.append(nota)
        return notas_disc

    
# adiciona nota a uma disciplina
@app.post("/notas/")
def create_nota(rnota: Nota):
    for nota in notas:
        if nota.nota_id == rnota.nota_id:
            ja_existe_nota()
    notas.append(rnota)
    return rnota


# modifica uma nota de uma disciplina
@app.put("/notas/{rnota_id}")
def update_nota(rnota_id: int, rnota: Nota):
    for nota in notas:
        if nota.nota_id == rnota_id:
            nota_index = notas.index(nota)
            notas[nota_index] = rnota
            return rnota
    nao_existe_nota()

#deleta uma nota de uma disciplina
@app.delete("/notas/{rnota_id}")
def delete_nota(rnota_id: int):
    for nota in notas:
        if nota.nota_id == rnota_id:
            notas.remove(nota)
            return {"retorno":f"nota de {nota.disc_nome} apagada"}
    nao_existe()