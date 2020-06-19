El repositorio esta organizado de la siguiente forma: 

1. En la carpeta [concepts](\concepts) encontramos pequeñas aplicaciones que sirven para repasar y dar luz sobre algunos de los conceptos: recursos, endpoints, y metodos de comunicación. 
2. La carpeta secureapp ejemplifica los metodos anteriores y muestra una implementación completa que además incorpora un sistema de autentificación. 
3. Carpetas que contienen una app con sus metodos de despliegue y archivos adicionales, los pasos respectivos para desplegar estás apps son:
   1. Mediante [Git](gitway): 
      1. heroku login
      2. heroku create {appname}
      3. git remote -v  (debemos previamente haber inicializado un git en carpeta que contiene la app)
      4. git push heroku master 
   2. Mediante [Docker](dockerway): 
      1. heroku login
      2. heroku create {appname}
      3. heroku container:push web --app {appname} (desde la carpeta que contiene el dockerfile y sus dependencias)
      4. heroku container:release web --app {appname}
   3. Agregamos Dynos a las apps: 
      1. heroku ps:scale web=1 --app {appname} **FREEE**

En ambos casos se debe poseer  una cuenta en [Heroku](https://www.heroku.com/) y descargar el CLI.

Para probar localmente, tenemos el archivo de [dependencias](requirements.txt). 

Con virtualenv (Windows):

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

