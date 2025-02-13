# Sprint_7
# Ничего не могу сделать с тестом, он падает по таймауту: FAILED tests/test_login_courier.py::TestLoginCourier::test_login_without_required_key[user_data_without_password] - assert 504 == <HTTPStatus.BAD_REQUEST: 400>

* Установка и запуск
```
python3.9
```
* Установка
```bash
pip install -r requirements.txt 
```
* Запуск
```bash
pytest tests/ --alluredir=allure_results 
```
* Формирование отчета
```bash
allure generate allure_results -o allure_report
```
* Просмотр отчета по тестированию
```bash
allure open allure_report
```
