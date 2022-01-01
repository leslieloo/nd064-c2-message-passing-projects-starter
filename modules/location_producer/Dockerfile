FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache g++ gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5005

COPY . .
CMD ["python", "server.py"]