from fastapi import APIRouter
from .user_route import router as user_router
from .boat_route import router as boat_router
from .fishing_log_route import router as fishing_log_router
from .trip_route import router as trip_router
from .booking_route import router as booking_router

router = APIRouter()

router.include_router(user_router)
router.include_router(boat_router)
router.include_router(fishing_log_router)
router.include_router(trip_router)
router.include_router(booking_router)