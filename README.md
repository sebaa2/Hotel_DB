Alumnos:  Dario Araneda
          Hector Campos
          Sebastian Cisternas
          
# 🏨 HotelDB - Sistema de Gestión Hotelera

Un sistema completo de gestión hotelera desarrollado con Django que permite administrar reservas, habitaciones, clientes, empleados y hoteles de manera eficiente.

## 📋 Descripción del Proyecto

HotelDB es una aplicación web CRM (Customer Relationship Management) diseñada específicamente para la industria hotelera. Permite gestionar todos los aspectos operativos de uno o múltiples hoteles desde una interfaz centralizada.

### Características Principales

- 🏨 **Gestión de Hoteles**: Administra múltiples propiedades hoteleras
- 🛏️ **Control de Habitaciones**: Gestiona tipos, precios y disponibilidad
- 📅 **Sistema de Reservas**: Reservas con check-in/check-out
- 👥 **Gestión de Clientes**: Base de datos completa de clientes
- 👔 **Administración de Empleados**: Control de personal por hotel
- 🔐 **Sistema de Autenticación**: Registro y login de usuarios
- 📊 **Interfaz Intuitiva**: Diseño responsive con Bootstrap

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 4.2.4
- **Base de Datos**: MySQL/MariaDB
- **Frontend**: 
  - HTML5, CSS3
  - Bootstrap 5.3.2
  - jQuery 3.7.0
  - DataTables 1.13.6
  - Font Awesome 6.4.2
- **ORM**: Django ORM
- **Autenticación**: Django Auth System

## 📦 Instalación

### Requisitos Previos

```bash
Python 3.8 o superior
MySQL/MariaDB
pip (gestor de paquetes de Python)
virtualenv (recomendado)
```

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone <url-del-repositorio>
cd HotelDB
```

2. **Crear y activar entorno virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install django==4.2.4
pip install mysqlclient
# O usar requirements.txt si está disponible
pip install -r requirements.txt
```

4. **Configurar la base de datos**

Crear la base de datos en MySQL:
```sql
CREATE DATABASE hoteldb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'hoteluser'@'localhost' IDENTIFIED BY 'tu_contraseña';
GRANT ALL PRIVILEGES ON hoteldb.* TO 'hoteluser'@'localhost';
FLUSH PRIVILEGES;
```

Actualizar `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hoteldb',
        'USER': 'hoteluser',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. **Aplicar migraciones**
```bash
python manage.py migrate
```

6. **Crear superusuario (opcional)**
```bash
python manage.py createsuperuser
```

7. **Ejecutar el servidor**
```bash
python manage.py runserver
```

8. **Acceder a la aplicación**
```
http://localhost:8000
```

## 📁 Estructura del Proyecto

```
HotelDB/
├── CRM/                          # Aplicación principal
│   ├── migrations/              # Migraciones de base de datos
│   ├── __init__.py
│   ├── admin.py                # Configuración del admin
│   ├── apps.py                 # Configuración de la app
│   ├── datos_globales.py       # Context processors
│   ├── forms.py                # Formularios Django
│   ├── models.py               # Modelos de datos
│   ├── tests.py                # Tests
│   └── views.py                # Vistas y lógica de negocio
├── Templates/                   # Plantillas HTML
│   ├── crm/
│   │   ├── principal.html      # Página principal
│   │   ├── reserva.html        # Gestión de reservas
│   │   ├── cliente.html        # Lista de clientes
│   │   ├── hotel.html          # Lista de hoteles
│   │   ├── habitacion.html     # Gestión de habitaciones
│   │   ├── empleados.html      # Lista de empleados
│   │   ├── crear_reserva.html  # Formulario de reserva
│   │   ├── crear_clientes.html # Formulario de cliente
│   │   ├── interfaz.html       # Plantilla base
│   │   └── ...
│   └── registration/
│       ├── login.html          # Página de login
│       └── registro.html       # Página de registro
├── static/                      # Archivos estáticos
│   └── images/
│       ├── palmtree.jpg        # Imagen de fondo
│       ├── tree.png            # Logo
│       ├── fb_64x64.png        # Ícono Facebook
│       ├── ig_64x64.png        # Ícono Instagram
│       └── x_64x64.png         # Ícono Twitter/X
├── manage.py
└── settings.py
```

## 💾 Modelos de Datos

### Hotel
```python
- idhotel (PK)
- nombre
- direccion
- celular
- correo
```

### Cliente
```python
- idcliente (PK)
- nombre
- direccion
- celular
- correo
```

### Habitacion
```python
- idhabitacion (PK)
- tipo
- precio
- estado
- hotel_idhotel (FK)
```

### Empleados
```python
- idempleados (PK)
- nombre
- puesto
- salario
- hotel_idhotel (FK)
```

### Reserva
```python
- idreserva (PK, AutoField)
- fecha_chekin
- fecha_chekout
- estado_reserva
- hotel_idhotel (FK)
- cliente_idcliente (FK)
```

## 🚀 Uso del Sistema

### Página Principal
- **URL**: `/` o `/principal/`
- Vista inicial con navegación principal
- Acceso rápido a todas las secciones
- Diseño atractivo con fondo de playa

### Sistema de Autenticación

#### Registro de Usuario
- **URL**: `/registro/`
- Crear cuenta nueva
- Formulario personalizado de Django
- Auto-login después del registro

#### Inicio de Sesión
- **URL**: `/login/`
- Autenticación de usuarios
- Redirección a página principal

### Gestión de Reservas

#### Listar Reservas
- **URL**: `/lista-reserva/`
- Visualiza todas las reservas
- Tabla con DataTables (búsqueda, ordenamiento)
- Opciones: Editar, Eliminar

#### Crear Reserva
- **URL**: `/crear_reserva/`
- Flujo completo:
  1. Registrar cliente (si es nuevo)
  2. Seleccionar hotel
  3. Definir estado de reserva
  4. Confirmar reserva

#### Editar Reserva
- **URL**: `/editar-reserva/<id>/`
- Modificar datos de reserva existente
- Validación de formularios

#### Eliminar Reserva
- **URL**: `/eliminar-reserva/<id>/`
- Confirmación antes de eliminar
- Eliminación permanente de la base de datos

### Gestión de Clientes

#### Listar Clientes
- **URL**: `/lista-clientes/`
- Todos los clientes registrados
- Información completa (ID, nombre, contacto)

#### Registrar Cliente
- **URL**: `/registrar-clientes/`
- Formulario completo:
  - Nombre
  - Dirección
  - RUT
  - Email
  - Celular
- Redirección automática a crear reserva

### Gestión de Hoteles

#### Listar Hoteles
- **URL**: `/lista-hotel/`
- Visualiza todos los hoteles del sistema
- Información de contacto

### Gestión de Habitaciones

#### Listar Habitaciones
- **URL**: `/lista-habitacion/`
- Todas las habitaciones
- Información: tipo, precio, estado, hotel
- Estado: disponible/ocupada

### Gestión de Empleados

#### Listar Empleados
- **URL**: `/lista-empleados/`
- Personal de todos los hoteles
- Información: nombre, puesto, hotel asignado

## 🎨 Características del Frontend

### Diseño Responsive
- Bootstrap 5.3.2
- Adaptable a móviles, tablets y desktop
- Navegación hamburguesa en móviles

### Componentes Interactivos
- **DataTables**: Tablas con búsqueda y paginación
- **Marquee**: Banner animado con mensajes
- **Modales**: Confirmaciones de eliminación
- **Alerts**: Mensajes informativos

### Estilo Visual
- Fondo tropical con palmeras
- Colores vibrantes (turquesa, verde, naranja)
- Iconos Font Awesome
- Footer con redes sociales

## 🔐 Seguridad

### Autenticación
- Sistema integrado de Django Auth
- Contraseñas hasheadas
- Validación de formularios
- CSRF Protection habilitado

### Autorización
- Control de acceso por usuario
- Sesiones seguras
- Protección contra inyección SQL (ORM)

## 📊 Características Técnicas

### DataTables Integration
```javascript
$(document).ready(function() {
    $('table').DataTable();
});
```

### AJAX para Eliminación
```javascript
$('.eliminar-reserva').click(function(e) {
    e.preventDefault();
    var confirma = confirm('¿Estás seguro?');
    if (confirma) {
        window.location.href = '/eliminar-reserva/' + id + '/';
    }
});
```

### Context Processors
```python
def datos_globales(request):
    return {
        'nombre_completo': request.session.get('nombre_completo', 'Invitado')
    }
```

## 🔧 Configuración Avanzada

### URLs Configuration

```python
# urls.py
urlpatterns = [
    path('', views.principal, name='principal'),
    path('registro/', views.registro, name='registro'),
    path('lista-reserva/', views.listar_reserva, name='reserva'),
    path('lista-clientes/', views.listar_cliente, name='clientes'),
    path('lista-hotel/', views.listar_hotel, name='hotel'),
    path('lista-habitacion/', views.listar_habitacion, name='habitacion'),
    path('lista-empleados/', views.listar_empleados, name='empleados'),
    path('registrar-clientes/', views.registrarCliente, name='registrar_cliente'),
    path('agregarclientes/', views.AgregarCliente, name='agregar_cliente'),
    path('crear_reserva/', views.crearReserva, name='crear_reserva'),
    path('editar-reserva/<int:idreserva>/', views.editarReserva, name='editar_reserva'),
    path('eliminar-reserva/<int:idreserva>/', views.eliminar_reservar, name='eliminar_reserva'),
]
```

### Settings Configuration

```python
# settings.py

# Context Processors
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                'CRM.datos_globales.datos_globales',
            ],
        },
    },
]

# Static Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media Files (si es necesario)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## 🐛 Solución de Problemas

### Error de Conexión a MySQL
```bash
# Instalar mysqlclient
pip install mysqlclient

# En Windows, si hay problemas:
pip install pymysql
# Luego en __init__.py del proyecto:
import pymysql
pymysql.install_as_MySQLdb()
```

### Migraciones no Aplicadas
```bash
# Verificar migraciones pendientes
python manage.py showmigrations

# Aplicar migraciones
python manage.py migrate

# Si hay conflictos:
python manage.py makemigrations
python manage.py migrate --fake-initial
```

### Error "managed = False"
Los modelos tienen `managed = False` porque fueron generados desde una BD existente. Para permitir que Django gestione las tablas:
```python
class Meta:
    managed = True  # Cambiar a True
    db_table = 'nombre_tabla'
```

### Archivos Estáticos no se Cargan
```bash
# Recolectar archivos estáticos
python manage.py collectstatic

# Verificar STATIC_URL y STATICFILES_DIRS en settings.py
```

## 📈 Mejoras Futuras

### Funcionalidades Pendientes
- [ ] Sistema de check-in/check-out automático
- [ ] Cálculo automático de precios
- [ ] Sistema de descuentos y promociones
- [ ] Gestión de servicios adicionales
- [ ] Reportes y estadísticas
- [ ] Integración con pasarelas de pago
- [ ] Notificaciones por email
- [ ] API REST para integración externa
- [ ] Sistema de reviews y calificaciones
- [ ] Dashboard con gráficos

### Optimizaciones
- [ ] Implementar caché de consultas
- [ ] Optimización de queries (select_related, prefetch_related)
- [ ] Compresión de archivos estáticos
- [ ] Implementar búsqueda avanzada
- [ ] Filtros dinámicos en listados

## 🔄 Workflow de Desarrollo

### Flujo de Trabajo Típico

1. **Configuración Inicial**
   - Instalar dependencias
   - Configurar base de datos
   - Aplicar migraciones

2. **Desarrollo**
   - Crear modelos en `models.py`
   - Generar migraciones
   - Crear formularios en `forms.py`
   - Implementar vistas en `views.py`
   - Diseñar templates HTML

3. **Testing**
   - Probar funcionalidades
   - Verificar validaciones
   - Comprobar responsive design

4. **Despliegue**
   - Configurar servidor de producción
   - Actualizar settings.py
   - Recolectar archivos estáticos
   - Configurar servidor web (Apache/Nginx)

## 📚 Recursos Adicionales

### Django Documentation
- [Django Official Docs](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)
- [Django Forms](https://docs.djangoproject.com/en/4.2/topics/forms/)

### Bootstrap
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/)
- [Bootstrap Components](https://getbootstrap.com/docs/5.3/components/)

### DataTables
- [DataTables Documentation](https://datatables.net/)
- [DataTables Examples](https://datatables.net/examples/)

## 🤝 Contribuciones

Las contribuciones son bienvenidas:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📝 Convenciones de Código

### Python/Django
- Seguir PEP 8
- Nombres de clases en PascalCase
- Nombres de funciones en snake_case
- Docstrings en funciones complejas

### HTML/CSS
- Indentación de 4 espacios
- Nombres de clases descriptivos
- Uso de Bootstrap cuando sea posible

### JavaScript
- Usar jQuery para manipulación DOM
- Comentar código complejo
- Separar lógica en funciones

## ⚖️ Licencia

Este proyecto está bajo una licencia de código abierto. Consulta el archivo `LICENSE` para más detalles.

## 👤 Información del Proyecto

Sistema desarrollado para la gestión integral de hoteles, permitiendo:
- Administración centralizada de múltiples propiedades
- Control completo de reservas y clientes
- Gestión de recursos humanos
- Interface amigable para operadores

## 🙏 Agradecimientos

- Django Framework por el robusto backend
- Bootstrap por los componentes UI
- DataTables por las tablas interactivas
- Font Awesome por los iconos
- Comunidad de desarrolladores Django

## 📞 Soporte

Para preguntas o problemas:
- Abrir un Issue en GitHub
- Consultar la documentación de Django
- Revisar logs del servidor

---

**Desarrollado con ❤️ para la industria hotelera**

## 📊 Estado del Proyecto

**Versión**: 1.0  
**Estado**: En Desarrollo Activo  
**Última Actualización**: 2023  

---

**Nota**: Este proyecto utiliza modelos con `managed = False` que fueron generados desde una base de datos existente. Asegúrate de tener la estructura de base de datos correcta antes de ejecutar.

## 🎯 Roadmap

### Q1 2024
- ✅ Sistema básico de reservas
- ✅ Gestión de clientes
- ✅ Autenticación de usuarios
- 🔄 Sistema de reportes

### Q2 2024
- [ ] Dashboard administrativo
- [ ] API REST
- [ ] Aplicación móvil
- [ ] Integración de pagos

---

**¡Bienvenido a HotelDB! 🏨✨**
