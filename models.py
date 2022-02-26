from datetime import datetime
from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text,Date,TIMESTAMP, true

class Paciente(Base):
    __tablename__='glic_paciente'
    user_id=Column(Integer,primary_key=True)
    sexo =Column(String(255),nullable=True)
    id_tipo =Column(Integer,nullable=True)
    id_med =Column(Integer,nullable=True)
    date_create=Column(TIMESTAMP,nullable=True)
    dt_nasc=Column(Date, nullable=True)
    estado =Column(Integer,nullable=True)
    
    def __repr__(self):
       return f"<Paciente sexo={self.sexo} id_tipo={self.id_tipo}>"

class Especialidade(Base):
    __tablename__='glic_especialidade'
    id=Column(Integer,primary_key=True)
    codigo =Column(String(255),nullable=True)
    descricao =Column(String(255),nullable=True)
    estado =Column(Integer,nullable=True)
    

    def __repr__(self):
       return f"<Paciente codigo={self.codigo} descricao={self.descricao}>"

class Indece_diario(Base):
    __tablename__='glic_glicemia'
    id=Column(Integer,primary_key=True)
    id_pac =Column(Integer,nullable=True)
    indece_glic =Column(Integer,nullable=True)
    aliminetos =Column(String(255),nullable=True)
    estado =Column(Integer,nullable=True)
    

    def __repr__(self):
       return f"<Paciente indece_glic={self.indece_glic} descricao={self.aliminetos}>"

class Comunidade(Base):
    __tablename__='glic_mensagem'
    id=Column(Integer,primary_key=True)
    mensagem =Column(String(255),nullable=True)
    user_id_remetente =Column(String(255),nullable=True)
    user_id_receptor =Column(String(255),nullable=True)
    tipo =Column(String(255),nullable=True)
    estado =Column(Integer,nullable=True)
    
    def __repr__(self):
       return f"<Desc mensagem={self.mensagem} tipo={self.tipo}>"


class Receita(Base):
    __tablename__='glic_receita'
    id=Column(Integer,primary_key=True)
    descricao =Column(String(255),nullable=True)
    id_med =Column(Integer,nullable=True)
    id_pac =Column(Integer,nullable=True)
    quantidade =Column(Integer,nullable=True)
    estado =Column(Integer,nullable=True)
    estado_ped =Column(String(255),nullable=True)
  

    def __repr__(self):
       return f"<Medicamento descricao={self.descricao} quantidade={self.quantidade}>"

class Medico(Base):
    __tablename__='glic_medico'
    user_id=Column(Integer,primary_key=True)
    id_esp=Column(Integer,primary_key=True)
    id_estr=Column(Integer,primary_key=True) 
    estado =Column(String(255),nullable=True)
    
    def __repr__(self):
       return f"<Medico user_id={self.user_id} id_esp={self.id_esp}>"


class Tipo(Base):
    __tablename__='glic_tipo'
    id=Column(Integer,primary_key=True)
    descricao =Column(String(255),nullable=True)
    codigo =Column(String(255),nullable=True)
    estado =Column(Integer,primary_key=True)


    def __repr__(self):
       return f"<Tipo codigo={self.codigo} descricao={self.descricao}>"

class Estrutura(Base):
    __tablename__='glic_estrutura'
    id=Column(Integer,primary_key=True)
    ilha =Column(String(255),nullable=True)
    concelho =Column(String(255),nullable=True)
    codigo =Column(String(255),primary_key=True)
    descricao =Column(String(255),primary_key=True)
    estado =Column(Integer,primary_key=True)


    def __repr__(self):
       return f"<Estrutura codigo={self.codigo} descricao={self.descricao}>"

