# REST APIs with Flask - Tutorial and Examples

## 📖 Overview / Resumen

This repository contains comprehensive examples and tutorials for building REST APIs using Flask. It demonstrates different concepts from basic endpoints to advanced features like JWT authentication and machine learning model deployment.

**Este repositorio contiene ejemplos y tutoriales completos para construir APIs REST usando Flask. Demuestra diferentes conceptos desde endpoints básicos hasta características avanzadas como autenticación JWT y despliegue de modelos de machine learning.**

## 🏗️ Repository Structure / Estructura del Repositorio

### 1. [concepts/](concepts) - Basic Concepts / Conceptos Básicos
Educational examples showing fundamental Flask concepts:
- **`simple_start.py`** - Basic Flask "Hello World" application
- **`verbs.py`** - HTTP verbs demonstration with data management
- **`Simplerestful_1.py`** - Introduction to Flask-RESTful
- **`Simplerestful_2.py`** - Advanced REST concepts
- **`templates/index.html`** - Frontend example with AJAX calls

*Pequeñas aplicaciones que sirven para repasar conceptos fundamentales: recursos, endpoints, y métodos de comunicación.*

### 2. [secureapp/](secureapp) - Authentication Examples / Ejemplos con Autenticación
Advanced examples incorporating security:
- **`Simplerestful_3.py`** - Complete API with JWT authentication and ML models
- **`security.py`** - User authentication and authorization system

*Ejemplifica los métodos anteriores y muestra una implementación completa que incorpora un sistema de autenticación.*

### 3. [gitway/](gitway) - Git-based Deployment / Despliegue basado en Git
Production-ready application configured for Git-based Heroku deployment:
- Complete Flask application with ML capabilities
- Heroku configuration files (Procfile, requirements.txt, runtime.txt)

### 4. [dockerway/](dockerway) - Docker-based Deployment / Despliegue basado en Docker
Same application configured for Docker deployment:
- **`Dockerfile`** - Container configuration
- **`app/`** - Application code optimized for containerization

## 🛠️ Technology Stack / Tecnologías Utilizadas

- **Flask 1.1.2** - Web framework
- **Flask-RESTful 0.3.8** - REST API extension
- **Flask-JWT 0.3.2** - JSON Web Token authentication
- **scikit-learn 0.22.1** - Machine learning capabilities
- **NumPy, SciPy** - Scientific computing
- **Gunicorn 20.0.4** - WSGI HTTP Server for production

## 🚀 Quick Start / Inicio Rápido

### Prerequisites / Requisitos Previos
- Python 3.7+
- pip (Python package manager)
- [Heroku account](https://www.heroku.com/) (for deployment)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) (for deployment)

### Local Development Setup / Configuración para Desarrollo Local

#### Option 1: Using virtualenv (Windows/Linux/Mac)
```bash
# Install virtualenv
pip install virtualenv

# Create virtual environment
virtualenv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Option 2: Using Conda
```bash
# Create conda environment
conda create --name restapi python=3.7

# Activate environment
conda activate restapi

# Install dependencies
pip install -r requirements.txt
```

### Running Examples / Ejecutando los Ejemplos

#### Basic Concepts
```bash
# Navigate to concepts directory
cd concepts

# Run basic Flask app
python simple_start.py

# Run HTTP verbs example
python verbs.py

# Run Flask-RESTful examples
python Simplerestful_1.py
```

#### Secure Application with ML
```bash
# Navigate to secureapp directory
cd secureapp

# Run the secure application
python Simplerestful_3.py
```

## 🔐 Authentication / Autenticación

The secure applications use JWT (JSON Web Tokens) for authentication:

### Default User / Usuario por Defecto
- **Username:** `andres`
- **Password:** `1234`

### Getting JWT Token / Obtener Token JWT
```bash
# POST request to /auth endpoint
curl -X POST \
  http://localhost:5000/auth \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "andres",
    "password": "1234"
  }'
```

### Using JWT Token / Usar Token JWT
```bash
# Use the token in Authorization header
curl -X GET \
  http://localhost:5000/area/analytics \
  -H 'Authorization: JWT YOUR_TOKEN_HERE'
```

## 📚 API Documentation / Documentación de la API

### Concepts API Endpoints

#### Verbs.py Endpoints
- **GET** `/areas` - Get all areas
- **POST** `/areas` - Create new area
- **GET** `/areas/{name}` - Get specific area
- **POST** `/areas/{name}/bigpeople` - Add person to area
- **GET** `/areas/{name}/users` - Get users in area

#### Simplerestful_1.py Endpoints
- **GET** `/bigpeople/{name}` - Get person information

### Secure Application Endpoints

#### Authentication
- **POST** `/auth` - Authenticate user and get JWT token

#### Data Management (requires JWT)
- **GET** `/area/{name}` - Get area information
- **POST** `/area/{name}` - Create new area
- **PUT** `/area/{name}` - Update area
- **DELETE** `/area/{name}` - Delete area
- **GET** `/datacol` - Get all areas

#### Machine Learning Endpoints
- **POST** `/train/{version}` - Train ML model
- **GET** `/train/{version}` - Get model definition
- **GET** `/modelo` - List all models
- **GET** `/predtest/{version}` - Test predictions
- **POST** `/predtest/{version}` - Make predictions with custom data
- **GET** `/saludar` - Health check endpoint

### Example API Requests / Ejemplos de Peticiones

#### Train a Model / Entrenar un Modelo
```bash
curl -X POST \
  http://localhost:5000/train/v1 \
  -H 'Authorization: JWT YOUR_TOKEN_HERE' \
  -H 'Content-Type: application/json' \
  -d '{
    "split_size": 0.2,
    "pca_grid": [2, 3, 4],
    "alpha": [1, 10, 100]
  }'
```

#### Make Predictions / Hacer Predicciones
```bash
curl -X POST \
  http://localhost:5000/predtest/v1 \
  -H 'Content-Type: application/json' \
  -d '{
    "data": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
  }'
```

## 🚢 Deployment / Despliegue

### Option 1: Git-based Deployment / Despliegue basado en Git

```bash
# Navigate to gitway directory
cd gitway

# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Verify git remotes
git remote -v

# Deploy to Heroku
git push heroku master

# Scale dynos (free tier)
heroku ps:scale web=1 --app your-app-name
```

### Option 2: Docker-based Deployment / Despliegue basado en Docker

```bash
# Navigate to dockerway directory
cd dockerway

# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Push and release container
heroku container:push web --app your-app-name
heroku container:release web --app your-app-name

# Scale dynos (free tier)
heroku ps:scale web=1 --app your-app-name
```

## 🧪 Testing the APIs / Probando las APIs

### Using curl
```bash
# Test basic endpoint
curl http://localhost:5000/saludar

# Test with authentication
curl -X POST http://localhost:5000/auth \
  -H 'Content-Type: application/json' \
  -d '{"username": "andres", "password": "1234"}'
```

### Using Python requests
```python
import requests

# Get JWT token
response = requests.post('http://localhost:5000/auth', 
                        json={'username': 'andres', 'password': '1234'})
token = response.json()['access_token']

# Make authenticated request
headers = {'Authorization': f'JWT {token}'}
response = requests.get('http://localhost:5000/area/analytics', headers=headers)
print(response.json())
```

## 📖 Learning Path / Ruta de Aprendizaje

1. **Start with basics** - Run `concepts/simple_start.py`
2. **Learn HTTP verbs** - Explore `concepts/verbs.py`
3. **Understand REST** - Study `concepts/Simplerestful_1.py` and `Simplerestful_2.py`
4. **Add security** - Move to `secureapp/Simplerestful_3.py`
5. **Deploy applications** - Use `gitway/` or `dockerway/` for production

## 🤝 Contributing / Contribuir

Feel free to contribute to this educational repository by:
- Adding new examples
- Improving documentation
- Fixing bugs
- Adding tests

## 📚 Additional Documentation / Documentación Adicional

- **[API Reference Guide](docs/API_REFERENCE.md)** - Complete API endpoint documentation
- **[Deployment Guide](docs/DEPLOYMENT.md)** - Detailed deployment instructions for Heroku
- **[Complete Examples](docs/EXAMPLES.md)** - Comprehensive usage examples and code samples

## 🔗 Useful Links / Enlaces Útiles

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-RESTful Documentation](https://flask-restful.readthedocs.io/)
- [Flask-JWT Documentation](https://pythonhosted.org/Flask-JWT/)
- [Heroku Python Support](https://devcenter.heroku.com/categories/python-support)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)

## 📄 License / Licencia

This project is for educational purposes. Please check individual file headers for specific licensing information.

