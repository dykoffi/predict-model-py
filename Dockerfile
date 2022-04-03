FROM python:3.8-slim


# Install and update 
RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip install pipenv

WORKDIR /app
COPY Pipfile .

#Install python dependencies
RUN pipenv --python /usr/local/bin/python install

COPY . .

EXPOSE $PORT

CMD uvicorn main:app --host 0.0.0.0 --port $PORT