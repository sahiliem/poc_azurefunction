import json
import os

import uvicorn
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
def read_root():
    return {"Hello": "World!!!"}


if __name__ == '__main__':
    host_name = os.getenv('SERVER_HOST', '127.0.0.1')
    print(host_name)
    print("TESTING")
    uvicorn.run(app, host='0.0.0.0', port=8010)
    print("running")
