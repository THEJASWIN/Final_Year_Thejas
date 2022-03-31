import os
import openai
from wiki import *
from qgen import *
from typing import Optional
from fastapi import FastAPI, UploadFile, Form
from dotenv import load_dotenv,find_dotenv

app=FastAPI()
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

@app.post("/api/chat")
async def chat(inputPrompt: str = Form(...)):
  response = openai.Completion.create(
    engine="text-ada-001",
    prompt=inputPrompt,
    max_tokens=100,
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

@app.post("/api/qagen")
async def qa_generation(keywordPrompt: Optional[str] = Form(None), file: Optional[UploadFile] = None):
  if file.filename == "" and keywordPrompt == None:
    return {"Message": "Please provide a Keyword or TextFile"}
  elif keywordPrompt != None:
    getContent = wiki_content(keywordPrompt)
    getQa = Qa_Gen(getContent)
    return getQa
  else:
    fileContent = await file.read()
    contentText = fileContent.decode("utf-8")
    getQa = Qa_Gen(contentText)
    return getQa