FROM python:3.12-slim
WORKDIR \app
COPY . .
run pip install -r requirements.txt
ENTRYPOINT ["python", "hello=volume.py"]
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT ["python3", "./re.py"]