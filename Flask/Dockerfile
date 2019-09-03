FROM python:3.5
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD ["gunicorn", "-c", "gunicorn.ini", "wsgi:app"]











#historial de versiones históricas:
#0) la primera mejora en el dockerfile consistió en mejorar la carga de las imágenes aprovechando el caché.
#por lo tanto se cargaron los requirements para su instalación inmediata antes de el comandos
#COPY . /app
#lo anterior implica que al realizar cambios en el proyecto, cambios que no sean en requirements.txt, cargarán
#más rápido debido a que no se ejecutan los pip install.

#1) durante la primera versión la aplicación solo se encontraba en stage dev por lo tanto
#la conexión con lenguaje wsgi no se realizaba y funcionaba solo como un flask + postgres. aquí los comandos de despliegue:
#ENTRYPOINT ["python"]
#CMD ["app/app.py"]

#2) se integra wsgi por lo tanto se ingresa el comando
#CMD ["gunicorn", "-c", "gunicorn.ini", "wsgi:app"]
#ahora levantamos el sistema usando gunicorn
#flag --c es config y elegimos el archivo de configuracion gunicorn.ini
#elegimos wsgi:app como archivo. se activa wsgi.py, que importa y ejecuta run sobre la aplicación que.
#osea ahora llegarán peticiones desde swgi que ejecutará las respuestas de la aplicación como funciones.










#
