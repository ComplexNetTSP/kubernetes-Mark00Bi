FROM python:3.11-slim

WORKDIR /app1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app1.py .

EXPOSE 5001

CMD ["python", "app1.py"]

