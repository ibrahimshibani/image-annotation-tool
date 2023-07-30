FROM mongo:latest

COPY configs/mongod.conf /etc/mongod.conf

EXPOSE 27017

CMD ["mongod", "--config", "/etc/mongod.conf"]
