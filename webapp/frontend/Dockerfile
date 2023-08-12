FROM node:18.7.0-alpine3.16

WORKDIR /react-app
COPY ./package.json /react-app
RUN npm install
COPY . .
CMD npm start