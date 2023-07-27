from models.base import Session
from models.company_model import CompanyModel

class CompanyService:
    def create(self, cnpj, cnae, company_name, fantasy_name) -> CompanyModel:
        with Session.begin() as session:
            company = CompanyModel(
                cnpj,
                cnae,
                company_name,
                fantasy_name,
            )

            session.add(company)
            return company.asdict()

    def find(self, cnpj) -> CompanyModel:
        with Session.begin() as session:
            company = session.query(CompanyModel).filter(CompanyModel.cnpj == cnpj).first()

            return company.asdict()

    def all(self, start: int = 0, limit: int = 25, sort: str = None, dir: str = 'asc') -> list:
        with Session.begin() as session:
            query = session.query(CompanyModel)

            total_companies = query.count()

            if sort:
                sort_column = getattr(CompanyModel, sort, None)
                if sort_column is not None:
                    if dir.lower() == 'desc':
                        query = query.order_by(sort_column.desc())
                    else:
                        query = query.order_by(sort_column.asc())

            companies = query.offset(start).limit(limit).all()
            dict_companies = [row.asdict() for row in companies]

            return dict_companies, total_companies


    def update(self, cnpj, fantasy_name, cnae) -> CompanyModel:
        with Session.begin() as session:
            session.query(CompanyModel).filter(CompanyModel.cnpj == cnpj).update({"fantasy_name": fantasy_name, "cnae": cnae})


    def remove(self, cnpj):
        with Session.begin() as session:
            session.query(CompanyModel).filter(CompanyModel.cnpj == cnpj).delete()
