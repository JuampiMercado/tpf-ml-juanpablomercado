FROM python:3.7.9-slim-buster
# set work directory
WORKDIR /app
RUN python3 -m pip install --upgrade pip && pip3 install "fastapi[all]" && pip3 install pandas && pip3 install psycopg2-binary && pip3 install SQLAlchemy
COPY . /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
