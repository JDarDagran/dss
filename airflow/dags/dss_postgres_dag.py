import datetime

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.datasets import Dataset

DAG_ID = "dss_postgres_dag"

with DAG(
    dag_id=DAG_ID,
    start_date=datetime.datetime(2020, 2, 2),
    schedule="@once",
    catchup=False,
    tags=["dss", "postgres_operator"],
) as dag:
    create_pet_table = SQLExecuteQueryOperator(
        conn_id="postgres_default",
        task_id="create_top_speakers",
        sql=
        """
        CREATE TABLE IF NOT EXISTS session_performance AS
        SELECT
            a.session_id,
            a.attendees_count,
            s.name AS speaker_name,
            s.speaker_id
        FROM
            attendees_by_session a
        JOIN
            top_speakers s ON a.session_id = s.session_id
        ORDER BY
            attendees_count DESC;
                """,
        outlets=[Dataset("postgres://postgres:5432/airflow.public.session_performance")],
    )