import gradio as gr
import torch
from transformers import pipeline
import webbrowser
import threading

# Prüfen, ob CUDA verfügbar ist
if torch.cuda.is_available():
    device = torch.device('cuda')
# Prüfen, ob MPS (Apple Silicon) verfügbar ist
elif torch.backends.mps.is_available():
    device = torch.device('mps')
# Wenn keines der beiden verfügbar ist, auf CPU zurückgreifen
else:
    device = torch.device('cpu')

#device = get_device()
print(f"Verwendetes Gerät: {device}")

# Laden der Modelle deutsch / englisch und umgekehrt
de_to_en = pipeline("translation", model="Helsinki-NLP/opus-mt-de-en", device=device)
en_to_de = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de", device=device)

# Laden der Modelle französisch / deutsch und umgekehrt
de_to_fr = pipeline("translation", model="Helsinki-NLP/opus-mt-de-fr", device=device)
fr_to_de = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-de", device=device)

# Übersetzungsfunktionen
def translate_de_to_en(text):
    return de_to_en(text)[0]['translation_text']

def translate_en_to_de(text):
    return en_to_de(text)[0]['translation_text']

# Übersetzungsfunktionen französisch / deutsch und umgekehrt
def translate_de_to_fr(text):
    return de_to_fr(text)[0]['translation_text']

def translate_fr_to_de(text):
    return fr_to_de(text)[0]['translation_text']

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Deutsch-Englisch und Deutsch-Französisch Übersetzer und umgekehrt ;-)")
    
    with gr.Row():
        with gr.Column():
            german_input = gr.Textbox(label="Deutscher Text", lines=5)
            en_output = gr.Textbox(label="Englische Übersetzung", lines=5)
            de_to_en_btn = gr.Button("Deutsch -> Englisch")
        
        with gr.Column():
            english_input = gr.Textbox(label="Englischer Text", lines=5)
            de_output = gr.Textbox(label="Deutsche Übersetzung", lines=5)
            en_to_de_btn = gr.Button("Englisch -> Deutsch")
        # Fränzösisch / Deutsch  und umgekehrt
    with gr.Row():
        with gr.Column():
            germanfr_input = gr.Textbox(label="Deutscher Text", lines=5)
            fr_output = gr.Textbox(label="Französische Übersetzung", lines=5)
            de_to_fr_btn = gr.Button("Deutsch -> Französisch")
        
        with gr.Column():
            frgerman_input = gr.Textbox(label="Französischer Text", lines=5)
            defr_output = gr.Textbox(label="Deutsche Übersetzung", lines=5)
            fr_to_de_btn = gr.Button("Französisch -> Deutsch")
    
    de_to_en_btn.click(translate_de_to_en, inputs=german_input, outputs=en_output)
    en_to_de_btn.click(translate_en_to_de, inputs=english_input, outputs=de_output)
    # Übersetzungsalgorythmus
    de_to_fr_btn.click(translate_de_to_fr, inputs=germanfr_input, outputs=fr_output)
    fr_to_de_btn.click(translate_fr_to_de, inputs=frgerman_input, outputs=defr_output)

# Funktion zum Öffnen des Browsers
def open_browser():
    webbrowser.open_new("http://127.0.0.1:7860/")

# Starten der Gradio-Oberfläche und Öffnen des Browsers
if __name__ == "__main__":
    # Starten des Browsers in einem separaten Thread
    threading.Timer(1.5, open_browser).start()
    # Starten der Gradio-Oberfläche
    demo.launch()