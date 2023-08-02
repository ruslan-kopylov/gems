Запуск проекта:

`docker compose up`

***

Загрузка файла со сделками:

Отправить POST запрос:

form-data: key - deals, value - {file.csv}

http://0.0.0.0:8000/api/load_deals/

***

Получить список покупателей:

Отправить GET запрос на адрес - 
http://0.0.0.0:8000/api/top_five_customers/