from fastapi import FastAPI
app = FastAPI()
@app.get ("/")
def root():
    return "Live from production !"

@app.get ("/test")
def test():
    return "This is a Test !"