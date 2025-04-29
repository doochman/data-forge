FROM apache/airflow:2.8.1

# Use the airflow user to install Python packages
COPY requirements.txt /requirements.txt
USER airflow
RUN pip install --no-cache-dir -r /requirements.txt

# Copy DAGs after switching to airflow user
COPY dags/ /opt/airflow/dags/
