from database import Base
from sqlalchemy import Column, Integer, String, Time, Boolean


class Atividade(Base):
    __tablename__ = 'atividade'

    id = Column(Integer, primary_key=True, nullable=False)
    tarefa = Column(String, nullable=False)
    tempo = Column(String, nullable=False)
    tempoRestante = Column(String, nullable=False)
    selecionado = Column(Boolean, nullable=False, default=False)
    completado = Column(Boolean, nullable=False, default=False)
