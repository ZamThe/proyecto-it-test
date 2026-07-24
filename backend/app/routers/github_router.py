from fastapi import APIRouter
from app.services.github_service import get_github_user

router = APIRouter(
    prefix="/github",
    tags=["GitHub"]
)

@router.get("/{username}")
def github_user(username: str):
    return get_github_user(username)