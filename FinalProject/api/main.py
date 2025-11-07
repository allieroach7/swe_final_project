import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .dependencies.config import conf

app = FastAPI(title="Online Restaurant Ordering System", version="1.0.0")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and create tables
from .models import model_loader
from .routers import index as indexRoute

model_loader.index()
indexRoute.load_routes(app)

@app.get("/")
def read_root():
    return {"message": "Welcome to Online Restaurant Ordering System API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)