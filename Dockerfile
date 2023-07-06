FROM python:3.10-alpine3.18
RUN addgroup app && adduser -S -G app app
USER app
WORKDIR /app
COPY . .
# run npm install
ENV API_URL=http://api.myapp.com/
EXPOSE 8000
# cmd ["npm", "start"]
# entrypoint ["npm", "start"]
