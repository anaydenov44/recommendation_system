# Рекомендательная система с защитой (DevOps проект)

## Описание
Проект реализует рекомендательную систему в финансовом секторе
Используются технологии:  
- **Flask** — бэкенд рекомендаций  
- **Nginx** — прокси, логирование в JSON  
- **MySQL** — хранение данных  
- **Fail2ban** — защита от частых запросов  

## Сборка и запуск
bash
git clone https://github.com/anaydenov44/recommendation_system.git
cd recommendation_system

# Запуск системы
docker-compose up -d
