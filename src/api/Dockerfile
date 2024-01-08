FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY . /app

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
