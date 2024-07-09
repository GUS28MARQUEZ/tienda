$(document).ready(function() {
  $.get('https://www.themoviedb.org/api/v1/movies', function(data) {
           
    alert(data);      

// Recorrer los datos usando $each

$.each(data.results, function(i, item) {

  // Crear el codigo HTML para agegar filas a la tabla usando los campos de cada fila
  
html=`
<div class="container-fluid">
        <div class="row">
            <div class="col-sm-12 col-md-7 col-xl-6" style="height: 500px;">
                <img class="ficha_foto" src="${item.image}" alt="${item.title})">
            </div>
            <div class="col-sm-12 col-md-5 col-xl-6">
                <div class="ficha_titulo">
                    ${item.title}
                    <p class="card-text">
                        ${item.description}</p>
                </div>
                <div class="ficha_disponible">
                    DISPONIBLE
                </div>
                <div class="ficha_precio">
                    $1.000
                </div>
                <a href="MisCompras.html" class="btn btn-primary">COMPRAR AHORA</a>
                <a href="index.html" class="btn btn-primary">CANCELAR COMPRA</a>
            </div>
        </div>
    </div>
`;

 $('#comprar-ahora').click(function() {
   $('#accion').val('comprar-ahora');
   $('#formulario-ficha').submit();
 });
 $('#agregar-al-carrito').click(function() {
   $('#accion').val('agregar-al-carrito');
   $('#formulario-ficha').submit();
 });
});
});
});