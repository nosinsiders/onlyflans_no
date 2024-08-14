1. Creamos un ambiente virtual en la carpeta raiz, donde vamos a crear el proyecto:

  a) Crear ambiente virtual
    python3 -m venv onlyflans_env
  b) Activarlo:
    source onlyflans_env/Scripts/activate
  c) Instalar Django:
    pip install Django

2. Crear un proyecto nuevo y entrar en la carpeta del proyecto:
  django-admin startproject onlyflans 
  cd nameproject
  code . (opcional, para abri VSC en la pantalla nueva)

3. Estando dentro de la carpeta del proyecto, realizamos la migraciones:
  a) Busca cambios:
    python manage.py makemigrations
  b) Aplica los cambios:
    python3 manage.py migrate

4. Ejecutar el servidor:
  python3 manage.py runserver
  