import joblib
import logging
from fastapi import APIRouter

from taxi_travel_time_prediction.web.api.predict.schema import RideInfo, TravelTime

router = APIRouter()


@router.post("/predict", response_model=TravelTime)
def predict(
    ride_info: RideInfo,
) -> TravelTime:
    """
    Predicts travel time.

    :param ride_info: information about incomming ride.
    :returns: travel time.
    """
    logging.info(f"Predicting travel time for {ride_info}.")
    model = joblib.load("./model.joblib")

    features = [
        [
            ride_info.vendor_id,
            ride_info.distance_km,
        ],
    ]
    prediction = model.predict(features).tolist()[0]
    return TravelTime(travel_time=prediction)