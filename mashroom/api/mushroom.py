from mashroom.db.schema import MushroomFeatures
from mashroom.db.models import Mushroom
from mashroom.db.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
import joblib
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

mushroom_router = APIRouter(prefix='/mushroom', tags=['Mushroom'])

BASE_DIR = Path(__file__).resolve().parent.parent.parent

model_path = BASE_DIR / 'mushroom_model.pkl'
scaler_path = BASE_DIR / 'mushroom_scaler.pkl'

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


ENCODING_MAP = {
    'cap_shape': ['c', 'f', 'k', 's', 'x'],
    'cap_surface': ['g', 's', 'y'],
    'cap_color': ['c', 'e', 'g', 'n', 'p', 'r', 'u', 'w', 'y'],
    'bruises': ['t'],
    'odor': ['c', 'f', 'l', 'm', 'n', 'p', 's', 'y'],
    'gill_attachment': ['f'],
    'gill_spacing': ['w'],
    'gill_size': ['n'],
    'gill_color': ['e', 'g', 'h', 'k', 'n', 'o', 'p', 'r', 'u', 'w', 'y'],
    'stalk_shape': ['t'],
    'stalk_root': ['c', 'e', 'r'],
    'stalk_surface_above_ring': ['k', 's', 'y'],
    'stalk_surface_below_ring': ['k', 's', 'y'],
    'stalk_color_above_ring': ['c', 'e', 'g', 'n', 'o', 'p', 'w', 'y'],
    'stalk_color_below_ring': ['c', 'e', 'g', 'n', 'o', 'p', 'w', 'y'],
    'veil_color': ['o', 'w', 'y'],
    'ring_number': ['o', 't'],
    'ring_type': ['f', 'l', 'n', 'p'],
    'spore_print_color': ['h', 'k', 'n', 'o', 'r', 'u', 'w', 'y'],
    'population': ['c', 'n', 's', 'v', 'y'],
    'habitat': ['g', 'l', 'm', 'p', 'u', 'w']
}


@mushroom_router.post('/predict')
async def predict(mushroom: MushroomFeatures):
    data = []
    mushroom_dict = mushroom.dict()

    for feature, possible_values in ENCODING_MAP.items():
        value = mushroom_dict[feature]
        encoded = [1 if value == pv else 0 for pv in possible_values]
        data.extend(encoded)

    scaled = scaler.transform([data])
    prediction = model.predict(scaled)[0]
    probability = model.predict_proba(scaled)[0][1]

    return {
        "class": bool(prediction),
        "probability": f'{probability * 100:.1f}'
    }
