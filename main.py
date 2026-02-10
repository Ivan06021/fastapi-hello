from fastapi import FastAPI
from controllers.hello_controller import router

app = FastAPI()
app.include_router(router)
