latitud = document.getElementById("latitud")
longitud = document.getElementById("longitud")

latitud.addEventListener("keyup", function(){
    const coma = ','
    if (this.value.includes(coma)){
        alert("LA LATITUD: '"+ this.value + "' NO DEBE INCLUIR COMA");
    }
    
});

longitud.addEventListener("keyup", function(){
    const coma = ','
    if (this.value.includes(coma)){
        alert("LA LONGITUD: '"+ this.value + "' NO DEBE INCLUIR COMA");
    }
    
});

