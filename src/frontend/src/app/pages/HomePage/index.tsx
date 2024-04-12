import * as React from "react";
import { Helmet } from "react-helmet-async";

export function HomePage() {
  const [vendorId, setVendorId] = React.useState("");
  const [distanceKm, setDistanceKm] = React.useState("");
  const [travelTime, setTravelTime] = React.useState("");

  const sendData = async () => {
    const parsedVendorId = parseInt(vendorId);
    const parsedDistanceKm = parseFloat(distanceKm);

    if (isNaN(parsedVendorId) || isNaN(parsedDistanceKm)) {
      console.error('vendorId and distanceKm must be valid numbers');
      return;
    }

    const response = await fetch('http://taxi-travel-time-prediction.local/api/predict/', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ vendor_id: parsedVendorId, distance_km: parsedDistanceKm })
    });

    if (response.ok) {
      const data = await response.json();
      setTravelTime(data["travel_time"]);
    } else {
      setTravelTime("Error sending data");
    }
  };

  return (
    <>
      <Helmet>
        <title>HomePage</title>
        <meta name="description" content="A Boilerplate application homepage" />
      </Helmet>
      <input type="number" step="1" placeholder="Vendor ID" value={vendorId} onChange={e => setVendorId(e.target.value)} />
      <input type="number" step="0.01" placeholder="Distance km" value={distanceKm} onChange={e => setDistanceKm(e.target.value)} />
      <button onClick={sendData}>Calculate travel time</button>
      <p>{travelTime}</p>
    </>
  );
}
