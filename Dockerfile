FROM python:3.10-slim


# Install and update 
RUN pip install pipenv

WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy --ignore-pipfile
# RUN pipenv shell

COPY . .

EXPOSE 80

CMD gunicorn --bind :80 --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app