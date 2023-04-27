FROM python:3.9-slim-buster
RUN apt-get update && apt-get install -y mosquitto mosquitto-clients
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 1883
CMD ["sh", "-c", "mosquitto & python3 Fog.py"]
