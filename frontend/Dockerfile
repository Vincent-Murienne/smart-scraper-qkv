# Étape de build
FROM node:20-alpine AS builder
WORKDIR /app

# Copier uniquement les fichiers nécessaires pour installer les dépendances
COPY frontend/package*.json ./
RUN npm install

# Copier tout le reste du code
COPY frontend/ ./
RUN npm run build

# Étape de déploiement (serveur statique via nginx)
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
