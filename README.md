El repositorio esta organizado de la siguiente forma: 

1. En la carpeta [concepts](\concepts) encontramos pequeñas aplicaciones que sirven para repasar y dar luz sobre algunos de los conceptos: recursos, endpoints, y metodos de comunicación. 
2. La carpeta secureapp ejemplifica los metodos anteriores y muestra una implementación completa que además incorpora un sistema de autentificación. 
3. Carpetas que contienen una app con sus metodos de despliegue y archivos adicionales:
   1. gitway: 
      1. heroku login
      2. heroku create {appname}
      3. git remote -v  (debemos previamente haber inicializado un git en carpeta que contiene la app)
      4. git push heroku master 
   2. dockerway: 
      1. heroku login
      2. heroku create {appname}
      3. heroku container:push web --app {appname} (desde la carpeta que contiene el dockerfile y sus dependencias)
      4. heroku container:release web --app {appname}
   3. Agregamos Dynos a las apps: 
      1. heroku ps:scale web=1 --app {appname} **FREEE**

Para probar localmente, el archivo con el que se debe crear el entorno virtual es *requirements.txt*. 
Con Virtualenv (Windows):
    ```
    pip install virtualenv
    virtualenv {env}
    {env}\Scripts\activate
    pip install -r requirements.txt 
    ```
Con Conda: 
    ```
    conda create --name {env} python=3.7
    conda activate {env}
    pip install -r requirements.txt
    ```
