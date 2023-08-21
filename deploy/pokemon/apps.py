from django.apps import AppConfig
import joblib

import os

class PokemonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pokemon'
    model_path = os.path.join("model", "model_pokemon.joblib")
    model_path = os.path.join('pokemon', model_path)
    trained_model = joblib.load(model_path)
