FROM python:3

WORKDIR /opt/raspi-home/

RUN python -m  venv venv

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY .env .

COPY main.py .

COPY src src

CMD python3 main.py



