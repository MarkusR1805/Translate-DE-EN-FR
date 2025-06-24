import os
import torch
from transformers import pipeline

def load_translation_models(local_model_paths):
    # Prüfen, ob eine GPU verfügbar ist, ansonsten CPU verwenden
    device = torch.device('cuda' if torch.cuda.is_available() else 'mps')
    print(f"Verwendetes Gerät: {device}")

    # Laden der Modelle aus lokalen Pfaden
    de_to_en = pipeline("translation", model=local_model_paths['de_to_en'], device=device)
    en_to_de = pipeline("translation", model=local_model_paths['en_to_de'], device=device)
    de_to_fr = pipeline("translation", model=local_model_paths['de_to_fr'], device=device)
    fr_to_de = pipeline("translation", model=local_model_paths['fr_to_de'], device=device)

    return {
        'de_to_en': de_to_en,
        'en_to_de': en_to_de,
        'de_to_fr': de_to_fr,
        'fr_to_de': fr_to_de
    }

if __name__ == "__main__":
    # Definieren Sie die lokalen Pfade zu Ihren Modellen
    local_model_paths = {
        'de_to_en': './Helsinki-NLP-opus-mt-de-en',
        'en_to_de': './Helsinki-NLP-opus-mt-en-de',
        'de_to_fr': './Helsinki-NLP-opus-mt-de-fr',
        'fr_to_de': './Helsinki-NLP-opus-mt-fr-de'
    }

    # Laden der Modelle
    translation_models = load_translation_models(local_model_paths)
