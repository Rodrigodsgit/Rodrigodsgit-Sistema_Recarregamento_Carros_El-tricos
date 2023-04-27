import React, { useEffect, useState, useRef } from "react";
import L, { marker } from "leaflet";
import "leaflet/dist/leaflet.css";
import "../styles/styles.css"
import axios from "axios";

let map;

export function Interface() {
  const [data, setData] = useState([]);
  const [coords, setcoords] = useState([-12.271, -38.961])
  const [batery, setbatery] = useState(100)
  const markerRef = useRef<L.Marker | null>(null);
  const [count, setcount] = useState(0)


  useEffect(() => {
    // cria o mapa
    map = L.map("map").setView([-12.245, -38.990], 13);

    // adiciona camada do mapa base do OpenStreetMap
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
      maxZoom: 18,
    }).addTo(map);

    // , {icon:redIcon}
    L.marker([-12.240, -38.950]).addTo(map);
    L.marker([-12.265, -38.950]).addTo(map);
    L.marker([-12.253, -38.972]).addTo(map);
  }, []);
 
  useEffect(() => {
    const interval = setInterval(() => {
      fetchData();
      baterylow();
      console.log(batery)
      console.log(count)
      if(count === 1){
        const latitude = Math.random() * (-12.285 - (-12.205)) + (-12.205);
        const longitude = Math.random() * (-38.990 - (-38.905)) + (-38.905);
        setcoords([latitude,longitude])
        setbatery(100)
        setcount(0)
      }
    }, 3000); 

    return () => clearInterval(interval);
  }, [batery,count]); 

  async function fetchData() {
    try {
      axios({
        method: 'get',
        url: `http://172.16.103.4:5001/positions`,
        }).then(function (response){
          if (response.data){
              setData(response.data)
          }
    })
    } catch (error) {
      console.log(error);
    }
  }

  async function baterylow(){
    if (batery > 50){
      setbatery(prevBatery => prevBatery - 10)
    }
    else if (count === 0){
      getStation();
      setcount(1)
    }
  }
 
  async function getStation(){
    try { 
      axios({
        method: 'post',
        url: `http://172.16.103.4:5001/lessQueue`,
        data:{
          latitude: coords[0],
          longitude: coords[1]
        }
        }).then(function (response){
          if (response.data){
            setcoords([Number(Object.values(response.data)[0][3] +0.001),Number(Object.values(response.data)[0][4])])
          }
    })
    } catch (error) {
      console.log(error);
    }
  }

  useEffect(() =>{

  }, [count])

  useEffect(() => {
    // adiciona marcadores ao mapa quando o estado data é atualizado
    const greenIcon = L.icon({
      iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
    });

    data.forEach((coord) => {
      L.marker(coord,{icon:greenIcon}).addTo(map);
    });
  }, [data]);

  useEffect(() =>{
    const redIcon = L.icon({
      iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
    });
    markerRef.current?.remove()
    const marker1 = L.marker(coords,{icon:redIcon}).addTo(map);
    markerRef.current = marker1;

  },[coords])

  return( 
    <div className="Main">
      <div className="Header"> Recharge
      </div>
      <div id="map" style={{ height: "500px", width:'800px'}} className=""></div>
    </div>
  )
}
