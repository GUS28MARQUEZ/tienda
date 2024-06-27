// Crear funcion ready
$(document).ready(function() {
  
    // Crear evento de click del boton usando su id #btn-obtener-recetas
    $('#btn-obtener-peliculas').click(function() {
      
      // Crear invocación a la API donde se obtienen los datos
      $.get('https://www.themealdb.com/api/json/v1/1/categories.php', function(data) {
  
        $('#tabla-peliculas-tbody').empty();
  
        // Recorrer los datos usando $each
        $.each(data.categories, function(i, item) {
  
          // Crear el codigo HTML para agegar filas a la tabla usando los campos de cada fila
          var fila = `
            <tr>
              <td> ${item.idCategory} </td>
              <td> ${item.strCategory} </td>
              <td> <img src="${item.strCategoryThumb}"> </td>
              <td> ${item.strCategoryDescription} </td>
            </tr>
          `;
  
          $('#tabla-peliculas-tbody').append(fila);
        });
      });
    });
  });
  
  // Puedes probar otras APIs en http://jsonplaceholder.typicode.com