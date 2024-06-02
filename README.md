# Dokit Test - Sistema de Registro de Doctores y Oficinas

Dokit Test es una aplicación web diseñada para facilitar el registro y la gestión de doctores y sus respectivas oficinas. Con Dokit Test, puedes crear, actualizar y eliminar registros oficinas de manera eficiente y sencilla, así como crear y ver la lista de doctores.

## Características

- Registro de Doctores: Permite registrar nuevos doctores proporcionando información básica como nombre, apellidos y correo electrónico.
- Registro de Oficinas: Permite registrar nuevas oficinas asociadas a un doctor(email), especificando detalles como la dirección.
- Actualización y Eliminación: Facilita la actualización y eliminación de registros oficinas existentes.
- Interfaz Intuitiva: Ofrece una interfaz fácil de usar para una navegación fluida y una experiencia de usuario agradable.

## Requisitos

- Python 3.10.12
- Django 5.0.6

## Instalación

1. Clona el repositorio de Dokit en tu máquina local.
```bash
pip install -r requirements.txt
```

2. Instala los requisitos del proyecto utilizando pip:
```bash
pip install -r requirements.txt
```

3. Realiza las migraciones de la base de datos:
```bash
python manage.py migrate
```

4. Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

5. Abre tu navegador web y visita `http://localhost:8000` para acceder a la aplicación.

## Base de Datos
Este proyecto utiliza SQLite3 como base de datos. No se requiere ninguna configuración adicional, ya que SQLite3 es una base de datos ligera y se incluye automáticamente con Python.

## Uso

- Login: Puede iniciar sesion con email y password los doctores registrados.
- Registro de Doctores: Haz clic en el enlace "Register Doctor" en el dashboard para agregar un nuevo doctor proporcionando la información requerida.
- Registro de Oficinas: Haz clic en el enlace "Register Office" en el dashboard para agregar una nueva oficina asociada a un doctor existente.
- Actualización y Eliminación: Utiliza los enlaces "Edit" y "Delete" en el dashboard para actualizar o eliminar registros de  oficinas.

## Créditos

Desarrollado por Liliana Martinez para Dokit.


