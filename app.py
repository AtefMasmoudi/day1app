from fastapi import FastAPI
app = FastAPI()
@app.get ("/")
def root():
    return "Live from production !"