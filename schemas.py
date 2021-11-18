from typing import List, Optional

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