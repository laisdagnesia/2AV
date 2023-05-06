from fastapi import APIRouter
router = APIRouter()
@router.get('/produtos')
def listar_produtos():
return {"Produtos": "Lista de Produtos"}