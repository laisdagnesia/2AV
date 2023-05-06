from fastapi import FastAPI
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from models import Produto
from fastapi import Path, Query
from typing import List


app = FastAPI(
    title='Segunda AV',
    description='API da segunda avaliação',
    version='1.0'
)

produtos = {
    1:{
        'titulo': 'Batata-Frita',
        'valor': 5
    },
    2:{
        'titulo': 'Hamburger',
        'valor': 10
    },
    3:{
        'titulo':'Refrigerante',
        'valor': 8
    }
}

@app.get('/produtos')
async def get_produtos():
    return produtos

#PATH PARAMETERS

@app.get('/produtos/{produto_id}')
async def get_produtos(
    produto_id: int = Path(gt=0,lt=3)):
    try:
        produto = produtos[produto_id]
        return produto
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Produto não existe')
    
    #QUERY PARAMETER

@app.get('/somarProdutos')
def somar(hamburger:int=Query(default=None,gt=0),batata:int=Query(default=None,gt=0),refrigerante:int=Query(default=None,gt=0)):
    return hamburger+batata+refrigerante
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app:app', host="0.0.0.0", port=8000, reload=True)
