FROM python:3.11-slim-buster

WORKDIR /src

RUN apt-get -y update
RUN apt-get -y install git build-essential cargo


COPY requirements.txt .
COPY requirements_dev.txt .

RUN pip install --no-cache-dir -r requirements_dev.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]