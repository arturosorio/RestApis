from flask import Flask, request  
from typing import List
from flask_restful import Resource, Api, reqparse   ## Un recurso es algo que nuestra API puede crear, modificar, devolver, etc. 
from flask_jwt import JWT, jwt_required
from sklearn.datasets import load_boston
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os
from sklearn.model_selection import GridSearchCV ,train_test_split
import numpy as np
import joblib 

from security import authenticate, identity

### FLASK JWT : json web token: obsfuscation of data, encoding. 
### User: entidad con id unico nos envia (nombre,  contraseña) y les devolvemos un jwt. Con el jwt pueden enviarnos cualquier solicitud 
### puesto que sabemos que se han identificado previamente. 

app = Flask(__name__) 
app.secret_key = "data" ### En producción no se hace esto. 
api = Api(app) ### Nos permite agregar y controlar los recursos con facilidad. 

### Api funciona como sobre recursos y cada recurso debe ser una clase. 

jwt = JWT(app, authenticate, identity) # /auth (user, password) -> autentificacion: devuelve un jwt token

Modelos = {
    "modelo dummy" : None
}

class Entrenar(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("split_size",
        type = float, 
        required = True)
    parser.add_argument("pca_grid", 
        type = int, 
        required = True,
        action = "append")
    parser.add_argument("alpha",
        type = int, 
        required = True, 
        action = "append")
    data = load_boston()
    cols = data["feature_names"]
    X = data["data"]
    y = data['target']
    pipeline = make_pipeline(StandardScaler(), PCA(), Ridge())
    
    @jwt_required()
    def post(self, version):
        args = Entrenar.parser.parse_args()
        # Parameters of pipelines can be set using ‘__’ separated parameter names:
        param_grid = {
        'pca__n_components': args["pca_grid"],
        'ridge__alpha': args["alpha"],
        }
        X_train, X_test, y_train, y_test = train_test_split(Entrenar.X, Entrenar.y, test_size = args["split_size"])
        search = GridSearchCV(Entrenar.pipeline, param_grid, n_jobs=-1)
        model = search.fit(X_train, y_train)
        Modelos[version] = model
        score = model.score(X_test,y_test)
        if not os.path.exists("app/models"):
            os.makedirs("app/models")

        joblib.dump(model, f"app/models/modelo_{version}.pkl")
        
        return {"mensaje": f'Modelo {version} con parametros {args["pca_grid"]} para PCA y {args["alpha"]} para el Ridge',
                "gridsearch" : param_grid,
                "score": score, 
                "FinalModel" : str(model.best_estimator_)}, 200 

    def get(self, version):
        return {"Model Definition" : str(Entrenar.pipeline.get_params())}

class ListaModelos(Resource):
    def get(self):
        return {"modelos": [*Modelos]}

class Predict(Resource):
    def get(self, version):
        model = Modelos[version]
        pred = model.predict(Entrenar.X[0:10,:].reshape(10,-1))
        return {"pred": list(pred)}, 200 

    def post(self, version):
        parser = reqparse.RequestParser()
        parser.add_argument("data",
            type = float, 
            required = True,
            action = "append")
        args = parser.parse_args()
        model = Modelos[version]
        nrow = len(args['data'])//13
        pred = model.predict(np.array(args['data']).reshape(nrow, -1))
        return {"pred": list(pred)}, 200

class Saludo(Resource):
    def get(self):
        return {"mensaje" : "Hola Equipo"}
    

api.add_resource(Entrenar, '/train/<string:version>')
api.add_resource(ListaModelos, '/modelo')
api.add_resource(Predict, "/predtest/<string:version>")
api.add_resource(Saludo, "/saludar")
#api.add_resource(Test, '/mierda/<string:que>')
#api.add_resource(Datalytics, '/datacol')

#app.run(port=5000)