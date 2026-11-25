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

```bash
# sqlite3: таблица, параметры, DELETE
python -m lab7.sqlite_demo

# SQLAlchemy ORM CRUD
python -m lab7.orm_crud

# Веб-интерфейс
python -m lab7.web_app
# http://127.0.0.1:5000/
```

## Структура

```text
lab7/
├── __init__.py
├── sqlite_demo.py    # №1, №6, №9 — sqlite3
├── models.py         # SQLAlchemy модели
├── orm_crud.py       # №2↑ — CRUD через ORM
└── web_app.py        # №9↑ — Flask UI к БД
```

## Кратко по заданиям

| № | Что сделано |
|---|-------------|
| 1 | `CREATE TABLE students` |
| 6 | `DELETE FROM students WHERE id = ?` |
| 9 | `executemany(..., (?, ?, ?))` |
| 2↑ | create / read / update / delete через ORM |
| 9↑ | Flask: список, добавление, удаление |
