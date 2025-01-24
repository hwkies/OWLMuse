# 
FROM python:3.11

# 
WORKDIR /server

# 
COPY ./requirements.txt /server/requirements.txt

# 
RUN apt-get update && apt-get install freetds-dev -y

#
RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

# 
COPY ./api /server/api

# 
CMD ["fastapi", "run", "api/main.py", "--port", "8000"]