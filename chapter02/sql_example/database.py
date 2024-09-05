from typing import Any
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id : Mapped[int]  = mapped_column(primary_key=True,)
    name : Mapped[str]
    email : Mapped[str]
    
    def __init__(self, name, email):
        super().__init__()
        self.name  = name
        self.email = email
          
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind = engine)