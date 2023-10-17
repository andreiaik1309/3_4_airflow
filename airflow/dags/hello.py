from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from api_live_currency import get_rate_from_api

# Настройка аргументов для DAG
default_args = {
    'owner': 'Andrey1309',
    'start_date': datetime(2023, 10, 17),  # Укажите дату начала выполнения
    'retries': 1,
    'retry_delay': timedelta(minutes=5),  # Интервал повторных попыток выполнения
}

# Создание объекта DAG
dag = DAG(
    'currency_btc_rub_every_10_munutes',
    default_args=default_args,
    schedule_interval='*/10 * * * *',  # Расписание для выполнения каждые 10 минут
    catchup=False,  # Запрет выполнения отставших задач
)

# Оператор PythonOperator, который выполнит функцию из отдельного файла
python_task = PythonOperator(
    task_id='get_rate_from_api_task',
    python_callable=get_rate_from_api,
    op_kwargs={'url': 'http://api.exchangerate.host/live', 
             'params_api': {'access_key': 'b56fa97aaac1908f5b8f9943cd9a02e5',
              'source': 'BTC',
              'currencies': 'RUB'},
             'host': 'db',
             'database': 'test',
             'user': 'postgres',
             'password': 'postgres'},
    dag=dag,
)


# Оператор, который выполнит указанную команду
bash_task = BashOperator(
    task_id='good_morning_task',
    bash_command='echo "Good morning my diggers!"',  # Команда для выполнения
    dag=dag,
)

# порядок выполнения задач
bash_task >> python_task 

