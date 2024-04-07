# Use an official MySQL image as the base image
FROM mysql:5.7

# Environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=myDb
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=admin

# Copy the SQL script into the container to initialize the database
COPY ./mysql/product.sql /docker-entrypoint-initdb.d/product.sql
