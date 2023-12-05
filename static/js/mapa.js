// VARIABLES

var filter_container = document.getElementById('popup-filter');
var filter_content = document.getElementById('filter-content');
var container = document.getElementById('popup');
var content = document.getElementById('popup-content');
var closer = document.getElementById('popup-closer');
var dato_encontrado = document.getElementById('dato-encontrado');
var dato_no_encontrado = document.getElementById('dato-no-encontrado');
var popup_filter = document.getElementById('ol-popup-filter');

//FIN VARIABLES

//INICIALIZACION DE LISTAS PARA LOS MARCADORES
const marcadores = [];
const filtros = []; 



//CARGA DE MAPA PRINCIPAL
const overlay = new ol.Overlay({
    element: container,
    autoPan: true,
    autoPanAnimation: {
            duration: 300,
    }       
  });
  
  
  
  var map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    overlays: [overlay],
    view: new ol.View({
      center: ol.proj.fromLonLat([-60.1450400, -24.555300]),
      zoom: 8
    }),
  
  });
  



//FIN CARGA MAPA PRINCIPAL

// MODAL CON DETALLE DE LAS OBRAS
map.on('click', function (e) {
  map.forEachFeatureAtPixel(e.pixel, function (feature, layer) {

    const coordinate = e.coordinate;
    
    
    datos_cartel.forEach(data => {
      
       if(feature.getId() == data.id){
           console.log(data)
           content.innerHTML = '<div>' //inicio contenedor datos presentacion
             +'<div class="div-data">'
             +'<p class= "data-p">Nombre: <span class="data"> '+ data.nombre + '</span></p>'
             +'<p class= "data-p">Direccion: <span class="data"> '+ data.direccion + '</span></p>'
             +'<p class= "data-p">Localidad: <span class="data"> '+ data.localidad + '</span></p>'
             +'<p class="data-p">Latitud: <span class="data">' + data.longitud+ '</span></p>'
             +'<p class="data-p">Longitud:  <span class="data">' + data.latitud + '</span></p>'
             +'<img class="img-cartel" src="/media/'+ data.imagen + '" alt="Imagen" /></p>'

             +'</div>'
             +'</div>' //fin contenedor datos renaper
            
          
            
           overlay.setPosition(coordinate);
          
       }
     })

    
  });
  
});

// CIERRE DE MODAL
closer.onclick = function() {
  overlay.setPosition(undefined);
  closer.blur();
  return false;
};




//************************** CARGA DE UBICACIONES ********************************/

//CARGA DE UBICACIONES DE TODAS LAS OBRAS 
ubicaciones_carteles = cargar_datos(coordenadas, iconos,  marcadores)
var ultimaCapa = new ol.layer.Vector({
  source: new ol.source.Vector({
    features: ubicaciones_carteles, 
  }),
  
});

map.addLayer(ultimaCapa)

//FIN CARGA DE UBICACIONES DE TODAS LAS OBRAS 


//CARGA DE UBICACIONES CON FILTROS APLICADOS DE TODAS LAS OBRAS

if (filtros_ubicacion.length > 0){
      dato_no_encontrado.style.display = 'none';
      dato_encontrado.style.display = 'block';
      popup_filter.style.display = 'block';
      ultimaCapa.getSource().clear() //borra marcadores existentes

      cartles_filtrados = cargar_datos(filtros_ubicacion,iconos, filtros)
     

      var ultimaCapa = new ol.layer.Vector({
        source: new ol.source.Vector({
          features: cartles_filtrados, 
        }),
      })
      
      
      map.addLayer(ultimaCapa)

}

function maximizar_filtros(){
  

  popup_filter.style.display = 'block';
}

function minimizar_filtros(){
  popup_filter.style.display = 'none';
}