FROM python:3.9-slim-buster
RUN apt-get update && apt-get install -y mosquitto mosquitto-clients
COPY . .
EXPOSE 1883
CMD ["sh", "-c", "mosquitto"]
