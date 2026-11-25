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

Дополнительно: экспорт в CSV, асинхронный доступ через aiosqlite.

## Зависимости

```bash
pip install -r requirements.txt
```

## Запуск

```bash
# sqlite3: таблица, параметры (?), DELETE, экспорт CSV
python -m lab7.sqlite_demo

# SQLAlchemy ORM CRUD
python -m lab7.orm_crud

# Веб-интерфейс + /export
python -m lab7.web_app
# http://127.0.0.1:5000/
# http://127.0.0.1:5000/export

# Асинхронный доступ (aiosqlite)
python -m lab7.async_demo
```

## Важно

- `sqlite_demo` и `orm_crud` **пересоздают** свои файлы БД при каждом запуске (`students_sqlite.db` / `students_orm.db`).
- Веб-интерфейс использует `students_orm.db`. Если сначала запустить `orm_crud`, данные веб-интерфейса будут сброшены.
- `app.run(debug=False)` — безопасный режим. Для отладки передайте `debug=True` вручную.

## Структура

```text
lab7/
├── __init__.py
├── sqlite_demo.py    # №1, №6, №9 + export_to_csv
├── models.py         # SQLAlchemy модели
├── orm_crud.py       # №2↑ — CRUD через ORM
├── web_app.py        # №9↑ — Flask UI + /export
└── async_demo.py     # aiosqlite async/await
```

## Кратко по заданиям

| № | Что сделано |
|---|-------------|
| 1 | `CREATE TABLE students` |
| 6 | `DELETE FROM students WHERE id = ?` |
| 9 | `executemany(..., (?, ?, ?))` — параметры |
| 2↑ | create / read / update / delete через ORM |
| 9↑ | Flask: список, добавление, удаление, `/export` |
| + | `export_to_csv()` + aiosqlite |
