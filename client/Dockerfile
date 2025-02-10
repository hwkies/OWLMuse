FROM node:20-alpine

RUN mkdir /project
WORKDIR /project

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000
    
CMD ["npm", "start"]
# CMD if [ "$ENV" = "production" ]; then \
#     ng serve --configuration=production --host 0.0.0.0; \
# else \
#     ng serve --host 0.0.0.0; \
# fi