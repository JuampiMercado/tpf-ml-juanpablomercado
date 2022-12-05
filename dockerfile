FROM apache/airflow:2.4.0-python3.10
COPY requirements.txt /
RUN pip install --upgrade pip && pip install --no-cache-dir -r /requirements.txt