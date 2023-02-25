from fastapi import FastAPI
from git import Repo

app = FastAPI()
Repo.clone_from('https://github.com/zlab-foss/backend-interview.git', 'C:/Users/Behshad/Desktop/zlab/download')

@app.post("/")
async def root():
    return Repo




