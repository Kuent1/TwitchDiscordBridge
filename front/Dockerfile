# Use a base image
FROM httpd:latest

# Copy the files to the web server directory
COPY . /usr/local/apache2/htdocs/

# Expose the default HTTP port
EXPOSE 80

# Start the web server
CMD ["httpd", "-D", "FOREGROUND"]
