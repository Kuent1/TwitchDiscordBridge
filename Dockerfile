# Use a base image with Java installed
FROM openjdk:18-jdk-alpine3.13

# Set the working directory inside the container
WORKDIR /app

# Copy the application JAR file to the container
COPY TwitchDiscordBridge-*.jar .

# Set the command to run the application
CMD ["java", "-jar", "TwitchDiscordBridge-*.jar"]