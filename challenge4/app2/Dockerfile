FROM python:3.11-slim

WORKDIR /app2

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app2.py .

EXPOSE 5002

CMD ["python", "app2.py"]

