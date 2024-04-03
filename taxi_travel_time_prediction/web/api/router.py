from fastapi.routing import APIRouter

from taxi_travel_time_prediction.web.api import echo, monitoring, predict

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(predict.router, prefix="/predict", tags=["predict"])
