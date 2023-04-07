from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/create-job", response_class=HTMLResponse)
async def create_job():
    with open('./templates/create_job.html') as f:
        return f.read()
