env_dev = False

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
    "aws": {
        "aws_access_key_id":"ASIAUKIPBF3MR3YXMZLA",
        "aws_secret_access_key":"rkjCbGRGutAZn3Bv46ZriM6WnXQ5VXT0dyY5NHqb",
        "aws_session_token":"FwoGZXIvYXdzEIj//////////wEaDA4MdU8kzBC/1PimtSLOAbBxAAR/5G/XKYcgPsjjd0OIFRnMLJkMpgsSFVMRgw/iMhmHJVR6+PlpKNRzexDVJdVxAL235dSq9dicDDj0ZmvVPzzeFSAjYmftWBIRO3yZliTxIq8qZ13wsaAy5a8seFs0KK3WvIL5GuCLt6VIerNHnAOcVuVIHVQEAeWhWg/5WF1/UKnOyMlFOxENwwEBH9UZUAwuf3G3++Cn77kFhEqN3rvjBEcCpp9ekWXEe/1npxiR848XAghG4yPMIVLlosfHR0VjRVI/HdOcFr+VKNL3opwGMi1lZADpiUBNHLMUzEu/nI+DYeyPLM+6oLyrEp64QHrPovd0H3Zm0jLUf+EkgPA="
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