

function calcular_metros(){
    metros_cuadrados = document.getElementById("metros_cuadrados")
    altura = $('#altura').val()
    largo = $("#largo").val()

    metros_final = largo * altura
    metros_cuadrados.value = metros_final
 
    
}