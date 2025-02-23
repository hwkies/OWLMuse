Testing:
In /server
pytest --cov --cov-report term-missing

Compose:
docker-compose --profile <dev/prod> up --build
docker-compose --profile <dev/prod> down

FastAPI:
In /server
fastapi dev main.py

React/Next:
In /client
npm run dev
npm run start