FROM python:3.10
WORKDIR /app
COPY consumer.py requirements.txt wait-for-it.sh ./
RUN chmod +x wait-for-it.sh
RUN pip install -r requirements.txt
CMD ["./wait-for-it.sh", "rabbitmq:5672", "--", "python", "consumer.py"]
