// INICIO funcion ready
$(document).ready(function() {
  
    // Crear evento de click del boton usando su id #btn-obtener-usuarios
  
      // Crear invocación a la API donde se obtienen los datos
      $.get('https://freetestapi.com/api/v1/movies', function(data) {
           
            alert(data);      
  
        // Recorrer los datos usando $each

        $.each(data.results, function(i, item) {
  
          // Crear el codigo HTML para agegar filas a la tabla usando los campos de cada fila
          
        html=`
        <div class="col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-3 text-center">
                <div class="card" style="width: 15rem;">
                    <img src="${item.image}" style="width: 100px; margin: auto;" class="card-img-top pt-3">
                    <div class="card-body">
                        <h5 class="card-title">
                            ${item.title}
                        </h5>
                        <h6>
                            ${item.category}
                        </h6>
                        <p class="card-text">
                            ${item.description}
                        </p>
                        <a class="btn btn-primary" target="_blank"
                            href="https://www.max.com/cl/es/channel/dc.${item.title}">
                            Buscar en MAX
                        </a>
                    </div>
                </div>
            </div>
        `;

        $('#fila-Pelicula').append(html)
      });  
    });    
  });

    // INICIO consumo API "http://fakestoreapi.com/products"
    
        // Limpiar fila de ropa

        // INICIO $each para recorrer los registros con la ropa

            // Crear string con HTML de un "card de bootstrap" para formatear ropa

            // Agregar string con el card a fila de ropa

        // FIN $each

    // FIN consumo API
     
// FIN funcion ready