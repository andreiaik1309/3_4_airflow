import requests
import psycopg2


def get_rate_from_api(url, params_api, host, database, user, password):
    try:
        response = requests.get(url, params=params_api)
        data = response.json()

        datetime_rate = data['timestamp']
        value_rate = data['quotes']['BTCRUB']
        conn = psycopg2.connect(host=host,
                                database=database,
                                user=user,
                                password=password)
        cur = conn.cursor()

        # Вставка данных в базу данных
        cur.execute(f"INSERT INTO history_rate_btc_rub (date_rate, value_rate) VALUES (to_timestamp({datetime_rate}), {value_rate})")

        # Завершение транзакции и закрытие соединения
        conn.commit()
        cur.close()
        conn.close()
        print("Данные успешно вставлены в базу данных.")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
    except psycopg2.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")