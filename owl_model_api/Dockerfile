# 
FROM python:3.9

# 
WORKDIR /owl_model_api

# 
COPY ./requirements.txt /owl_model_api/requirements.txt

# 
RUN apt-get update && apt-get install freetds-dev -y

#
RUN pip install --no-cache-dir --upgrade -r /owl_model_api/requirements.txt

# 
COPY ./api /owl_model_api/api

# 
CMD ["fastapi", "run", "api/main.py", "--port", "8000"]