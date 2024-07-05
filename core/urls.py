from django.urls import path

from .views import inicio, index,registrarme, nosotros, productos
from .views import usuarios, bodega, ventas, boleta, ingresar, usuarios
from .views import misdatos, miscompras, salir, carrito, ficha, ManOfSteel, BatmanVSuperman, JusticeLeague
from .views import cambiar_estado_boleta, poblar, obtener_productos, eliminar_producto_en_bodega
from .views import premio, eliminar_producto_en_carrito, agregar_producto_al_carrito
from .views import vaciar_carrito, mipassword, cambiar_password, comprar_ahora


# from .views import index, registrarme, nosotros, admin_productos
# from .views import admin_usuarios, admin_bodega, ventas, boleta, ingresar, admin_usuarios
# from .views import misdatos, miscompras, salir, carrito, ficha
# from .views import cambiar_estado_boleta, poblar, obtener_productos, eliminar_producto_en_bodega
# from .views import premio, eliminar_producto_en_carrito, agregar_producto_al_carrito
# from .views import vaciar_carrito, mipassword, cambiar_password

urlpatterns = [
    path('inicio', inicio, name='inicio'),
     path('index', index, name='index'),
    path('registrarme', registrarme, name='registrarme'),
    path('nosotros', nosotros, name='nosotros'),
    path('productos/<accion>/<id>', productos, name='productos'),
    path('usuarios/<accion>/<id>', usuarios, name='usuarios'),
    path('cambiar_password', cambiar_password, name='cambiar_password'),
    path('bodega', bodega, name='bodega'),
    path('obtener_productos', obtener_productos, name='obtener_productos'),
    path('eliminar_producto_en_bodega/<bodega_id>', eliminar_producto_en_bodega, name='eliminar_producto_en_bodega'),
    path('ventas', ventas, name='ventas'),
    path('boleta/<nro_boleta>', boleta, name='boleta'),
    path('cambiar_estado_boleta/<nro_boleta>/<estado>', cambiar_estado_boleta, name='cambiar_estado_boleta'),
    path('ingresar', ingresar, name='ingresar'),
    path('misdatos', misdatos, name='misdatos'),
    path('mipassword', mipassword, name='mipassword'),
    path('miscompras', miscompras, name='miscompras'),
    path('salir', salir, name='salir'),
    path('carrito', carrito, name='carrito'),
    path('eliminar_producto_en_carrito/<carrito_id>', eliminar_producto_en_carrito, name='eliminar_producto_en_carrito'),
    path('vaciar_carrito', vaciar_carrito, name='vaciar_carrito'),
    path('agregar_producto_al_carrito/<producto_id>', agregar_producto_al_carrito, name='agregar_producto_al_carrito'),
    path('ficha/<producto_id>', ficha, name='ficha'),
    path('ficha/<producto_id>', ManOfSteel, name='ManOfSteel'),
    path('ficha/<producto_id>', BatmanVSuperman, name='BatmanVSuperman'),
    path('ficha/<producto_id>', JusticeLeague, name='JusticeLeague'),
    path('comprar_ahora', comprar_ahora, name='comprar_ahora'),
    path('premio', premio, name='premio'),
    path('poblar', poblar, name='poblar'),
]