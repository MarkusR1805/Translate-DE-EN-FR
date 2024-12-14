import torch
from transformers import pipeline

def load_translation_models():
    # Die Modelle laufen schneller auf CPU (zumindest auf dem Mac)
    device = torch.device('cpu')
    print(f"Verwendetes Gerät: {device}")

    # Laden der Modelle deutsch / englisch und umgekehrt
    de_to_en = pipeline("translation", model="Helsinki-NLP/opus-mt-de-en", device=device)
    en_to_de = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de", device=device)

    # Laden der Modelle französisch / deutsch und umgekehrt
    de_to_fr = pipeline("translation", model="Helsinki-NLP/opus-mt-de-fr", device=device)
    fr_to_de = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-de", device=device)

    return {
        'de_to_en': de_to_en,
        'en_to_de': en_to_de,
        'de_to_fr': de_to_fr,
        'fr_to_de': fr_to_de
    }
