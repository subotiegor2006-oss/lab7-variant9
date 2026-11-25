"""sqlite3: создание таблицы, параметры (?), DELETE, экспорт CSV.

Задания средней сложности №1, №6, №9.
"""

import csv
import sqlite3
from contextlib import closing
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "students_sqlite.db"
CSV_PATH = Path(__file__).parent.parent / "students_export.csv"


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_table(conn: sqlite3.Connection) -> None:
    """Задание №1 — создать таблицу students."""
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            name       TEXT NOT NULL,
            group_name TEXT NOT NULL,
            score      REAL DEFAULT 0.0
        )
        """
    )
    conn.commit()
    print("[№1] Таблица students создана")


def insert_students(conn: sqlite3.Connection) -> None:
    """Задание №9 — вставка с параметрами (?)."""
    students = [
        ("Иванов Алексей", "221341", 4.5),
        ("Петрова Мария", "221341", 4.8),
        ("Сидоров Иван", "221342", 3.9),
        ("Козлова Анна", "221341", 5.0),
        ("Морозов Дмитрий", "221343", 4.2),
    ]
    conn.executemany(
        "INSERT INTO students (name, group_name, score) VALUES (?, ?, ?)",
        students,
    )
    conn.commit()
    print(f"[№9] Вставлено {len(students)} записей через параметры (?)")


def show_all(conn: sqlite3.Connection) -> None:
    rows = conn.execute("SELECT * FROM students ORDER BY id").fetchall()
    print("\nТекущие записи:")
    for row in rows:
        print(f"  {row['id']}: {row['name']} | {row['group_name']} | {row['score']}")


def delete_student(conn: sqlite3.Connection, student_id: int) -> None:
    """Задание №6 — DELETE студента (с параметром)."""
    cur = conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"[№6] Удалено строк: {cur.rowcount} (id={student_id})")


def export_to_csv(conn: sqlite3.Connection, path: Path) -> int:
    """Экспорт таблицы students в CSV.

    Использует csv.DictWriter, newline='' и encoding='utf-8'.
    """
    rows = conn.execute(
        "SELECT id, name, group_name, score FROM students ORDER BY id"
    ).fetchall()
    fieldnames = ["id", "name", "group_name", "score"]

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row[key] for key in fieldnames})

    print(f"[CSV] Экспортировано {len(rows)} строк → {path}")
    return len(rows)


def main() -> None:
    # Для демонстрации база пересоздаётся при каждом запуске.
    # Данные, добавленные через веб-интерфейс (students_orm.db), не затрагиваются.
    if DB_PATH.exists():
        DB_PATH.unlink()

    with closing(connect()) as conn:
        create_table(conn)
        insert_students(conn)
        show_all(conn)

        delete_student(conn, 3)
        show_all(conn)

        export_to_csv(conn, CSV_PATH)

    print(f"\nБаза: {DB_PATH}")
    print(f"CSV:  {CSV_PATH}")


if __name__ == "__main__":
    main()
