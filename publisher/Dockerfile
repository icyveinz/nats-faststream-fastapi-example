FROM python:3.10
WORKDIR /app
COPY main.py requirements.txt wait-for-it.sh ./
RUN chmod +x wait-for-it.sh
RUN pip install -r requirements.txt
CMD ["./wait-for-it.sh", "rabbitmq:5672", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
