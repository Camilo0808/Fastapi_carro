from pydantic import BaseModel, validator
from typing import Optional, List

class CarroModel(BaseModel):
    Cor: Optional[str]
    Marca: Optional[str]
    Modelo: Optional[str]

class idModel(BaseModel):
    id: str