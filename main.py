from fastapi import FastAPI
from routers import posts ,history
from fastapi.middleware.cors import CORSMiddleware
from database.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()   

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


  
app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(history.router, prefix="/history", tags=["history"])