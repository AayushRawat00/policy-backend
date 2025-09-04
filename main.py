from fastapi import FastAPI
from app.router.login_register import router as auth_router
from app.router.create_policy import router as policy_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(policy_router, prefix="/api", tags=["api"])

@app.get("/")
def root():
    return {"message": "Backend running"}
