from fastapi import APIRouter

router = APIRouter()

@router.get('/clientes')
def clientes():
    return{"message" : "Lista de Clientes" }