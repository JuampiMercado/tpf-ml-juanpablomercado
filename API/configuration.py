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
        "aws_access_key_id":"ASIAUKIPBF3MUB2INKG3",
        "aws_secret_access_key":"Xo56JoZMQE9JdpwqGvSJWqrroGaUy7+Eo96QH+UA",
        "aws_session_token":"FwoGZXIvYXdzEOr//////////wEaDN3CNhQVP6jO3CzleiLOAR6PbGexnT146wjx7c0tCRFC14p9s7Syr+cAbmv3QpcSb/e7MZxwyxF5ZERuP3a2KnKBhRnC3+Rsgglx1xdodp2cZccbX+T6Lu2wxBs8rzSIOQIMdrOS1bt5UcJoL2hafCBkcw7KLp+SSGNf+g9iyRWnhgqOfbfsT5EW/muzB7pDOi4H7ahYHVhha9svId81T8FUl6cda/H9nkJqWD+XOUYlT6FnYM9aX/5u9BHo0+1f0nXIpQxmi4166a9MPX8b5AVNC4Z0MgRqPoMZ+5HQKJbAuJwGMi1IkqkXHO3EZcj+ZDUSIs0aXkP76bQ5pEi53Z3dbi2GiTgyna3FPCrU6L3UnM8="
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