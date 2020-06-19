## Verbs + Stateless

from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

dataareas = [{
    'nombre': 'analitica',
    'Bigpeople': [{'nombre':'Monica', 'skills': ["TimeSeries", "R"]},
                  {'nombre': 'Andres', 'skills': ['NLP', 'Python']}]
}]

@app.route('/')
def home():
  return render_template('index.html')


@app.route('/areas' , methods=['POST'])
def create_area():
  request_data = request.get_json()
  new_area = {
    'nombre':request_data['nombre'],
    'Bigpeople':[]
  }
  dataareas.append(new_area)
  return jsonify(new_area)
  #pass


@app.route('/areas/<string:name>')
def get_area(name):
  for area in dataareas:
    if area['nombre'] == name:
          return jsonify(area)
  return jsonify({'message': 'No existe el area'})



@app.route('/areas')
def get_areas():
  return jsonify({'areas': dataareas})



@app.route('/areas/<string:name>/bigpeople' , methods=['POST'])
def create_user_in_area(name):
  request_data = request.get_json()
  for area in dataareas:
    if area['nombre'] == name:
        new_user = {
            'nombre': request_data['nombre'],
            'skills': request_data['skills']
        }
        area['Bigpeople'].append(new_user)
        return jsonify(new_user)
  return jsonify ({'message' :'area not found'})



@app.route('/areas/<string:name>/users')
def get_users_in_area(name):
  for area in dataareas:
    if area['nombre'] == name:
        return jsonify( {'items':area['Bigpeople'] } )
  return jsonify ({'message':'area not found'})



app.run(port=5000, debug=True)