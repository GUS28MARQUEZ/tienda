$(document).ready(function() {

    // Cambiar el texto del combo de categoría por "Seleccione una categoría"
    var select = document.querySelector('select[name="categoria"]');
    if (select) {
        var defaultOption = select.querySelector('option[value=""]');
        if (defaultOption) {
            defaultOption.text = "Seleccione una categoría";
        }
    }

    // Asignar placeholders para ayudar a los usuarios
    $('#id_nombre').attr('placeholder', 'Ej: EL HOMBRE DE ACERO(2013), BATMAN V SUPERMAN DAWN OF THE JUSTICE(2016), JUSTICE LEAGUE(2021)');
    $('#id_descripcion').attr('placeholder', 'Ej: Clark Kent se entera de que es un alienígena con superpoderes procedente del planeta Krypton En ese momento decide asumir el papel de protector de la raza humana como SUPERMAN tomando la decisión de enfrentarse al general Zod y evitar que destruya la humanidad, Tras los sucesos de MAN OF STEEL, SUPERMAN es visto como un dios para algunos y una amenza para otros, De entre esas personas esta BRUCE WAYNE cuya identidad es BATMAN el vigilante de GOTHAM Quiere destruirlo por VENGANZA, Tras los sucesos de BATMAN V SUPERMAN, BRUCE WAYNE(BATMAN) y DIANA PRINCE(WONDER WOMAN) deciden unir a unos superheroes ARTHUR CURRY(AQUAMAN) BARRY ALLEN(FLASH) VICTOR STONE(CYBORG) para detener a una amenza llamada STEPPENWOLF que viene a recolectar las cajas madres para atraer a una amenaza mayor');
    $('#id_precio').attr('placeholder', 'Ej: 1000');
    $('#id_descuento_subscriptor').attr('placeholder', 'Ej: 10');
    $('#id_descuento_oferta').attr('placeholder', 'Ej: 5');

    // Agregar una validación por defecto para que la imagen la exija como campo obligatorio
    $.extend($.validator.messages, {
        required: "Este campo es requerido",
    });

    // Agregar validación para que la suma de los descuentos no supere el 100%
    $.validator.addMethod('sumaDescuentos', function(value, element) {
        
        var descuentoSubscriptor = parseFloat($('#id_descuento_subscriptor').val());
        var descuentoOferta = parseFloat($('#id_descuento_oferta').val());
        var sumaDescuentos = descuentoSubscriptor + descuentoOferta;
        
        if (isNaN(descuentoSubscriptor) || isNaN(descuentoOferta)) return true;

        return sumaDescuentos <= 100;

    }, 'La suma de los descuentos no puede superar el 100%');

    $('#form').validate({ 
        rules: {
            'categoria': {
                required: true,
            },
            'nombre': {
                required: true,
            },
            'descripcion': {
                required: true,
            },
            'precio': {
                required: true,
                digits: true,
                number: true,
            },
            'descuento_subscriptor': {
                required: true,
                digits: true,
                number: true,
                range: [0, 100],
                sumaDescuentos: true,
            },
            'descuento_oferta': {
                required: true,
                digits: true,
                number: true,
                range: [0, 100],
                sumaDescuentos: true,
            },
        },
        messages: {
            'categoria': {
                required: 'Debe ingresar la categoría del producto',
            },
            'nombre': {
                required: 'Debe ingresar el nombre del producto',
            },
            'descripcion': {
                required: 'Debe ingresar la descripción del producto',
            },
            'precio': {
                required: 'Debe ingresar el precio del producto',
                number: 'Debe ingresar un número',
                digits: 'Debe ingresar un número entero',
            },
            'descuento_subscriptor': {
                required: 'Debe ingresar el % de descuento para subscriptores',
                number: 'Debe ingresar un número',
                digits: 'Debe ingresar un número entero',
                range: 'El descuento debe ser un número entre 0 y 100',
            },
            'descuento_oferta': {
                required: 'Debe ingresar el % de descuento para ofertas',
                number: 'Debe ingresar un número',
                digits: 'Debe ingresar un número entero',
                range: 'El descuento debe ser un número entre 0 y 100',
            },
        },
        errorPlacement: function(error, element) {
            error.insertAfter(element); // Inserta el mensaje de error después del elemento
            error.addClass('error-message'); // Aplica una clase al mensaje de error
        },
    });

});
