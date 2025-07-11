FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install flask mysql-connector-python
CMD ["python", "server.py"]
EXPOSE 5000

