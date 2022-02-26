from datetime import date,timezone
from os import stat
from turtle import st
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app=FastAPI()
 
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

db=SessionLocal()
#method get select all
@app.get('/pacientes',response_model=List[Paciente],status_code=200)
def get_all_pacientes():
    pacientes=db.query(models.Paciente).all()

    return pacientes

@app.get('/especialidades',response_model=List[Especialidade],status_code=200)
def get_all_especialidades():
    especialidade=db.query(models.Especialidade).all()

    return especialidade

@app.get('/indece_diario',response_model=List[Indece_diario],status_code=200)
def get_all_indece_diario():
    diario=db.query(models.Indece_diario).all()

    return diario

@app.get('/comunidade',response_model=List[Comunidade],status_code=200)
def get_all_mensagem():
    msg=db.query(models.Comunidade).all()

    return msg

@app.get('/receita',response_model=List[Receita],status_code=200)
def get_all_receita():
    rec=db.query(models.Receita).all()

    return rec

@app.get('/medico',response_model=List[Medico],status_code=200)
def get_all_medico():
    msg=db.query(models.Medico).all()

    return msg

@app.get('/tipo',response_model=List[Tipo],status_code=200)
def get_all_tipo():
    msg=db.query(models.Tipo).all()

    return msg
@app.get('/estrutura',response_model=List[Estrutura],status_code=200)
def get_all_estrutura():
    msg=db.query(models.Estrutura).all()

    return msg

#method get select for id
@app.get('/especialidades/{id}',response_model=Especialidade,status_code=status.HTTP_200_OK)
def get_an_especialidade(id:int):
    user=db.query(models.Especialidade).filter(models.Especialidade.id==id).first()
    return user

@app.get('/paciente/{user_id}',response_model=Paciente,status_code=status.HTTP_200_OK)
def get_an_paciente(user_id:int):
    user=db.query(models.Paciente).filter(models.Paciente.user_id==user_id).first()
    return user

@app.get('/indece_diario/{ind_id}',response_model=Indece_diario,status_code=status.HTTP_200_OK)
def get_an_ind_diario(ind_id:int):
    user=db.query(models.Indece_diario).filter(models.Indece_diario.id==ind_id).first()
    return user

@app.get('/comunidade/{com_id}',response_model=Comunidade,status_code=status.HTTP_200_OK)
def get_an_comunidade(com_id:int):
    user=db.query(models.Comunidade).filter(models.Comunidade.id==com_id).first()
    return user

@app.get('/receita/{rec_id}',response_model=Receita,status_code=status.HTTP_200_OK)
def get_an_receita(rec_id:int):
    user=db.query(models.Receita).filter(models.Receita.id==rec_id).first()
    return user

@app.get('/medico/{med_id}',response_model=Medico,status_code=status.HTTP_200_OK)
def get_an_medico(med_id:int):
    user=db.query(models.Medico).filter(models.Medico.user_id==med_id).first()
    return user

@app.get('/tipo/{tp_id}',response_model=Tipo,status_code=status.HTTP_200_OK)
def get_an_tipo(tp_id:int):
    user=db.query(models.Tipo).filter(models.Tipo.id==tp_id).first()
    return user

@app.get('/estrutura/{est_id}',response_model=Estrutura,status_code=status.HTTP_200_OK)
def get_an_estrutura(est_id:int):
    user=db.query(models.Estrutura).filter(models.Estrutura.id==est_id).first()
    return user

#method post
@app.post('/pacientes',response_model=Paciente,
        status_code=status.HTTP_201_CREATED)
def create_an_paciente(pac:Paciente):
    db_pac=db.query(models.Paciente).filter(models.Paciente.user_id==pac.user_id).first()

    if db_pac is not None:
        raise HTTPException(status_code=400,detail="Item already exists")

    new_pac=models.Paciente(
        user_id=pac.user_id,
        sexo=pac.sexo,
        id_tipo=pac.id_tipo,
        id_med=pac.id_med,
        estado=pac.estado
    )

    db.add(new_pac)
    db.commit()

    return new_pac

@app.post('/especialidade',response_model=Especialidade,
        status_code=status.HTTP_201_CREATED)
def create_an_esp(esp:Especialidade):
    db_esp=db.query(models.Especialidade).filter(models.Especialidade.codigo==esp.codigo).first()

    if db_esp is not None:
        raise HTTPException(status_code=400,detail="Code already exists")

    new_esp=models.Especialidade(
        id=esp.id,
        codigo=esp.codigo,
        descricao=esp.descricao,
        estado=esp.estado
    )

    db.add(new_esp)
    db.commit()

    return new_esp

@app.post('/indece_diario',response_model=Indece_diario,
        status_code=status.HTTP_201_CREATED)
def create_an_ind(ind:Indece_diario):
    db_ind=db.query(models.Indece_diario).filter(models.Indece_diario.id==ind.id).first()

    if db_ind is not None:
        raise HTTPException(status_code=400,detail="Code already exists")

    new_ind=models.Indece_diario(
        id=ind.id,
        id_pac=ind.id_pac,
        indece_glic=ind.indece_glic,
        aliminetos=ind.aliminetos,
        estado=ind.estado
    )

    db.add(new_ind)
    db.commit()

    return new_ind

@app.post('/comunidade',response_model=Comunidade,
        status_code=status.HTTP_201_CREATED)
def create_an_msg(ind:Comunidade):
    db_msg=db.query(models.Comunidade).filter(models.Comunidade.id==ind.id).first()

    if db_msg is not None:
        raise HTTPException(status_code=400,detail="Code already exists")

    new_msg=models.Comunidade(
        id=ind.id,
        mensagem=ind.mensagem,
        user_id_remetente=ind.user_id_remetente,
        user_id_receptor=ind.user_id_receptor,
        tipo=ind.tipo,
        estado=ind.estado
    )

    db.add(new_msg)
    db.commit()

    return new_msg

@app.post('/receita',response_model=Receita,
        status_code=status.HTTP_201_CREATED)
def create_an_msg(rec:Receita):
    db_rec=db.query(models.Receita).filter(models.Receita.id==rec.id).first()

    if db_rec is not None:
        raise HTTPException(status_code=400,detail="Code already exists")

    new_rec=models.Receita(
        id=rec.id,
        descricao=rec.descricao,
        id_med=rec.id_med,
        id_pac=rec.id_pac,
        quantidade=rec.quantidade,
        estado=rec.estado,
        estado_ped=rec.estado_ped

    )

    db.add(new_rec)
    db.commit()

    return new_rec


@app.post('/medico',response_model=Medico,
        status_code=status.HTTP_201_CREATED)
def create_an_med(med:Medico):
    db_med=db.query(models.Medico).filter(models.Medico.user_id==med.user_id).first()

    if db_med is not None:
        raise HTTPException(status_code=400,detail="Code already exists")

    new_med=models.Medico(
        user_id=med.user_id,
        id_esp=med.id_esp,
        id_estr=med.id_estr,
        estado=med.estado

    )

    db.add(new_med)
    db.commit()

    return new_med

@app.post('/tipo',response_model=Tipo,
        status_code=status.HTTP_201_CREATED)
def create_an_tp(tp:Tipo):
    db_tp=db.query(models.Tipo).filter(models.Tipo.id==tp.id).first()

    if db_tp is not None:
        raise HTTPException(status_code=400,detail="Code already exists")

    new_tp=models.Tipo(
        id=tp.id,
        descricao=tp.descricao,
        codigo=tp.codigo,
        estado=tp.estado
    )

    db.add(new_tp)
    db.commit()

    return new_tp

@app.post('/estrutura',response_model=Estrutura,
        status_code=status.HTTP_201_CREATED)
def create_an_est(est:Estrutura):
    db_est=db.query(models.Estrutura).filter(models.Estrutura.id==est.id).first()

    if db_est is not None:
        raise HTTPException(status_code=400,detail="Code already exists")

    new_est=models.Estrutura(
        id=est.id,
        ilha=est.ilha,
        concelho=est.concelho,
        descricao=est.descricao,
        codigo=est.codigo,
        estado=est.estado
    )

    db.add(new_est)
    db.commit()

    return new_est

#method put
@app.put('/paciente/{user_id}',response_model=Paciente,status_code=status.HTTP_200_OK)
def update_an_paciente(user_id:int,pac:Paciente):
    pac_to_update=db.query(models.Paciente).filter(models.Paciente.user_id==user_id).first()
    pac_to_update.sexo=pac.sexo
    pac_to_update.id_tipo=pac.id_tipo
    pac_to_update.id_med=pac.id_med
    pac_to_update.estado=pac.estado

    db.commit()

    return pac_to_update

@app.put('/especialidade/{esp_id}',response_model=Especialidade,status_code=status.HTTP_200_OK)
def update_an_esp(esp_id:int,esp:Especialidade):
    esp_to_update=db.query(models.Especialidade).filter(models.Especialidade.id==esp_id).first()
    esp_to_update.codigo=esp.codigo
    esp_to_update.descricao=esp.descricao
    esp_to_update.estado=esp.estado

    db.commit()

    return esp_to_update

@app.put('/indece_diario/{ind_id}',response_model=Indece_diario,status_code=status.HTTP_200_OK)
def update_an_ind(ind_id:int,ind:Indece_diario):
    ind_to_update=db.query(models.Indece_diario).filter(models.Indece_diario.id==ind_id).first()
    ind_to_update.id_pac=ind.id_pac
    ind_to_update.indece_glic=ind.indece_glic
    ind_to_update.aliminetos=ind.aliminetos
    ind_to_update.estado=ind.estado

    db.commit()

    return ind_to_update

@app.put('/comunidade/{msg_id}',response_model=Comunidade,status_code=status.HTTP_200_OK)
def update_an_msg(msg_id:int,com:Comunidade):
    msg_to_update=db.query(models.Comunidade).filter(models.Comunidade.id==msg_id).first()
    msg_to_update.mensagem=com.mensagem
    msg_to_update.user_id_remetente=com.user_id_remetente
    msg_to_update.user_id_receptor=com.user_id_receptor
    msg_to_update.tipo=com.tipo
    msg_to_update.estado=com.estado

    db.commit()

    return msg_to_update

@app.put('/receita/{rec_id}',response_model=Receita,status_code=status.HTTP_200_OK)
def update_an_msg(rec_id:int,rec:Receita):
    rec_to_update=db.query(models.Receita).filter(models.Receita.id==rec_id).first()
    rec_to_update.descricao=rec.descricao
    rec_to_update.id_med=rec.id_med
    rec_to_update.id_pac=rec.id_pac
    rec_to_update.quantidade=rec.quantidade
    rec_to_update.estado=rec.estado
    rec_to_update.estado_ped=rec.estado_ped

    db.commit()

    return rec_to_update

@app.put('/medico/{med_id}',response_model=Medico,status_code=status.HTTP_200_OK)
def update_an_med(med_id:int,med:Medico):
    med_to_update=db.query(models.Medico).filter(models.Medico.user_id==med_id).first()
    med_to_update.user_id=med.user_id
    med_to_update.id_esp=med.id_esp
    med_to_update.id_estr=med.id_estr
    med_to_update.estado=med.estado

    db.commit()

    return med_to_update

@app.put('/tipo/{tp_id}',response_model=Tipo,status_code=status.HTTP_200_OK)
def update_an_tp(tp_id:int,tp:Tipo):
    tp_to_update=db.query(models.Tipo).filter(models.Tipo.id==tp_id).first()
    tp_to_update.id=tp.id
    tp_to_update.descricao=tp.descricao
    tp_to_update.codigo=tp.codigo
    tp_to_update.estado=tp.estado
 
    db.commit()

    return tp_to_update

@app.put('/estrutura/{estr_id}',response_model=Estrutura,status_code=status.HTTP_200_OK)
def update_an_tp(estr_id:int,est:Estrutura):
    est_to_update=db.query(models.Estrutura).filter(models.Estrutura.id==estr_id).first()
    est_to_update.id=est.id
    est_to_update.ilha=est.ilha
    est_to_update.concelho=est.concelho
    est_to_update.descricao=est.descricao
    est_to_update.codigo=est.codigo
    est_to_update.estado=est.estado
   
    db.commit()

    return est_to_update


#method delete
@app.delete('/paciente/{user_id}')
def delete_paciente(user_id:int):
    pac_to_delete=db.query(models.Paciente).filter(models.Paciente.user_id==user_id).first()

    if pac_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(pac_to_delete)
    db.commit()

    return pac_to_delete

@app.delete('/especialidade/{esp_id}')
def delete_esp(esp_id:int):
    esp_to_delete=db.query(models.Especialidade).filter(models.Especialidade.id==esp_id).first()

    if esp_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(esp_to_delete)
    db.commit()

    return esp_to_delete

@app.delete('/indece_diario/{ind_id}')
def delete_ind(ind_id:int):
    ind_to_delete=db.query(models.Indece_diario).filter(models.Indece_diario.id==ind_id).first()

    if ind_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(ind_to_delete)
    db.commit()

    return ind_to_delete

@app.delete('/comunidade/{msg_id}')
def delete_msg(msg_id:int):
    msg_to_delete=db.query(models.Comunidade).filter(models.Comunidade.id==msg_id).first()

    if msg_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(msg_to_delete)
    db.commit()

    return msg_to_delete

@app.delete('/receita/{rec_id}')
def delete_rec(rec_id:int):
    rec_to_delete=db.query(models.Receita).filter(models.Receita.id==rec_id).first()

    if rec_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(rec_to_delete)
    db.commit()

    return rec_to_delete

@app.delete('/medico/{med_id}')
def delete_med(med_id:int):
    med_to_delete=db.query(models.Medico).filter(models.Medico.user_id==med_id).first()

    if med_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(med_to_delete)
    db.commit()

    return med_to_delete

@app.delete('/tipo/{tp_id}')
def delete_tp(tp_id:int):
    tp_to_delete=db.query(models.Tipo).filter(models.Tipo.id==tp_id).first()

    if tp_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(tp_to_delete)
    db.commit()

    return tp_to_delete

@app.delete('/estrutura/{est_id}')
def delete_med(est_id:int):
    rec_to_delete=db.query(models.Estrutura).filter(models.Estrutura.id==est_id).first()

    if rec_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(rec_to_delete)
    db.commit()

    return rec_to_delete