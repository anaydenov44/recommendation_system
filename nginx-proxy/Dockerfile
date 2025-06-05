FROM alpine:latest

# Установка Nginx и OpenSSL
RUN apk add --no-cache nginx openssl

# Генерация директории для сертификатов
RUN mkdir -p /etc/nginx/certs

# Генерация самоподписанного сертификата
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/certs/nginx.key \
    -out /etc/nginx/certs/nginx.crt \
    -subj "/C=RU/ST=Moscow/L=Moscow/O=Bank/OU=IT/CN=localhost"

# Копирование конфига Nginx
COPY nginx.conf /etc/nginx/

# Открытие порта
EXPOSE 443

# Запуск Nginx
CMD ["nginx", "-g", "daemon off;"]
