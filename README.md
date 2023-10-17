# Структура репозитория
Папка airflow:
  1) dags:
     1.1) api_live_currency.py (скрипт с получением данных курса и записи значений в таблицу)
     1.2) hell.py (скрипт создает даг)

папка ddl:
  1) create_table.sql (создает тадлицу для сохранения курсов валют)

docker-compose.yml (запуск контейнера: создается 8 контейнеров)


# Алгоритм работы

скачайте репозиторий на локальный ПК;

в терминале перейдите в директорию, где сохранили данный проект;

в командной строке запустите команду docker-compose up -d;

подключите базу данных к клиенту управления базами данных и изучите:
    Таблица: history_rate_btc_rub (данные в таблицу добавляются каждые 10 минут)

войдите http://localhost:8080/dags/currency_btc_rub_every_10_munutes/, чтобы отследить работу Airflow
