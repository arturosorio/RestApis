# API Reference Guide

## Authentication

All secure endpoints require JWT authentication. First, obtain a token by authenticating with valid credentials.

### POST /auth
Authenticate user and receive JWT token.

**Request Body:**
```json
{
  "username": "andres",
  "password": "1234"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

## Data Management API

### Areas Management

#### GET /area/{name}
Get information about a specific area.

**Headers:** 
- `Authorization: JWT {token}`

**Response:**
```json
{
  "area": {
    "nombre": "analytics",
    "bigpeople": ["Monica", "Andres"]
  }
}
```

#### POST /area/{name}
Create a new area.

**Headers:** 
- `Content-Type: application/json`

**Request Body:**
```json
{
  "bigpeople": ["John", "Jane"]
}
```

**Response:**
```json
{
  "nombre": "analytics",
  "bigpeople": ["John", "Jane"]
}
```

#### PUT /area/{name}
Update an existing area or create if it doesn't exist.

**Request Body:**
```json
{
  "bigpeople": ["Updated", "List"]
}
```

#### DELETE /area/{name}
Delete an area.

**Response:**
```json
{
  "mensage": "Area analytics eliminada"
}
```

#### GET /datacol
Get all areas.

**Response:**
```json
{
  "Datalytics Colombia": [
    {
      "nombre": "analytics",
      "bigpeople": ["Monica", "Andres"]
    }
  ]
}
```

## Machine Learning API

### Model Training

#### POST /train/{version}
Train a new machine learning model with specified parameters.

**Headers:** 
- `Authorization: JWT {token}`
- `Content-Type: application/json`

**Request Body:**
```json
{
  "split_size": 0.2,
  "pca_grid": [2, 3, 4],
  "alpha": [1, 10, 100]
}
```

**Response:**
```json
{
  "mensaje": "Modelo v1 con parametros [2, 3, 4] para PCA y [1, 10, 100] para el Ridge",
  "gridsearch": {
    "pca__n_components": [2, 3, 4],
    "ridge__alpha": [1, 10, 100]
  },
  "score": 0.8234,
  "FinalModel": "Pipeline(steps=[('standardscaler', StandardScaler()), ('pca', PCA(n_components=3)), ('ridge', Ridge(alpha=10))])"
}
```

#### GET /train/{version}
Get model definition and parameters.

**Response:**
```json
{
  "Model Definition": "{'memory': None, 'steps': [('standardscaler', StandardScaler()), ('pca', PCA()), ('ridge', Ridge())], 'verbose': False}"
}
```

### Model Management

#### GET /modelo
List all available trained models.

**Response:**
```json
{
  "modelos": ["modelo dummy", "v1", "v2"]
}
```

### Predictions

#### GET /predtest/{version}
Get test predictions using the first 10 samples from the training dataset.

**Response:**
```json
{
  "pred": [24.12, 21.45, 32.67, 18.90, 25.34, 29.12, 22.78, 27.45, 31.23, 19.87]
}
```

#### POST /predtest/{version}
Make predictions with custom input data.

**Request Body:**
```json
{
  "data": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
}
```

**Note:** Data should contain 13 features per sample. For multiple samples, provide multiples of 13 values.

**Response:**
```json
{
  "pred": [25.67]
}
```

### Health Check

#### GET /saludar
Simple health check endpoint.

**Response:**
```json
{
  "mensaje": "Hola Equipo"
}
```

## Error Responses

### 400 Bad Request
```json
{
  "mensage": "El area analytics ya existe"
}
```

### 401 Unauthorized
```json
{
  "description": "Request does not contain an access token",
  "error": "Authorization Required",
  "status_code": 401
}
```

### 404 Not Found
```json
{
  "area": null
}
```

## Rate Limiting

Currently, there are no rate limits implemented in the example applications. In production, consider implementing rate limiting for security and performance.

## Data Models

### Area
```json
{
  "nombre": "string",
  "bigpeople": ["string"]
}
```

### User
```json
{
  "id": "integer",
  "username": "string",
  "password": "string (hashed in production)"
}
```

### ML Model Training Parameters
```json
{
  "split_size": "float (0.0-1.0)",
  "pca_grid": ["integer array"],
  "alpha": ["integer array"]
}
```