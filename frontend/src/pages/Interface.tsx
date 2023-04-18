import React, { useEffect } from "react";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

export function Interface() {
  useEffect(() => {
    // cria o mapa
    const map = L.map("map").setView([-12.205, -38.990], 13);

    // adiciona camada do mapa base do OpenStreetMap
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
      maxZoom: 18,
    }).addTo(map);

    // adiciona marcador ficticio na posição [51.5, -0.09]
    L.marker([-12.240, -38.950]).addTo(map);
    L.marker([-12.265, -38.950]).addTo(map);
    L.marker([-12.253, -38.972]).addTo(map);
  }, []);

  return( 
    <div style={{ height: "100%" }}>
      <div className="flex h-200 w-200"> // div do cabeçalho aqui
        // conteúdo do cabeçalho aqui
      </div>
      <div id="map" style={{ height: "400px" }} className="flex h-200 w-200"></div>
    </div>
  )
}
