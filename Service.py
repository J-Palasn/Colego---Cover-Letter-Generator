import requests
import streamlit as st

API_URL = "https://router.huggingface.co/v1/chat/completions"
HF_TOKEN = st.secrets["HF_TOKEN"]
headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def generate(messages):
    response = query({
        "messages": messages,
        "model": "mistralai/Mistral-7B-Instruct-v0.2:featherless-ai"
    })

    return response["choices"][0]["message"]["content"]