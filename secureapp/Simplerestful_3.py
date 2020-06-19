from flask import Flask, request
from typing import List
from flask_restful import Resource, Api, reqparse   ## Un recurso es algo que nuestra API puede crear, modificar, devolver, etc. 
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

### FLASK JWT : json web token: obsfuscation of data, encoding. 
### User: entidad con id unico nos envia (nombre,  contraseña) y les devolvemos un jwt. Con el jwt pueden enviarnos cualquier solicitud 
### puesto que sabemos que se han identificado previamente. 

app = Flask(__name__) 
app.secret_key = "data" ### En producción no se hace esto. 
api = Api(app) ### Nos permite agregar y controlar los recursos con facilidad. 

### Api funciona como sobre recursos y cada recurso debe ser una clase. 

jwt = JWT(app, authenticate, identity) # /auth (user, password) -> autentificacion: devuelve un jwt token

datalyticsCol = []


class Area(Resource): ### heredamos algunos metodos y atributos de la clase Resource: es una copia con cambios
    parser = reqparse.RequestParser()
    parser.add_argument('bigpeople',
        type = str,
        required = True,
        action = "append", 
        help = "El campo no puede estar vacio")  

    @jwt_required()
    def get(self, name): ### Defino el verbo y que va a hacer l
        area = next(filter(lambda x: x["nombre"] == name, datalyticsCol), None) ### filter -> es un iterable
        return {"area" : area}, 200 if area else 404
    
    def post(self, name):
        if next(filter(lambda x: x["nombre"] == name, datalyticsCol), None) is not None:
            return {"mensage": f"El area {name} ya existe"}, 400 ### BAD REQUEST
        #request_data = request.get_json() ### force=True (no necesitamos el contenttype, no mira el header: parsea aunque sea incorrecto)
        #area = {"nombre": request_data["nombre"], "bigpeople": request_data["bigpeople"]}
        data = Area.parser.parse_args()
        area = {"nombre": name, "bigpeople": data["bigpeople"]}
        datalyticsCol.append(area)
        return area, 201 ### 201: create; 202: acepted 

    def delete(self, name):
        global datalyticsCol
        datalyticsCol = list(filter(lambda x: x['nombre'] != name, datalyticsCol))
        return {"mensage": f"Area {name} eliminada"}
    
    def put(self, name):
        #data = request.get_json()

        data = Area.parser.parse_args()
        area = next(filter(lambda x: x["nombre"] == name, datalyticsCol),None)
        if area is None:
            area = {"nombre": name, "bigpeople": data["bigpeople"]}
            datalyticsCol.append(area)
        else: 
            area.update(data)
        return area


class Datalytics(Resource):
    def get(self):
        return {"Datalytics Colombia": datalyticsCol}


api.add_resource(Area, '/area/<string:name>')
api.add_resource(Datalytics, '/datacol')

app.run(port=5000, debug=True)  ### El recurso se vuelve accesible a tráves del Api: No tenemos la necesidad de definir endpoints

### Pasos: 
#### 1. Definir el API
#### 2. Definir y crear los recursos.
#### 3. Definir los metodos para los recursos y que haran cuando son alcanzados sus endpoints
#### 4. Se agrega el recurso y parametros. 