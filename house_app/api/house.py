from fastapi import APIRouter, Depends
from house_app.db.schema import HouseSchema
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


house_router = APIRouter(prefix='/house', tags=['House'])

BASE_DIR = Path(__file__).resolve().parent.parent.parent

model_path = BASE_DIR / 'model_gra.pkl'
scaler_path = BASE_DIR / 'scaler.pkl'

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@house_router.post('/predict')
async def predict(house: HouseSchema):
    house_dict = house.dict()

    neighborhood = house_dict.pop('Neighborhood')

    neighborhood_0_1 = [
        1 if neighborhood == 'Blueste' else 0,
        1 if neighborhood == 'BrDale' else 0,
        1 if neighborhood == 'BrkSide' else 0,
        1 if neighborhood == 'ClearCr' else 0,
        1 if neighborhood == 'CollgCr' else 0,
        1 if neighborhood == 'Crawfor' else 0,
        1 if neighborhood == 'Edwards' else 0,
        1 if neighborhood == 'Gilbert' else 0,
        1 if neighborhood == 'IDOTRR' else 0,
        1 if neighborhood == 'MeadowV' else 0,
        1 if neighborhood == 'Mitchel' else 0,
        1 if neighborhood == 'NAmes' else 0,
        1 if neighborhood == 'NPkVill' else 0,
        1 if neighborhood == 'NWAmes' else 0,
        1 if neighborhood == 'NoRidge' else 0,
        1 if neighborhood == 'NridgHt' else 0,
        1 if neighborhood == 'OldTown' else 0,
        1 if neighborhood == 'SWISU' else 0,
        1 if neighborhood == 'Sawyer' else 0,
        1 if neighborhood == 'SawyerW' else 0,
        1 if neighborhood == 'Somerst' else 0,
        1 if neighborhood == 'StoneBr' else 0,
        1 if neighborhood == 'Timber' else 0,
        1 if neighborhood == 'Veenker' else 0,
    ]

    features = list(house_dict.values()) + neighborhood_0_1
    scaled = scaler.transform([features])
    prediction = model.predict(scaled)[0]
    return {'predicted_price': f'{round(prediction)}'}
