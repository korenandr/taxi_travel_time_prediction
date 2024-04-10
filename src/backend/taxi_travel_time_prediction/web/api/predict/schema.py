from pydantic import BaseModel


class RideInfo(BaseModel):
    """Model describes ride of passenger."""

    vendor_id: int
    distance_km: float


class TravelTime(BaseModel):
    """Time for travelling in seconds."""

    travel_time: float
