import tkinter as tk
from tkinter import ttk, messagebox
from openai import OpenAI
import json
class OpenAIControler(): 
  def __init__(self, api_key):
     self.api_key = api_key
     self.client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
     )

  def evaluate_with_gemini(self,client_data: dict) -> dict:

    prompt = f"""
    You are a financial analyst. A potential client has the following data:
    {client_data}

    Based on typical credit-financing rules, answer:
   1. Should we approve financing for this client? (Yes or No)
   2. Give a short explanation of the risks or strengths.
   Return answer in JSON like:
   {{ "approved": true/false, "reason": "..." }}
    """
    
    resp = self.client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You are a helpful financial analyst."},
            {"role": "user", "content": prompt}
        ]
    )
    
    text = resp.choices[0].message.content.strip()
    
    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        result = {"approved": False, "reason": "Invalid response format: " + text}
    return result


