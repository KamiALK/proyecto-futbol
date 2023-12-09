from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def root():
    return "hola camilo como estas"