from transformers import pipeline
from huggingface_hub import login

# Log in with your Hugging Face token
login(token='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')  # Replace with your actual token

# Load the translation model
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")

input_text = "Translate this sentence into Korean."

# Perform translation
translated_text = translator(input_text)

print("Translated text: ", translated_text[0]['translation_text'])
