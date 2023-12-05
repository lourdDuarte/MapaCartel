function cargar_datos(ubicacion, iconos, feature){
    
    ubicacion.forEach(coordenada => {
          
      let marcador = new ol.Feature({
          id: coordenada.id,
          geometry: new ol.geom.Point(
              ol.proj.fromLonLat([coordenada.longitud, coordenada.latitud])
          ),
      });
      marcador.setId(coordenada.id);
      
      iconos.forEach(icon => {
        if(coordenada.proveedor == icon.id){
          
          marcador.setStyle(new ol.style.Style({
            image: new ol.style.Icon({
            src: '/media/'+icon.ruta,
            scale: 0.06,
            })
        }));

        }

      })
      
    
      feature.push(marcador);
    });
  
    return feature
  }
  