from fastapi import FastAPI
from git import Repo
import subprocess

app = FastAPI(
    title="zlab"
)

@app.get("/")
async def root():
    Repo.clone_from('https://github.com/zlab-foss/backend-interview.git', 'C:/Users/Behshad/Desktop/zlab/download')
    subprocess.call('cd C:/Users/Behshad/Desktop/zlab/download && docker build -t behshad . && docker run behshad', shell=True)
    return {"message":"repo downloded"}






