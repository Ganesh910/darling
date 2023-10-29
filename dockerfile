FROM python:3
WORKDIR /app
COPY . /app/
COPY requirements.txt /app/
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD [ "python", "/app/Darling/server.py" ]