FROM node:16-alpine3.16 as dependencies
WORKDIR /app

COPY package*.json ./

RUN npm install

FROM node:16-alpine3.16 as builder
WORKDIR /app
COPY . .
COPY --from=dependencies /app/node_modules ./node_modules

RUN npm run build 

FROM node:16-alpine3.16 as runner
WORKDIR /app

ENV PORT 3000
ENV REDIS_HOST=redis-primary
ENV REDIS_PORT=6379

COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/.env ./

EXPOSE 3000

CMD ["npm", "run", "start:prod"]