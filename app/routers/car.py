from fastapi.responses import JSONResponse
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from database.carro_crud import Carro
from uuid import uuid4
from models.model import CarroModel

router = APIRouter()#iniciando rotas

db_carro = Carro() # instanciando classe com os módulos de CRUD de carros

@router.patch("/alterarCarro/{id}")
def alterar_carro(id: str, data: CarroModel):
    
    db_carro.update_one({'id':id},{"$set":data.__dict__})

    return JSONResponse(
        status_code=200,
        content={"message": "Operação realizada com sucesso!"}
    )

@router.get("/consultarCarro/{id}")
def pegar_carro(id: str):
    
    carro_selecionado = db_carro.find({'id': id})

    return JSONResponse(
        content=jsonable_encoder(carro_selecionado),
        status_code=200
    )

@router.get("/consultarTodos")
def pegar_carro():
        
        exibir_carros = db_carro.find({}) # :0 == False
        
        return JSONResponse(
            content=jsonable_encoder(exibir_carros),
            status_code=200
        )

@router.delete("/deletarCarro/{id}")
def deletar_carro(id: str):
    
    db_carro.delete_one({'id':id})

    return JSONResponse(
        status_code=200,
        content={"message": "Operação realizada com sucesso!"}
    )

@router.post("/criarCarro")
def novoCarro(data: CarroModel):

    carro = data.__dict__
    carro["id"]= str(uuid4())
    db_carro.new(carro)
    
    return JSONResponse(
        status_code=200,
        content={"message": "Carro criado com sucesso!"}
    )