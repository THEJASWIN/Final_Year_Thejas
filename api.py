import os
import openai
from fastapi import FastAPI, Request, Form
from dotenv import load_dotenv,find_dotenv

app=FastAPI()
load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPEN_AI_APIKEY')

@app.get("/")
async def qgen():
    return {"Message": "API is working"}

@app.post("/api/py2nl")
async def qgen(inputPrompt: str = Form(...)):
    response = openai.Completion.create(
    engine="code-davinci-002",
    prompt=inputPrompt,
    temperature=0,
    max_tokens=513,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\"\"\""]
    )
    return {"Output":response.choices[0].text}

@app.post("/api/nl2py")
async def qgen(inputPrompt: str = Form(...)):
    response = openai.Completion.create(
    engine="code-davinci-002",
    prompt=inputPrompt,
    temperature=0,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )      
    return {"Output":response.choices[0].text} 

@app.get("/api/qa")
async def qgen(inputPrompt: str = Form(...)):
  response = openai.Completion.create(
    engine="text-ada-001",
    prompt=inputPrompt,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return {"Output":response.choices[0].text}



