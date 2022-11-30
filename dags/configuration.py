env_dev = True

prod_config = {
    "db_params": {
        "postgresql":{
            "host":"postgres",
            "port":"5432",
            "database":"ETL",
            "user":"airflow",
            "password":"airflow"
        },
        "sqlite":{
            "database":"sqlite_default.db"
        }
    },
    "output_path": "/opt/airflow/dags/output"
}

dev_config = {
    "db_params": {
        "postgresql":{
            "host":"localhost",
            "port":"5432",
            "database":"ETL",
            "user":"airflow",
            "password":"airflow"
        },
        "sqlite":{
            "database":"sqlite_default.db"
        }
    },
    "output_path": "dags/output"
}


def get_config(key):
    if env_dev:
        return dev_config[key]
    else:
        return prod_config[key]