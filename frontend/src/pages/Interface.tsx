import React, { useEffect } from "react";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import "../styles/styles.css"

export function Interface() {
  useEffect(() => {
    // cria o mapa
    const map = L.map("map").setView([-12.245, -38.990], 13);

    // adiciona camada do mapa base do OpenStreetMap
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
      maxZoom: 18,
    }).addTo(map);

    const redIcon = L.icon({
      iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
    });
    const greenIcon = L.icon({
      iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
    });
    // , {icon:redIcon}
    L.marker([-12.240, -38.950]).addTo(map);
    L.marker([-12.265, -38.950]).addTo(map);
    L.marker([-12.253, -38.972]).addTo(map);
  }, []);

  return( 
    <div className="Main">
      <div className="Header"> // div do cabeçalho aqui
        // conteúdo do cabeçalho aqui
      </div>
      <div id="map" style={{ height: "500px", width:'800px'}} className=""></div>
    </div>
  )
}
