# Complete API Examples

This document provides comprehensive examples for using all the APIs in this repository.

## Setup

Before running these examples, ensure you have the application running locally:

```bash
# Navigate to the appropriate directory
cd secureapp  # or gitway/

# Run the application
python Simplerestful_3.py  # or app.py for gitway
```

The application will be available at `http://localhost:5000`

## Authentication Examples

### 1. Get JWT Token

#### Using curl
```bash
curl -X POST \
  http://localhost:5000/auth \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "andres",
    "password": "1234"
  }'
```

#### Using Python requests
```python
import requests

# Authenticate and get token
auth_response = requests.post(
    'http://localhost:5000/auth',
    json={
        'username': 'andres',
        'password': '1234'
    }
)

if auth_response.status_code == 200:
    token = auth_response.json()['access_token']
    print(f"Token obtained: {token}")
else:
    print("Authentication failed")
```

#### Expected Response
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NDMyMzQ1NjcsIm5iZiI6MTY0MzIzNDU2NywianRpIjoiYjIwZjY4ZDQtZGI4ZC00NzA5LWI0ZDMtNjQwMjQ1OGZjMzNjIiwiZXhwIjoxNjQzMjM0ODY3LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.xPqTgKNpzTjKK3xDgFIiLUi82JmAVFwU8ZhKpDlVJ5o"
}
```

## Data Management Examples

### 2. Create a New Area

#### Using curl
```bash
curl -X POST \
  http://localhost:5000/area/analytics \
  -H 'Content-Type: application/json' \
  -d '{
    "bigpeople": ["Monica", "Andres", "Carlos"]
  }'
```

#### Using Python
```python
import requests

# Create new area
response = requests.post(
    'http://localhost:5000/area/analytics',
    json={
        'bigpeople': ['Monica', 'Andres', 'Carlos']
    }
)

print(response.json())
```

### 3. Get Area Information (Authenticated)

#### Using curl
```bash
curl -X GET \
  http://localhost:5000/area/analytics \
  -H 'Authorization: JWT YOUR_TOKEN_HERE'
```

#### Using Python
```python
import requests

# Use the token from authentication
headers = {'Authorization': f'JWT {token}'}

response = requests.get(
    'http://localhost:5000/area/analytics',
    headers=headers
)

print(response.json())
```

### 4. Update an Area

#### Using curl
```bash
curl -X PUT \
  http://localhost:5000/area/analytics \
  -H 'Content-Type: application/json' \
  -d '{
    "bigpeople": ["Monica", "Andres", "Carlos", "Sofia"]
  }'
```

### 5. Get All Areas

#### Using curl
```bash
curl -X GET http://localhost:5000/datacol
```

#### Using Python
```python
response = requests.get('http://localhost:5000/datacol')
print(response.json())
```

### 6. Delete an Area

#### Using curl
```bash
curl -X DELETE http://localhost:5000/area/analytics
```

## Machine Learning Examples

### 7. Train a Model

#### Using curl
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

#### Using Python
```python
import requests

# Train a model (requires authentication)
headers = {'Authorization': f'JWT {token}'}

training_data = {
    'split_size': 0.2,
    'pca_grid': [2, 3, 4],
    'alpha': [1, 10, 100]
}

response = requests.post(
    'http://localhost:5000/train/v1',
    headers=headers,
    json=training_data
)

print("Training response:", response.json())
```

### 8. List All Models

#### Using curl
```bash
curl -X GET http://localhost:5000/modelo
```

#### Using Python
```python
response = requests.get('http://localhost:5000/modelo')
print("Available models:", response.json())
```

### 9. Get Model Definition

#### Using curl
```bash
curl -X GET http://localhost:5000/train/v1
```

### 10. Make Test Predictions

#### Using curl
```bash
curl -X GET http://localhost:5000/predtest/v1
```

#### Using Python
```python
response = requests.get('http://localhost:5000/predtest/v1')
print("Test predictions:", response.json())
```

### 11. Make Custom Predictions

#### Using curl (Single Sample)
```bash
curl -X POST \
  http://localhost:5000/predtest/v1 \
  -H 'Content-Type: application/json' \
  -d '{
    "data": [0.00632, 18.00, 2.310, 0, 0.5380, 6.5750, 65.20, 4.0900, 1, 296.0, 15.30, 396.90, 4.98]
  }'
```

#### Using curl (Multiple Samples)
```bash
curl -X POST \
  http://localhost:5000/predtest/v1 \
  -H 'Content-Type: application/json' \
  -d '{
    "data": [
      0.00632, 18.00, 2.310, 0, 0.5380, 6.5750, 65.20, 4.0900, 1, 296.0, 15.30, 396.90, 4.98,
      0.02731, 0.00, 7.070, 0, 0.4690, 6.4210, 78.90, 4.9671, 2, 242.0, 17.80, 396.90, 9.14
    ]
  }'
```

#### Using Python
```python
import requests

# Single prediction
single_sample = {
    'data': [0.00632, 18.00, 2.310, 0, 0.5380, 6.5750, 65.20, 4.0900, 1, 296.0, 15.30, 396.90, 4.98]
}

response = requests.post(
    'http://localhost:5000/predtest/v1',
    json=single_sample
)

print("Single prediction:", response.json())

# Multiple predictions
multiple_samples = {
    'data': [
        # First sample (13 features)
        0.00632, 18.00, 2.310, 0, 0.5380, 6.5750, 65.20, 4.0900, 1, 296.0, 15.30, 396.90, 4.98,
        # Second sample (13 features)
        0.02731, 0.00, 7.070, 0, 0.4690, 6.4210, 78.90, 4.9671, 2, 242.0, 17.80, 396.90, 9.14
    ]
}

response = requests.post(
    'http://localhost:5000/predtest/v1',
    json=multiple_samples
)

print("Multiple predictions:", response.json())
```

## Complete Workflow Example

Here's a complete Python script that demonstrates the entire workflow:

```python
import requests
import json

# Base URL
BASE_URL = 'http://localhost:5000'

def main():
    # Step 1: Authenticate
    print("1. Authenticating...")
    auth_response = requests.post(
        f'{BASE_URL}/auth',
        json={'username': 'andres', 'password': '1234'}
    )
    
    if auth_response.status_code != 200:
        print("Authentication failed!")
        return
    
    token = auth_response.json()['access_token']
    headers = {'Authorization': f'JWT {token}'}
    print(f"✓ Authentication successful")
    
    # Step 2: Create an area
    print("\n2. Creating an area...")
    area_data = {'bigpeople': ['Alice', 'Bob', 'Charlie']}
    create_response = requests.post(
        f'{BASE_URL}/area/datascience',
        json=area_data
    )
    print(f"✓ Area created: {create_response.json()}")
    
    # Step 3: Get area information (requires auth)
    print("\n3. Getting area information...")
    get_response = requests.get(
        f'{BASE_URL}/area/datascience',
        headers=headers
    )
    print(f"✓ Area info: {get_response.json()}")
    
    # Step 4: Train a model
    print("\n4. Training a model...")
    training_params = {
        'split_size': 0.3,
        'pca_grid': [2, 3],
        'alpha': [1, 10]
    }
    train_response = requests.post(
        f'{BASE_URL}/train/demo_model',
        headers=headers,
        json=training_params
    )
    print(f"✓ Model trained: {train_response.json()}")
    
    # Step 5: List models
    print("\n5. Listing available models...")
    models_response = requests.get(f'{BASE_URL}/modelo')
    print(f"✓ Available models: {models_response.json()}")
    
    # Step 6: Make predictions
    print("\n6. Making predictions...")
    prediction_data = {
        'data': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
    }
    pred_response = requests.post(
        f'{BASE_URL}/predtest/demo_model',
        json=prediction_data
    )
    print(f"✓ Predictions: {pred_response.json()}")
    
    # Step 7: Health check
    print("\n7. Health check...")
    health_response = requests.get(f'{BASE_URL}/saludar')
    print(f"✓ Health: {health_response.json()}")

if __name__ == "__main__":
    main()
```

## Error Handling Examples

### Handling Authentication Errors
```python
import requests

def authenticate_with_error_handling():
    try:
        response = requests.post(
            'http://localhost:5000/auth',
            json={'username': 'wrong', 'password': 'credentials'}
        )
        
        if response.status_code == 401:
            print("Invalid credentials")
            return None
        elif response.status_code == 200:
            return response.json()['access_token']
        else:
            print(f"Unexpected error: {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
```

### Handling Model Training Errors
```python
def train_model_with_error_handling():
    # ... authentication code ...
    
    training_params = {
        'split_size': 0.2,
        'pca_grid': [2, 3, 4],
        'alpha': [1, 10, 100]
    }
    
    try:
        response = requests.post(
            'http://localhost:5000/train/v1',
            headers={'Authorization': f'JWT {token}'},
            json=training_params,
            timeout=300  # 5 minutes timeout for training
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"Model trained successfully!")
            print(f"Score: {result['score']}")
            return result
        elif response.status_code == 401:
            print("Authentication required or token expired")
            return None
        else:
            print(f"Training failed: {response.status_code}")
            print(response.text)
            return None
            
    except requests.exceptions.Timeout:
        print("Training timed out - this might be normal for large datasets")
        return None
```

## Frontend Integration Example

### JavaScript/AJAX Example
```html
<!DOCTYPE html>
<html>
<head>
    <title>API Example</title>
</head>
<body>
    <div id="result"></div>
    
    <script>
        // Authentication
        async function authenticate() {
            try {
                const response = await fetch('http://localhost:5000/auth', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        username: 'andres',
                        password: '1234'
                    })
                });
                
                const data = await response.json();
                return data.access_token;
            } catch (error) {
                console.error('Authentication failed:', error);
                return null;
            }
        }
        
        // Get areas
        async function getAreas() {
            try {
                const response = await fetch('http://localhost:5000/datacol');
                const data = await response.json();
                document.getElementById('result').innerHTML = 
                    '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
            } catch (error) {
                console.error('Failed to get areas:', error);
            }
        }
        
        // Run on page load
        getAreas();
    </script>
</body>
</html>
```

This completes the comprehensive examples for using all the APIs in the repository. Each example includes both curl and Python implementations, along with proper error handling and complete workflow demonstrations.