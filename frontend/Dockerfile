# Use the official Node.js image as the base for building the React app
FROM node:18 as build

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Build the React app
RUN npm run build

# Use a lightweight Nginx image as the runtime image
FROM nginx:alpine

# Copy the built React app from the build stage to the Nginx server's web root
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# The Nginx container starts automatically, so no need for CMD
