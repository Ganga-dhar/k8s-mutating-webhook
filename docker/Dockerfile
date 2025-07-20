FROM python:3.9-slim
COPY webhook.py /app/webhook.py
COPY cert.pem /app/cert.pem
COPY key.pem /app/key.pem
WORKDIR /app
RUN pip install flask
CMD ["python", "webhook.py"]
