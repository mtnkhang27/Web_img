from uvicorn import run
from fastapi import FastAPI, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
import datetime


app = FastAPI()


def cleanFilename(sourcestring,  removestring =" %:/,\\[]<>()*?"):
    # Remove unwanted character in file name
    return ''.join([c for c in sourcestring if c not in removestring])


class age_race_gender(BaseModel):
    age: int
    race: str = "NULL"
    gender: str = "NULL"   
    
@app.get("/")
async def nhucc():
    return  FileResponse('index.html')

@app.post("/upload")
async def upload_file(
    file: UploadFile,
):
    print("Received request")

    contents = file.file.read()
    #print(contents)
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "data/" + suffix + ".png"
    
    print(f"saving video to {filename}")
    with open(filename, 'wb') as f:
        f.write(contents)
        
    # res = predict(filename)
    response = age_race_gender(
        age = 19,
        race = "Bien Hoa",
        gender = "gay"
    )
    return response

if __name__ == "__main__":
    run("app:app", host="localhost", port=8080)