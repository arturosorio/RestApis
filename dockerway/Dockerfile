FROM python:3.7-slim

# Upgrade pip
RUN pip install --upgrade pip

## make a local directory
RUN mkdir /app

# set "app" as the working directory from which CMD, RUN, ADD references
WORKDIR /app

# now copy all the files in this directory to /code
COPY ./app /app

# pip install the local requirements.txt
RUN pip install Flask
RUN pip install Flask-JWT
RUN pip install Flask-RESTful
RUN pip install gunicorn
RUN pip install numpy
RUN pip install scipy
RUN pip install scikit-learn



# Define our command to be run when launching the container
CMD gunicorn run:app --bind 0.0.0.0:$PORT --reload