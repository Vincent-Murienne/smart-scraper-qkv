FROM node:20-alpine

WORKDIR /app

# Copier package.json en premier (cache)
COPY package*.json ./
RUN npm install

# Copier le reste du code
COPY . .

# Configuration Vite pour développement
EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "--port", "5173"]
