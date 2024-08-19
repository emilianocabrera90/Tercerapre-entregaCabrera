# Proyecto Django

## Requisitos

- Python
- Django

## Instalación

1. Clona el repositorio o descarga el proyecto.
2. Instala las dependencias:
    ```bash
    pip install django
    ```
3. Realiza las migraciones:
    ```bash
    python manage.py migrate
    ```
4. Ejecuta el servidor:
    ```bash
    python manage.py runserver
    ```

## Uso

1. Visita [http://127.0.0.1:8000/insert/](http://127.0.0.1:8000/insert/) para insertar datos.
2. Visita [http://127.0.0.1:8000/search/](http://127.0.0.1:8000/search/) para buscar datos en la base de datos.

## Estructura del Proyecto

- `myapp/models.py`: Definición de modelos.
- `myapp/forms.py`: Formularios para insertar y buscar datos.
- `myapp/views.py`: Lógica de las vistas.
- `myapp/urls.py`: Configuración de URLs para la aplicación.
- `templates/myapp/`: Plantillas HTML.
