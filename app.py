import os
import openai
from wiki import show_suggestion
from fastapi import FastAPI, Form
from dotenv import load_dotenv,find_dotenv
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPEN_AI_APIKEY')

@app.get("/")
async def index():
    return {"Message": "API is working"}

@app.post("/api/py2nl")
async def code(codePrompt: str = Form(...)):
    response = openai.Completion.create(
    engine="code-davinci-002",
    prompt=codePrompt,
    temperature=0,
    max_tokens=513,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\"\"\""]
    )
    return response.choices[0].text

@app.post("/api/nl2py")
async def code(codePrompt: str = Form(...)):
    response = openai.Completion.create(
    engine="code-davinci-002",
    prompt=codePrompt,
    temperature=0,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    ) 
    return response.choices[0].text

@app.post("/api/suggestion")
async def suggestion(keywordPrompt: str = Form(...)):
  return show_suggestion(keywordPrompt)

@app.post("/api/notes")
async def note_making(inputPrompt: str = Form(...)):
  response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=inputPrompt,
  temperature=0.3,
  max_tokens=150,
  top_p=1, 
  frequency_penalty=0,
  presence_penalty=0
)
  return response.choices[0].text