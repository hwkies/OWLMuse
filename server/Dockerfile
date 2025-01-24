# 
FROM python:3.11

# 
WORKDIR /server

# 
COPY ./requirements.txt /server/requirements.txt

# 
RUN apt-get update && \
apt-get install -y --no-install-recommends freetds-dev && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

#
RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

# 
COPY ./ /server

RUN python -c "import sqlite3; print('SQLite is ready to use!')"

# 
CMD ["fastapi", "run", "main.py", "--port", "8000"]