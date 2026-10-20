from fastapi import FastAPI

app = FastAPI(title="Billing API")

@app.get("/")
def read_root():
    return {"status": "Billing API online"}