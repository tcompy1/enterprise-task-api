from fastapi import FastAPI

app = FastAPI(title="Enterprise Task API")

@app.get("/")
def read_root():
    return {"message": "Welcome to Task API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/name")
def return_name():
    return {"Name:" "Trent"}

@app.post("/greeting")
def accept_name(name: str):
    return {"message": f"Hello, {name}"}
    