from sqlalchemy import Integer,String,Column, ForeignKey
from app.core.database import base
from app.models.produto import Produto
class Carrinho(base):
    __tablename__ = "carrinho"

    id = Column(Integer, autoincrement=True, primary_key=True)
    id_produto = Column(Integer,ForeignKey("produto.id", ondelete="cascade"))
    quantidade = Column(Integer, default=1)

