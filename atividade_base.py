from pydantic import BaseModel


class AtividadeBase(BaseModel):
    id: int
    tarefa: str
    tempo: str
    tempoRestante: str
    selecionado: bool
    completado: bool
