from .base import Base
from sqlalchemy import Column, String, Integer, DateTime, func

class CompanyModel(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cnpj = Column(String(20), unique=True)
    cnae = Column(String(10))
    company_name = Column(String(200))
    fantasy_name = Column(String(200))
    create_at = Column(DateTime, default=func.now())

    def __init__(self, cnpj, cnae, company_name, fantasy_name):
        self.cnpj = cnpj
        self.cnae = cnae
        self.company_name = company_name
        self.fantasy_name = fantasy_name

