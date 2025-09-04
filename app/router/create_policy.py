from fastapi import APIRouter, HTTPException
from app.models.login_register import User
from app.models.policy_details import PolicyDetails
from app.services import create_excel

router = APIRouter()

@router.post("/policy", response_model=User)
def create_policy(request: PolicyDetails):
    try:
        return create_excel.register_user(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
