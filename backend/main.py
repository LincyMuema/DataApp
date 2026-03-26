from fastapi import FastAPI

#allows frontend to talk to the backend
from fastapi.middleware.cors import CORSMiddleware 
from routes import upload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api", tags=["CSV Operations"])

@app.get("/")
def read_root():
    return {"message": "API is working"}