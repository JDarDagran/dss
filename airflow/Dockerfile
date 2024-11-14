FROM apache/airflow:2.10.3

RUN pip install apache-airflow-providers-postgres apache-airflow-providers-openlineage astronomer-cosmos

RUN uv venv dbt_venv && source dbt_venv/bin/activate && \
    uv pip install --no-cache-dir dbt-postgres && deactivate

USER airflow