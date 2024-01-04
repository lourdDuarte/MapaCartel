// VARIABLES

var filter_container = document.getElementById('popup-filter');
var filter_content = document.getElementById('filter-content');
var container = document.getElementById('popup');
var content = document.getElementById('popup-content');
var closer = document.getElementById('popup-closer');
var dato_encontrado = document.getElementById('dato-encontrado');
var dato_no_encontrado = document.getElementById('dato-no-encontrado');
var popup_filter = document.getElementById('ol-popup-filter');
var btn_solicitar = document.getElementById('solicitar-excel');
var btn_descargar = document.getElementById('descargar-excel');
var btn_filtros = document.getElementById('filtros');


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
           
           content.innerHTML = '<div>' //inicio contenedor datos presentacion
             +'<div class="div-data">'
             +'<p class= "data-p">Nombre: <span class="data"> '+ " " + data.nombre + '</span></p>'
             +'<p class= "data-p">Altura: <span class="data"> '+ " " +data.altura + '</span></p>'
             +'<p class= "data-p">Largo: <span class="data"> '+ " " +data.largo + '</span></p>'
             +'<p class= "data-p">m²2: <span class="data"> '+ " " +data.metros_cuadrados + '</span></p>'
             +'<p class= "data-p">Direccion:  <span class="data"> '+" " + data.direccion + '</span></p>'
             +'<p class= "data-p">Localidad: <span class="data"> '+" " + data.localidad + '</span></p>'
             +'<p class="data-p">Latitud: <span class="data">' + " " +data.longitud+ '</span></p>'
             +'<p class="data-p">Longitud:  <span class="data">' + " " +data.latitud + '</span></p>'
             +'<p class="data-p">Ultima modificacion:  <span class="data">' +" " + data.ultima_modificacion + '</span></p>'
             +'<img class="img-cartel-mapa" src="/media/'+ data.imagen + '" alt="Imagen" /></p>'
             +'</div>'
             +'</div>' //fin contenedor datos renaper
            
          
           localStorage.setItem(feature.getId(), data.nombre);
           overlay.setPosition(coordinate);

          
       }
     })

    
  });
  
});
  function solicitar_datos() {
    btn_solicitar.style.visibility = 'hidden';
    btn_filtros.style.visibility = 'hidden';
    btn_descargar.style.visibility = 'visible';
    popup_filter.style.display = 'none';

    localStorage.clear();
    alert("Seleccionar los carteles que desea descargar o reinicie el mapa")
  }

 function descargar_datos() {
  const claves = Object.keys(localStorage);
  const carteles = [];
  const datos = []

  //Se almacenan en un array para luego utilizar la informacion y descargar el excel
  claves.forEach(clave => {
    
    carteles.push({
      'clave': clave,
      
  });
 });
  console.log(carteles)

  carteles.forEach(cartel => {
    datos_cartel.forEach(data => {
        if(data.id == cartel.clave){
          
          
          datos.push({
            'id':data.id, 
            'nombre': data.nombre,
            'localidad': data.localidad,
            'proveedor': data.proveedor,
            'latitud': data.latitud,
            'longitud': data.longitud,
            'direccion': data.direccion,
            'altura': data.altura,
            'largo':data.largo,
            'metros_cuadrados': data.metros_cuadrados,
            'metros_precio': '$' + data.metros_precio
          });
        }
    
    })
    
  })


  
  const worksheet = XLSX.utils.json_to_sheet(datos);
  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, worksheet, "Dates");

  /* fix headers */
  XLSX.utils.sheet_add_aoa(worksheet, [["Nombre del cartel", "Localidad", "Proveedor", "Latitud", "Longitud", "Direccion", "Altura", "Largo", "Metros cuadrados", "Metros precio"]], { origin: "A1" });

  /* calculate column width */
  const max_width = datos.reduce((w, r) => Math.max(w, r.nombre.length), 10);
  worksheet["!cols"] = [ { wch: max_width } ];

  /* create an XLSX file and try to save to Presidents.xlsx */
  XLSX.writeFile(workbook, "Carteles.xlsx", { compression: true });
  
  location.reload()
}




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


// FUNCION PARA MOVER CAJA DE FILTRO

popup_filter.onmousedown = function(event) {
//   // Obtener el elemento sobre el cual se hizo clic
 const clickedElement = event.target;
// Verificar si el clic proviene de los elementos internos (selects y botón)
   if (
     clickedElement.tagName === 'SELECT' ||
     clickedElement.tagName === 'BUTTON'
   ) {
     // No iniciar el movimiento si se hizo clic en los elementos internos
     return;
   }
  // (1) preparar para mover: hacerlo absoluto y ponerlo sobre todo con el z-index
  popup_filter.style.position = 'absolute';
  popup_filter.style.zIndex = 100;

  // quitar cualquier padre actual y moverlo directamente a body
 // para posicionarlo relativo al body
 document.body.append(popup_filter);


  function moveAt(pageX, pageY) {
    {
      popup_filter.style.left = pageX - popup_filter.offsetWidth / 2 + 'px';
      popup_filter.style.top = pageY - popup_filter.offsetHeight / 2 + 'px';
    }
  }

  // mover la caja posicionada absolutamente bajo el puntero
 moveAt(event.pageX, event.pageY);

  function onMouseMove(event) {
  
      moveAt(event.pageX, event.pageY);
   
  }

  // (2) mover caja con mousemove
 document.addEventListener('mousemove', onMouseMove);

 // (3) soltar caja, quitar cualquier manejador de eventos innecesario
  popup_filter.onmouseup = function() {
    document.removeEventListener('mousemove', onMouseMove);
    popup_filter.onmouseup = null;
  };

 };