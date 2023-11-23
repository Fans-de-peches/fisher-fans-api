from fastapi import APIRouter
from .user_route import router as user_router
# Importe d'autres routeurs ici si nécessaire

router = APIRouter()
router.include_router(user_router)
# Inclut d'autres routeurs ici
