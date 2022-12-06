FROM python:3.10.7-slim-buster
# set work directory
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip &&  pip install --no-cache-dir -r /app/requirements.txt
COPY . /app
#RUN python3 -m pip install --upgrade pip && pip3 install "fastapi[all]" && pip3 install pandas && pip3 install psycopg2-binary && pip3 install SQLAlchemy
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
