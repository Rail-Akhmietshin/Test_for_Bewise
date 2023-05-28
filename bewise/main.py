import os
import sys

from fastapi.middleware.cors import CORSMiddleware

from .tasks.router import router as router_tasks
from .auth.router import router as router_user
from .audio.router import router as router_audio
from fastapi import FastAPI

root_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(root_path)


app = FastAPI(
    title='bewise',
)

origins = [
    "http://localhost",
    "http://0.0.0.0",
    "http://localhost:5555",
    "http://localhost:8000",
    "http://0.0.0.0:5555",
    "http://0.0.0.0:8000",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # allow_methods=["*"],
    # allow_headers=["*"]
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Authorization", "Access-Control-Allow-Origin",
                   "Access-Control-Allow-Credentials", "Access-Control-Allow-Headers", "Access-Control-Allow-Methods",
                   "Access-Control-Expose-Headers", "Access-Control-Max-Age", "Access-Control-Request-Headers",
                   "Access-Control-Request-Method", "Origin", "Timing-Allow-Origin"],
)

# *["http://localhost:" + port for port in ["5555", "8000"]],
app.include_router(router_tasks)
app.include_router(router_user)
app.include_router(router_audio)
