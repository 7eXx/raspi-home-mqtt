FROM python:3.9

WORKDIR /opt/raspi-home/

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY .env .

COPY main.py .
COPY wsgi.py .

COPY src src

ENV GPIOZERO_PIN_FACTORY=native
ENV FLASK_APP=main.py
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]



