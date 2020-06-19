from flask import Flask, request
from flask_restful import Resource, Api, reqparse   ## Un recurso es algo que nuestra API puede crear, modificar, devolver, etc. 

app = Flask(__name__) 
api = Api(app) ### Nos permite agregar y controlar los recursos con facilidad. 

### Api funciona  sobre recursos y cada recurso debe ser una clase. 

datalyticsCol = []


class Area(Resource): ### heredamos algunos metodos y atributos de la clase Resource: es una copia con cambios
    def get(self, name): ### Defino el verbo y que va a hacer 
        area = next(filter(lambda x: x["nombre"] == name, datalyticsCol), None) ### filter -> es un iterable
        return {"area" : area}, 200 if area else 404
    
    def post(self, name):
        if next(filter(lambda x: x["nombre"] == name, datalyticsCol), None) is not None:
            return {"mensage": f"El area {name} ya existe"}, 400 ### BAD REQUEST
        request_data = request.get_json() ### force=True (no necesitamos el contenttype, no mira el header: parsea aunque sea incorrecto)
        area = {"nombre": name, "bigpeople": request_data["bigpeople"]}
        datalyticsCol.append(area)
        return area, 201 ### 201: create; 202: acepted 

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