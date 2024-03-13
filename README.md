# DBManager

<!-- ABOUT THE PROJECT -->
## О проекте
*Код для интеграции с внешним сервисом через API и загрузки полученных данных в БД PostgreSQL*


## Основные шаги проекта
1.	Получает данные о работодателях и их вакансиях с сайта hh.ru. Для этого используется публичный API hh.ru и библиотеку requests.
2.	Проектирует таблицы в БД PostgreSQL для хранения полученных данных о работодателях и их вакансиях. Для работы с БД используется библиотеку psycopg2.
3.	Заполняет созданные в БД PostgreSQL таблицы данными о работодателях и их вакансиях.
4.	Подключается к БД PostgreSQL и реализует следующие запросы:

       * получает список всех компаний и количество вакансий у каждой компании;
       * получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию;
       * получает среднюю зарплату по вакансиям;
       * получает список всех вакансий, у которых зарплата выше средней по всем вакансиям;
       * получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.


## Структура проекта

В проекте есть следующие директории и файлы:
*	src — содержит классы (для работы с API hh.ru и БД PostgreSQL)
*	main.py - содержит код для запуска программы
*	config.py - содержит абсолютный путь до переменной окружения

<!-- GETTING STARTED -->
## Подготовка к работе

Чтобы запустить локальную копию, выполните следующие простые шаги.

### Установка

1. Клонируйте проект
   ```sh
   git@github.com:aukhadieva/DBManager.git
   ```
2. Убедитесь, что вы получили из удаленного репозитория все ветки и переключились на ветку разработки develop
   ```sh
   git checkout develop
   ```
3. Установите зависимости проекта (в случае, если не установились при клонировании)
   ```sh
   poetry install
   ```
