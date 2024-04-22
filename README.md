
<h2 align="center">Курсовая работа Django DRF</h2>

Приложение платформы онлайн обучения с возможностью оплаты через Stripe.


<!-- USAGE EXAMPLES -->
## Usage

Перед запуском web-приложения создайте базу данных, создайте и примените миграции, установите необходимые пакеты из файла requirements.txt и заполните файл .env по образцу .env.example. Используйте команду "python manage.py csu" для создания суперпользователя и "python manage.py moderator" для создания группы с функционалом менеджера. Для запуска используйте команду "python manage.py runserver" либо через конфигурационные настройки PyCharm.


### Docker 
Создать образы и контейнеры DOCKER с помощью команд: "docker-compose build" и "docker-compose up".


## Структура проекта

config/

    settings.py - настройки приложений
    urls.py - файл маршрутизации
    celery.py - настройки Celery

study/

    management/commands
        add_payments - команда загрузки списка платежей в БД
    migrations/
        папка с миграциями
    admin.py - настройки админки
    pagination.py - пагинация
    permissions.py - права доступа
    models.py - модели приложения
    serializers.py - сериализаторы
    services.py - сервисные функции
    tasks.py - отложенные и периодические задачи
    tests.py - тесты
    urls.py - файл маршрутизации приложения
    validatots.py - валидация
    views.py - контроллеры

users/

    management/commands
        csu - кастомная команда создания суперпользователя
        moderator - кастомная команда для создания группы с функционалом модератора
        create_user - создать юзера через терминал
    admin.py - настройки админки
    permissions.py - права доступа
    serializers.py - сериализаторы
    tasks.py - отложенные и периодические задачи
    models.py - модели приложения
    urls.py - файл маршрутизации приложения
    views.py - контроллеры

manage.py - точка входа веб-приложения

requirements.txt - список зависимостей для проекта.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

kettariec@gmail.com

https://github.com/Kettariec/drf_homework

<p align="right">(<a href="#readme-top">back to top</a>)</p>