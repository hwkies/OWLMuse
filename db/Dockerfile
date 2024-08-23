FROM mcr.microsoft.com/mssql/server

COPY init_template.sql init_template.sql
COPY init.sh init.sh

CMD ./init.sh & ./opt/mssql/bin/sqlservr