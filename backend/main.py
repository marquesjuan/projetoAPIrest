from fastapi import FastAPI
from app.routes.usuario import router as usuario_router
from  fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(usuario_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

