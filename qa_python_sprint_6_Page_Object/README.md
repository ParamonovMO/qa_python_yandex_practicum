# Финальный проект 6 спринта курса "Автоматизатор тестирования на Python" от Яндекс Практикум на тему "Page Object"

Автотесты для сервиса «Яндекс.Самокат». Его разработали специально для студентов.


## Файлы:
- allure_results - каталог с отчетом о тестировании
- tests/ - каталог с автотестами
- tests/test_home_page.py - файл с проверками домашней страницы 
- tests/test_order_page.py - файл с проверками оформления заказа
- conftest.py - файл с фикстурами
- helps/ - каталог с вспомогательными файлами
- helps/data.py - данные со вспомогательными данными для тестирования
- locators/ - каталог с файлами локаторов страниц
- locators/home_page_locators.py - файл с локаторами элементов на домашней страницы
- locators/order_page_locators.py - файл с локаторами элементов на страницах оформления заказа
- pages/ - каталог с файлами страниц
- pages/base_page.py - файл с базовыми методами взаимодействия с элементами
- pages/home_page.py -  файл с методами взаимодействия с домашней страницей
- pages/order_page.py - файл с методами взаимодействия со страницами оформления заказа
- requirements.txt - файл с внешними зависимостями

Перед работой с репозиторием требуется установить зависимости 
```
pip install -r requirements.txt
```
Запустить все тесты из директории tests
```shell
pytest tests --alluredir=allure_results
```
Посмотреть отчет в веб версии пройденного прогона
```
allure serve allure_results
```