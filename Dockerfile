
FROM python:3.13-slim


WORKDIR /app


COPY . .


EXPOSE 5000


CMD ["python", "app.py"]
