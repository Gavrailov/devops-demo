from fastapi import FastAPI

app = FastAPI(title="DevOps Demo API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "OK", "status": "healthy"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/items/{item_id}")
def get_item(item_id: int, name: str = "unknown"):
    return {"item_id": item_id, "name": name}