# Sprint_7
# Комментарий: Иногда тесты падают по таймауту, ничего не могу с этим сделать

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
