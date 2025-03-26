from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from pydantic import BaseModel
from app.core.database import session

router = APIRouter()

class UsuarioBase (BaseModel):

    nome: str
    email: str
    senha: str


@router.post("/usuario/cadastro")
def post_cadastro(usuario:UsuarioBase):
    db = session()
    usuarioDB = Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    db.add(usuarioDB)
    db.commit()
    db.refresh(usuarioDB)
    db.close()

    return {"usuario":usuarioDB}

@router.get("/usuario/login")
def get_login(email: str, senha: str):
    db = session()
    usuarioDB = db.query(Usuario).filter(Usuario.email == email, Usuario.senha == senha).first()

    if(usuarioDB): return {
        "usuario": {
            "id": usuarioDB.id,
            "nome": usuarioDB.nome,
            "email": usuarioDB.email
    }   }
    raise HTTPException(status_code=400)

