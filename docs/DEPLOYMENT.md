# Deployment Guide

This guide covers both Git-based and Docker-based deployment strategies for the Flask REST API applications to Heroku.

## Prerequisites

1. **Heroku Account**: Sign up at [heroku.com](https://www.heroku.com/)
2. **Heroku CLI**: Install from [Heroku CLI Documentation](https://devcenter.heroku.com/articles/heroku-cli)
3. **Git**: Required for both deployment methods
4. **Docker**: Required only for Docker-based deployment

## Method 1: Git-based Deployment

### Step 1: Prepare the Application

Navigate to the gitway directory:
```bash
cd gitway
```

### Step 2: Initialize Git Repository (if not already done)
```bash
git init
git add .
git commit -m "Initial commit"
```

### Step 3: Login to Heroku
```bash
heroku login
```

### Step 4: Create Heroku Application
```bash
heroku create your-unique-app-name
```

**Note**: Replace `your-unique-app-name` with a unique name. Heroku will suggest one if you don't specify.

### Step 5: Verify Git Remotes
```bash
git remote -v
```

You should see both `origin` and `heroku` remotes.

### Step 6: Deploy to Heroku
```bash
git push heroku master
```

### Step 7: Scale the Application
```bash
heroku ps:scale web=1 --app your-app-name
```

### Step 8: Open the Application
```bash
heroku open --app your-app-name
```

## Method 2: Docker-based Deployment

### Step 1: Prepare the Application

Navigate to the dockerway directory:
```bash
cd dockerway
```

### Step 2: Login to Heroku
```bash
heroku login
```

### Step 3: Create Heroku Application
```bash
heroku create your-unique-app-name
```

### Step 4: Build and Push Container
```bash
heroku container:push web --app your-app-name
```

### Step 5: Release the Container
```bash
heroku container:release web --app your-app-name
```

### Step 6: Scale the Application
```bash
heroku ps:scale web=1 --app your-app-name
```

### Step 7: Open the Application
```bash
heroku open --app your-app-name
```

## Configuration Files

### Git Deployment Files

#### Procfile
Tells Heroku how to run your application:
```
web: gunicorn run:app --bind 0.0.0.0:$PORT --reload
```

#### runtime.txt
Specifies Python version:
```
python-3.7.9
```

#### requirements.txt
Lists all Python dependencies:
```
aniso8601==8.0.0
Flask==1.1.2
Flask-JWT==0.3.2
Flask-RESTful==0.3.8
gunicorn==20.0.4
# ... other dependencies
```

### Docker Deployment Files

#### Dockerfile
```dockerfile
FROM python:3.7-slim

# Upgrade pip
RUN pip install --upgrade pip

# Make a local directory
RUN mkdir /app

# Set "app" as the working directory
WORKDIR /app

# Copy files
COPY ./app /app

# Install dependencies
RUN pip install Flask Flask-JWT Flask-RESTful gunicorn numpy scipy scikit-learn

# Define command to run when launching the container
CMD gunicorn run:app --bind 0.0.0.0:$PORT --reload
```

## Environment Variables

### Setting Environment Variables
```bash
# Set secret key for production
heroku config:set SECRET_KEY=your-secret-key --app your-app-name

# Set other configuration variables
heroku config:set DEBUG=False --app your-app-name
```

### Viewing Environment Variables
```bash
heroku config --app your-app-name
```

## Troubleshooting

### Common Issues

#### Build Failures
1. **Python Version Mismatch**: Ensure `runtime.txt` specifies a supported Python version
2. **Dependency Issues**: Update `requirements.txt` with compatible versions
3. **Memory Issues**: Optimize dependencies or upgrade to a paid Heroku plan

#### Runtime Errors
1. **Port Binding**: Ensure your app binds to `0.0.0.0:$PORT`
2. **Environment Variables**: Check that all required environment variables are set
3. **File Paths**: Use relative paths in your application

### Debugging Commands

#### View Logs
```bash
heroku logs --tail --app your-app-name
```

#### Check Application Status
```bash
heroku ps --app your-app-name
```

#### Restart Application
```bash
heroku restart --app your-app-name
```

#### Run Commands in Heroku Environment
```bash
heroku run python --app your-app-name
```

## Monitoring and Maintenance

### Application Metrics
```bash
heroku ps --app your-app-name
heroku logs --num 100 --app your-app-name
```

### Database Management (if using databases)
```bash
# For PostgreSQL addon
heroku pg:info --app your-app-name
heroku pg:psql --app your-app-name
```

### Scaling
```bash
# Scale web dynos
heroku ps:scale web=2 --app your-app-name

# Scale worker dynos (if applicable)
heroku ps:scale worker=1 --app your-app-name
```

## Cost Optimization

### Free Tier Limitations
- 550-1000 free dyno hours per month
- Apps sleep after 30 minutes of inactivity
- 512 MB RAM limit

### Optimization Tips
1. Use efficient code and minimal dependencies
2. Implement proper caching strategies
3. Monitor resource usage with Heroku metrics
4. Consider upgrading to paid plans for production applications

## Security Considerations

### Production Security
1. **Secret Keys**: Never hardcode secrets in your application
2. **Environment Variables**: Use Heroku config vars for sensitive data
3. **HTTPS**: Heroku provides SSL termination automatically
4. **Dependencies**: Regularly update dependencies for security patches

### Example Security Configuration
```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
```

## Continuous Deployment

### GitHub Integration
1. Connect your GitHub repository to Heroku
2. Enable automatic deployments
3. Set up review apps for pull requests

### CI/CD Pipeline Example
```yaml
# .github/workflows/deploy.yml
name: Deploy to Heroku
on:
  push:
    branches: [ main ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: akhileshns/heroku-deploy@v3.12.12
      with:
        heroku_api_key: ${{secrets.HEROKU_API_KEY}}
        heroku_app_name: "your-app-name"
        heroku_email: "your-email@example.com"
```

## Next Steps

After successful deployment:
1. Test all API endpoints
2. Set up monitoring and alerting
3. Configure custom domain (if needed)
4. Implement proper logging
5. Set up backup strategies (for data persistence)