FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

WORKDIR /app

COPY ./app /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]