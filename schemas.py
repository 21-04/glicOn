from typing import Optional
from pydantic import BaseModel
import datetime
from fastapi import Body


class Paciente(BaseModel):#serialezer
    user_id:int
    sexo:str
    id_tipo: int
    id_med: int
    #date_create: timezone
    dt_nasc: date
    estado: int
    
    class Config:
        orm_mode=True

class Especialidade(BaseModel):#serialezer
    id:int
    codigo:str
    descricao: str
    estado: int

    class Config:
        orm_mode=True

class Indece_diario(BaseModel):#serialezer
    id:int
    id_pac:int
    indece_glic: str
    aliminetos: str
    estado: int
   
    class Config:
        orm_mode=True

class Comunidade(BaseModel):#serialezer
    id:int
    mensagem:str
    user_id_remetente: str
    user_id_receptor: str
    tipo: str
    estado: str
   
    class Config:
        orm_mode=True

class Receita(BaseModel):#serialezer
    id:int
    descricao:str
    id_med:int
    id_pac:int
    quantidade:int
    estado: str
    estado_ped: str
    
    class Config:
        orm_mode=True

class Medico(BaseModel):#serialezer
    user_id:int
    id_esp:int
    id_estr:int
    estado: str
    
    class Config:
        orm_mode=True

class Tipo(BaseModel):#serialezer
    id:int
    descricao:str
    codigo:str
    estado: str
    
    class Config:
        orm_mode=True

class Estrutura(BaseModel):#serialezer
    id:int
    ilha:str
    concelho:str
    codigo:str
    descricao:str
    estado: int
    
    class Config:
        orm_mode=True