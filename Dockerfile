FROM python:3.11-slim


WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get install -y --fix-missing \ 
    build-essential \
    && rm -rf /var/lib/apt/lists/*  



RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


