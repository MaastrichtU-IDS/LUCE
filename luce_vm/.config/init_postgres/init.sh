#!/bin/bash
set -e

# Example to init the posgresql DB:
# psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
#     CREATE USER docker;
#     CREATE DATABASE docker;
#     GRANT ALL PRIVILEGES ON DATABASE docker TO docker;
# EOSQL