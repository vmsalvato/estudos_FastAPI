from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Fila(BaseModel):
      posicao: Optional[int] = 1
      nome: str = "Seu nome"
      data: str = "21/11/2023"
      prioridade: str = "Escolha: (P) Prioritário ou (N) Normal"
      atendido: Optional[bool] = False

db_fila = [
      Fila(nome="José", data="22/11/2023", prioridade="N")
]

@app.get("/")
def home():
    return {"message": "API Fila by FastAPI"}

@app.get("/fila/",status_code=status.HTTP_200_OK)
def exibe_fila():
        if(db_fila == []):
            return {"fila": db_fila, "status": status.HTTP_200_OK}
        else:
            return {"fila": db_fila}
    
@app.delete("/fila/{posicao}")
def apagar_posicao(posicao: int):
    if(posicao == True):
        fila = [fila for fila in db_fila if fila.posicao == posicao]
        db_fila.remove(fila[0])
        return {"message": "Posição removida da fila!"}
    else:
        return {"message": "Nada encontrado!", "status": status.HTTP_404_NOT_FOUND}

@app.get("/fila/{posicao}")
def mostrar_fila(posicao: int):
    if(posicao == True):
        return {"fila": [fila for fila in db_fila if posicao==fila.posicao]}
    else:
        return {"message": "Nada encontrado!", "status": status.HTTP_404_NOT_FOUND}
    
@app.post("/fila/")
def adicionar_fila(fila: Fila):
    if(fila.prioridade == "N"):
        fila.posicao = len(db_fila) + 1
        db_fila.append(fila)
        return {"message": "Adicionado na fila!"}
    elif(fila.prioridade == "P"):
        fila.posicao = len(db_fila) + 1
        db_fila.insert(0,fila)
        return {"message": "Adicionado na fila!"}

@app.patch("/fila/{posicao}")
def atualizar_fila(fila: Fila, posicao: int):
    index = [index for index, fila in enumerate(db_fila) if fila.posicao == posicao] 
    fila.posicao = db_fila[index[0]].posicao
    db_fila[index[0]] = fila
    return {"message": "Fila atualizada!"}