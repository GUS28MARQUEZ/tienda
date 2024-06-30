import sqlite3
from django.contrib.auth.models import User, Permission 
from django.db import connection 
from datetime import date, timedelta
from random import randint
from core.models import Categoria, Producto, Carrito, Perfil, Boleta, DetalleBoleta, Bodega

def eliminar_tabla(nombre_tabla):
    conexion = sqlite3.connect('db.sqlite3')
    cursor = conexion.cursor()
    cursor.execute(f"DELETE FROM {nombre_tabla}")
    conexion.commit()
    conexion.close()

def exec_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

def crear_usuario(username, tipo, nombre, apellido, correo, es_superusuario, 
    es_staff, rut, direccion, subscrito, imagen):

    try:
        print(f'Verificar si existe usuario {username}.')

        if User.objects.filter(username=username).exists():
            print(f'   Eliminar {username}')
            User.objects.get(username=username).delete()
            print(f'   Eliminado {username}')
        
        print(f'Iniciando creación de usuario {username}.')

        usuario = None
        if tipo == 'Superusuario':
            print('    Crear Superuser')
            usuario = User.objects.create_superuser(username=username, password='123')
        else:
            print('    Crear User')
            usuario = User.objects.create_user(username=username, password='123')

        if tipo == 'Administrador':
            print('    Es administrador')
            usuario.is_staff = es_staff
            
        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.email = correo
        usuario.save()

        if tipo == 'Administrador':
            print(f'    Dar permisos a core y apirest')
            permisos = Permission.objects.filter(content_type__app_label__in=['core', 'apirest'])
            usuario.user_permissions.set(permisos)
            usuario.save()
 
        print(f'    Crear perfil: RUT {rut}, Subscrito {subscrito}, Imagen {imagen}')
        Perfil.objects.create(
            usuario=usuario, 
            tipo_usuario=tipo,
            rut=rut,
            direccion=direccion,
            subscrito=subscrito,
            imagen=imagen)
        print("    Creado correctamente")
    except Exception as err:
        print(f"    Error: {err}")

def eliminar_tablas():
    eliminar_tabla('auth_user_groups')
    eliminar_tabla('auth_user_user_permissions')
    eliminar_tabla('auth_group_permissions')
    eliminar_tabla('auth_group')
    eliminar_tabla('auth_permission')
    eliminar_tabla('django_admin_log')
    eliminar_tabla('django_content_type')
    #eliminar_tabla('django_migrations')
    eliminar_tabla('django_session')
    eliminar_tabla('Bodega')
    eliminar_tabla('DetalleBoleta')
    eliminar_tabla('Boleta')
    eliminar_tabla('Perfil')
    eliminar_tabla('Carrito')
    eliminar_tabla('Producto')
    eliminar_tabla('Categoria')
    #eliminar_tabla('authtoken_token')
    eliminar_tabla('auth_user')

def poblar_bd(test_user_email=''):
    eliminar_tablas()

    crear_usuario(
        username='AraragiKoyomi',
        tipo='Cliente', 
        nombre='KOYOMI', 
        apellido='ARARAGI', 
        correo=test_user_email if test_user_email else 'AraragiKoyomi@dc.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='25.747.200-0',	
        direccion='123 Main Street, Los Angeles, \nCalifornia 90001 \nJapon', 
        subscrito=True, 
        imagen='perfiles/AraragiKoyomi.jpg')

    crear_usuario(
        username='STARLIGHTANYA',
        tipo='Cliente', 
        nombre='ANYA', 
        apellido='FORGER', 
        correo=test_user_email if test_user_email else 'STARLIGHTANYA@dc.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='12.202.357-5', 
        direccion='Albert Street, New York, \nNew York 10001 \nOstania', 
        subscrito=True, 
        imagen='perfiles/STARLIGHTANYA.jpg')

    crear_usuario(
        username='KOMI',
        tipo='Cliente', 
        nombre='SHOUKO', 
        apellido='KOMI', 
        correo=test_user_email if test_user_email else 'KOMI@dc.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='11.991.600-3', 
        direccion='105 Apple Park Way, \nCupertino, CA 95014 \nEstados Unidos', 
        subscrito=False, 
        imagen='perfiles/KOMI.jpg')

    crear_usuario(
        username='Shinji2015',
        tipo='Cliente', 
        nombre='SHINJI', 
        apellido='IKARI', 
        correo=test_user_email if test_user_email else 'Shinji2015@dc.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='16.469.725-8', 
        direccion='350 5th Ave, \nNew York, NY 10118 \nJapon', 
        subscrito=False, 
        imagen='perfiles/Shinji2015.jpg')

    crear_usuario(
        username='MadokaMagica',
        tipo='Cliente', 
        nombre='MADOKA', 
        apellido='KANAME', 
        correo=test_user_email if test_user_email else 'MadokaMagica@dc.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='16.469.725-8', 
        direccion='350 5th Ave, \nNew York, NY 10118 \nJapon', 
        subscrito=False, 
        imagen='perfiles/MadokaMagica.jpg')
    
    crear_usuario(
        username='YumekoChan',
        tipo='Cliente', 
        nombre='YUMEKO', 
        apellido='JABAMI', 
        correo=test_user_email if test_user_email else 'YumekoChan@dc.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='16.469.725-8', 
        direccion='350 5th Ave, \nNew York, NY 10118 \nJapon', 
        subscrito=False, 
        imagen='perfiles/YumekoChan.jpg')

    crear_usuario(
        username='KobayashiLover',
        tipo='Administrador', 
        nombre='TOURHU', 
        apellido='KOBAYASHI', 
        correo=test_user_email if test_user_email else 'KobayashiLover@marvel.com', 
        es_superusuario=False, 
        es_staff=True, 
        rut='19.441.980-5', 
        direccion='10 Pine Road, Miami, \nFlorida 33101 \nJapon', 
        subscrito=False, 
        imagen='perfiles/KobayashiLover.jpg')
    
    crear_usuario(
        username='FRIEREN',
        tipo='Administrador', 
        nombre='FRIEREN', 
        apellido='FLAMME', 
        correo=test_user_email if test_user_email else 'FRIEREN@marvel.com', 
        es_superusuario=False, 
        es_staff=True, 
        rut='21.708.052-5', 
        direccion='1600 Pennsylvania Avenue NW, \nWashington, D.C. \nEstados Unidos', 
        subscrito=False, 
        imagen='perfiles/mruffalo.jpg')

    crear_usuario(
        username='TheGolgenWitch',
        tipo='Superusuario',
        nombre='BEATRICE',
        apellido='CASTIGLIONI',
        correo=test_user_email if test_user_email else 'TheGolgenWitch@dc.com',
        es_superusuario=True,
        es_staff=True,
        rut='13.029.317-4',
        direccion='15 Oak Street, Los Angeles, \nCalifornia 90001 \nItalia',
        subscrito=False,
        imagen='perfiles/TheGoldenWitch.jpg')
    

    

    productos_data = [
        {
            'id': 1,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'EL HOMBRE DE ACERO(2013)',
            'descripcion': 'Ej: Clark Kent se entera de que es un alienígena con superpoderes procedente del planeta Krypton En ese momento decide asumir el papel de protector de la raza humana como SUPERMAN tomando la decisión de enfrentarse al general Zod y evitar que destruya la humanidad, Tras los sucesos de MAN OF STEEL.',
            'precio': 1000,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000001.jpg'
        },
        {
            'id': 2,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'BATMAN V SUPERMAN DAWN OF THE JUSTICE(2016)',
            'descripcion': 'SUPERMAN es visto como un dios para algunos y una amenza para otros, De entre esas personas esta BRUCE WAYNE cuya identidad es BATMAN el vigilante de GOTHAM Quiere destruirlo por VENGANZA',
            'precio': 1000,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000002.jpg'
        },
        {
            'id': 3,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'JUSTICE LEAGUE(2021)',
            'descripcion': 'Tras los sucesos de BATMAN V SUPERMAN, BRUCE WAYNE(BATMAN) y DIANA PRINCE(WONDER WOMAN) deciden unir a unos superheroes ARTHUR CURRY(AQUAMAN) BARRY ALLEN(FLASH) VICTOR STONE(CYBORG) para detener a una amenza llamada STEPPENWOLF que viene a recolectar las cajas madres para atraer a una amenaza mayor.',
            'precio': 1000,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000003.jpg'
        }
    ]

    print('Crear productos')
    for producto in productos_data:
        Producto.objects.create(**producto)
    print('Productos creados correctamente')

    print('Crear carritos')
    for rut in ['25.747.200-0', '11.991.600-3']:
        cliente = Perfil.objects.get(rut=rut)
        for cantidad_productos in range(1, 11):
            producto = Producto.objects.get(pk=randint(1, 10))
            if cliente.subscrito:
                descuento_subscriptor = producto.descuento_subscriptor
            else:
                descuento_subscriptor = 0
            descuento_oferta = producto.descuento_oferta
            descuento_total = descuento_subscriptor + descuento_oferta
            descuentos = int(round(producto.precio * descuento_total / 100))
            precio_a_pagar = producto.precio - descuentos
            Carrito.objects.create(
                cliente=cliente,
                producto=producto,
                precio=producto.precio,
                descuento_subscriptor=descuento_subscriptor,
                descuento_oferta=descuento_oferta,
                descuento_total=descuento_total,
                descuentos=descuentos,
                precio_a_pagar=precio_a_pagar
            )
    print('Carritos creados correctamente')

    print('Crear boletas')
    nro_boleta = 0
    perfiles_cliente = Perfil.objects.filter(tipo_usuario='Cliente')
    for cliente in perfiles_cliente:
        estado_index = -1
        for cant_boletas in range(1, randint(6, 21)):
            nro_boleta += 1
            estado_index += 1
            if estado_index > 3:
                estado_index = 0
            estado = Boleta.ESTADO_CHOICES[estado_index][1]
            fecha_venta = date(2023, randint(1, 5), randint(1, 28))
            fecha_despacho = fecha_venta + timedelta(days=randint(0, 3))
            fecha_entrega = fecha_despacho + timedelta(days=randint(0, 3))
            if estado == 'Anulado':
                fecha_despacho = None
                fecha_entrega = None
            elif estado == 'Vendido':
                fecha_despacho = None
                fecha_entrega = None
            elif estado == 'Despachado':
                fecha_entrega = None
            boleta = Boleta.objects.create(
                nro_boleta=nro_boleta, 
                cliente=cliente,
                monto_sin_iva=0,
                iva=0,
                total_a_pagar=0,
                fecha_venta=fecha_venta,
                fecha_despacho=fecha_despacho,
                fecha_entrega=fecha_entrega,
                estado=estado)
            detalle_boleta = []
            total_a_pagar = 0
            for cant_productos in range(1, randint(4, 6)):
                producto_id = randint(1, 10)
                producto = Producto.objects.get(id=producto_id)
                precio = producto.precio
                descuento_subscriptor = 0
                if cliente.subscrito:
                    descuento_subscriptor = producto.descuento_subscriptor
                descuento_oferta = producto.descuento_oferta
                descuento_total = descuento_subscriptor + descuento_oferta
                descuentos = int(round(precio * descuento_total / 100))
                precio_a_pagar = precio - descuentos
                bodega = Bodega.objects.create(producto=producto)
                DetalleBoleta.objects.create(
                    boleta=boleta,
                    bodega=bodega,
                    precio=precio,
                    descuento_subscriptor=descuento_subscriptor,
                    descuento_oferta=descuento_oferta,
                    descuento_total=descuento_total,
                    descuentos=descuentos,
                    precio_a_pagar=precio_a_pagar)
                total_a_pagar += precio_a_pagar
            monto_sin_iva = int(round(total_a_pagar / 1.19))
            iva = total_a_pagar - monto_sin_iva
            boleta.monto_sin_iva = monto_sin_iva
            boleta.iva = iva
            boleta.total_a_pagar = total_a_pagar
            boleta.fecha_venta = fecha_venta
            boleta.fecha_despacho = fecha_despacho
            boleta.fecha_entrega = fecha_entrega
            boleta.estado = estado
            boleta.save()
            print(f'    Creada boleta Nro={nro_boleta} Cliente={cliente.usuario.first_name} {cliente.usuario.last_name}')
    print('Boletas creadas correctamente')

    print('Agregar productos a bodega')
    for producto_id in range(1, 11):
        producto = Producto.objects.get(id=producto_id)
        cantidad = 0
        for cantidad in range(1, randint(2, 31)):
            Bodega.objects.create(producto=producto)
        print(f'    Agregados {cantidad} "{producto.nombre}" a la bodega')
    print('Productos agregados a bodega')

