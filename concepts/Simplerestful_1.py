from flask import Flask, request
from flask_restful import Resource, Api, reqparse   ## Un recurso es algo que nuestra API puede crear, modificar, devolver, etc. 

app = Flask(__name__) 
api = Api(app) ### Nos permite agregar y controlar los recursos con facilidad. 

### Api funciona como sobre recursos y cada recurso debe ser una clase. 


class BigPeople(Resource): ### heredamos algunos metodos y atributos de la clase Resource: es una copia con cambios
    def get(self, name):  ### Defino el verbo y que va a hacer 
        return {'bigpeople': name}

api.add_resource(BigPeople, '/bigpeople/<string:name>')

app.run(port=5000, debug=True)  ### El recurso se vuelve accesible a tráves del Api: No tenemos la necesidad de definir endpoints

### Pasos: 
#### 1. Definir el API
#### 2. Definir y crear los recursos.
#### 3. Definir los metodos para los recursos y que haran cuando son alcanzados sus endpoints
#### 4. Se agrega el recurso y parametros. 