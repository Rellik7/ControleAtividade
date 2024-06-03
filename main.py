import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db
from atividade_db import Atividade
from atividade_base import AtividadeBase

app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
async def buscar_atividades(db: db_dependency):
    result = db.query(Atividade).order_by(Atividade.id).all()

    if not result:
        raise HTTPException(status_code=404, detail='Aitividades não encontradas')
    return result


@app.post("/")
async def atualizar_atividade(atividade: AtividadeBase, db: db_dependency):
    db_atividade = Atividade(
        tarefa=atividade.tarefa,
        tempo=atividade.tempo,
        tempoRestante=atividade.tempoRestante,
        selecionado=atividade.selecionado,
        completado=atividade.completado
    )

    atividade_anterior = db.get(Atividade, atividade.id)
    if not atividade_anterior:
        db.add(db_atividade)
    else:
        if atividade.selecionado:
            db.query(Atividade).update({'selecionado': False})
        atividade_anterior.tarefa = atividade.tarefa
        atividade_anterior.tempo = atividade.tempo
        atividade_anterior.tempoRestante = atividade.tempoRestante
        atividade_anterior.selecionado = atividade.selecionado
        atividade_anterior.completado = atividade.completado

    db.commit()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
