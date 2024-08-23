#!/bin/bash

# Wait for SQL Server to start
echo "Waiting for SQL Server to start..."
until /opt/mssql-tools18/bin/sqlcmd -S 127.0.0.1,1433 -U "${MSSQL_ADMIN}" -P "${MSSQL_SA_PASSWORD}" -Q "SELECT 1" -C &> /dev/null
do
    sleep 1
done

DB_CHECK=$(/opt/mssql-tools18/bin/sqlcmd -S 127.0.0.1,1433 -U "${MSSQL_ADMIN}" -P "${MSSQL_SA_PASSWORD}" -Q "SELECT COUNT(*) FROM sys.databases WHERE name='${MSSQL_DB}'" -C -h -1 -W | grep -o '^[0-9]\+$')

if [ "$DB_CHECK" -eq 1 ]; then
    DB_READY=0
    while [ $DB_READY -ne 1 ]
    do
        echo "Checking database recovery status..."
        RECOVERY_STATUS=$(/opt/mssql-tools18/bin/sqlcmd -S 127.0.0.1,1433 -U "${MSSQL_ADMIN}" -P "${MSSQL_SA_PASSWORD}" -Q "SELECT state_desc FROM sys.databases WHERE name='${MSSQL_DB}'" -C -h -1 | grep -oP '^\w+' | head -1)
      
        if [[ "$RECOVERY_STATUS" == "ONLINE" ]]; then
            DB_READY=1
            echo "Database recovery is complete."
        else
            echo "Waiting for database recovery to complete..."
            sleep 1
        fi
    done
fi

echo "Preprocessing database init file..."

sql_template=$(<./init_template.sql)

# Perform variable substitution
sql_query=$(echo "$sql_template" | sed -e "s/\$(MSSQL_DB)/${MSSQL_DB}/g" \
                                       -e "s/\$(MSSQL_USER)/${MSSQL_USER}/g" \
                                       -e "s/\$(MSSQL_PASSWORD)/${MSSQL_PASSWORD}/g")

echo "Finished preprocessing."

echo "Executing init.sql..."

./opt/mssql-tools18/bin/sqlcmd -S localhost,1433 -U "${MSSQL_ADMIN}" -P "${MSSQL_SA_PASSWORD}" -Q "$sql_query" -C

echo "Finished executing init.sql."