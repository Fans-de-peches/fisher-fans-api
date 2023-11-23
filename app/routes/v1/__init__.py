from fastapi import APIRouter
from .user_route import router as user_router
from .boat_route import router as boat_router

router = APIRouter()
router.include_router(user_router)
router.include_router(boat_router)
