/*var map = new ol.Map({
        target: document.getElementById('mapdiv'),
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          })
        ],
        view: new ol.View({
          center: ol.proj.fromLonLat([37.41, 8.82]),
          zoom: 4,
        })
        
      });
    */
var mymap = L.map('mapdiv').setView([51.505, -0.09], 13);

/*L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWd1YXJhbmQiLCJhIjoiY2poZ214bWlsMWxrcTNhbzF0OWJndWQ1NiJ9.-aRR2ELQWpsAfW1WMT7cFA', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    crs: L.CRS.EPSG4326,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoibWd1YXJhbmQiLCJhIjoiY2poZ214bWlsMWxrcTNhbzF0OWJndWQ1NiJ9.-aRR2ELQWpsAfW1WMT7cFA'
}).addTo(mymap);
*/
L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
  maxZoom: 20,
  attribution: '&copy; Openstreetmap France | &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  crs: L.CRS.EPSG4326
}).addTo(mymap);
$.ajax({url: "/api/lastlocations",contentType:"application/json", success: function(result){
      //retrieve locations and add markers to the map
      for ( var i = 0; i < result.results.length; i++){
        var obj = result.results[i]; 
        lat = obj["location"]["lat"]
        lng = obj["location"]["lng"]
        
        console.log(obj["location"]);
        var point = L.point([lat,lng]);
        coords3857= L.Projection.LonLat.unproject(point); //get latlng
        console.log(coords3857)
        var marker = L.marker(coords3857).addTo(mymap);

      }
      console.log("map crs: " + mymap.options.crs.code);
      mymap.setView(coords3857);
    },
    error: function(error){
      console.log(error);
    }

  });


