import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status


@pytest.mark.anyio
async def test_health(client: AsyncClient, fastapi_app: FastAPI) -> None:
    """
    Checks the health endpoint.

    :param client: client for the app.
    :param fastapi_app: current FastAPI application.
    """
    data = {"vendor_id": 1, "distance_km": 1.0}
    url = fastapi_app.url_path_for("predict")

    response = await client.post(url, json=data)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["travel_time"], float)
