# Stage 1: Build the React application
FROM node:21-alpine as build
WORKDIR /app
COPY package*.json yarn.lock ./
RUN yarn install
COPY . .
RUN yarn build

# Stage 2: Serve the React application from Nginx
FROM nginx:1.25.4-alpine as serve
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]