# Лабораторная работа №7

Субботин Егор Сергеевич, группа 221341, вариант 9, лабораторная №7.

## Задания варианта

Средняя сложность:

- №1 — создать таблицу students
- №6 — DELETE студента
- №9 — использование параметров (?)

Повышенная сложность:

- №2 — CRUD через ORM (SQLAlchemy)
- №9 — веб-интерфейс к БД (Flask)

## Зависимости

```bash
pip install -r requirements.txt
```

## Запуск

### sqlite3 (средние задания)

```bash
python -m lab7.sqlite_demo
```

### ORM CRUD

```bash
python -m lab7.orm_crud
```

### Веб-интерфейс

```bash
python -m lab7.web_app
```

Откройте http://127.0.0.1:5000/

## Структура

```text
lab7/
├── __init__.py
├── sqlite_demo.py    # №1, №6, №9 — sqlite3
├── models.py         # SQLAlchemy модели
├── orm_crud.py       # №2↑ — CRUD через ORM
└── web_app.py        # №9↑ — Flask UI к БД
```
