from airflow.datasets import Dataset
from cosmos import DbtDag, ExecutionMode, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping
from datetime import datetime
import os
from pathlib import Path

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="postgres_default",
        profile_args={"schema": "public"},
    ),
)

dbt_dag = DbtDag(
    project_config=ProjectConfig(
        "/opt/airflow/dags/dbt",
    ),
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        execution_mode=ExecutionMode.VIRTUALENV,
        virtualenv_dir=Path("/opt/airflow/dbt_venv"),
        dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",
    ),
    # normal dag parameters
    schedule=[Dataset("postgres://postgres:5432/airflow.public.session_performance")],
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="dbt_dag",
    tags=["dss", "dbt"],
)