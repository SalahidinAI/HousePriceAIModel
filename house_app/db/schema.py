from pydantic import BaseModel


class HouseSchema(BaseModel):
    OverallQual: int
    Neighborhood: str
    GrLivArea: int
    GarageCars: int
    GarageArea: int
    TotalBsmtSF: int
    firstFlrSF: int
    FullBath: int
    YearBuilt: int
    YearRemodAdd: int
    TotRmsAbvGrd: int