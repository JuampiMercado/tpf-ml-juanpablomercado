env_dev = False

prod_config = {
    "db_params": {
        # "postgresql":{
        #     "host":"postgres",
        #     "port":"5432",
        #     "database":"ETL",
        #     "user":"airflow",
        #     "password":"airflow"
        # }
        "postgresql":{
            "host":"etl.cbtzrylgm8xu.us-east-1.rds.amazonaws.com",
            "port":"5432",
            "database":"etl",
            "user":"etlpostgres",
            "password":"etlpostgres"
        }
    },
    "aws": {
        "aws_access_key_id":"ASIAUKIPBF3MQURJ7FMA",
        "aws_secret_access_key":"o4Mo21ET4QV56yKfHVc+2Xp1Zh/dWqrAlwV7YTY",
        "aws_session_token":"FwoGZXIvYXdzEP3//////////wEaDJxpmkGaH9QchfumgSLOATF8MkEaGmxcC6J9MCdEKWH/UU6NI7CAjv4X75CkZHnw49YFoNBz9RdHNdcMgPiUc9OPZ5jl5LykdlTye4HN0i7pQ9+8x+CxqtH8XRk55l09NNqjWgpELttDInnY8v8fxMo9cVPslEfFC/UBvkqPMH/BRSe/oATee1qPyueTiZFLNPtwn5yazLuBwsV2PRy5d+MhDiB15S9+xYxipwSaYnkECs+f7An8GKEtLB6ltK87aq8yGk1N0glyGvcgHsLD87wrd2ZOSHWX93jqr5ZjKPnTvJwGMi1ce+xSSZdw1uwxQI4RZYa7Jxy5kX38EPNNJzefK/MA7+Jpsulkurmd0w6QJb4="
    }
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
    "aws": {
        "aws_access_key_id":"ASIAUKIPBF3MR3YXMZLA",
        "aws_secret_access_key":"rkjCbGRGutAZn3Bv46ZriM6WnXQ5VXT0dyY5NHqb",
        "aws_session_token":"FwoGZXIvYXdzEIj//////////wEaDA4MdU8kzBC/1PimtSLOAbBxAAR/5G/XKYcgPsjjd0OIFRnMLJkMpgsSFVMRgw/iMhmHJVR6+PlpKNRzexDVJdVxAL235dSq9dicDDj0ZmvVPzzeFSAjYmftWBIRO3yZliTxIq8qZ13wsaAy5a8seFs0KK3WvIL5GuCLt6VIerNHnAOcVuVIHVQEAeWhWg/5WF1/UKnOyMlFOxENwwEBH9UZUAwuf3G3++Cn77kFhEqN3rvjBEcCpp9ekWXEe/1npxiR848XAghG4yPMIVLlosfHR0VjRVI/HdOcFr+VKNL3opwGMi1lZADpiUBNHLMUzEu/nI+DYeyPLM+6oLyrEp64QHrPovd0H3Zm0jLUf+EkgPA="
    }
}


def get_config(key):
    if env_dev:
        return dev_config[key]
    else:
        return prod_config[key]