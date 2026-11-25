"""Асинхронный доступ к БД через aiosqlite.

Повышенная часть: async/await вместо синхронного sqlite3.
"""

import asyncio
from pathlib import Path

import aiosqlite

DB_PATH = Path(__file__).parent.parent / "students_async.db"


async def init_db(db: aiosqlite.Connection) -> None:
    await db.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            name       TEXT NOT NULL,
            group_name TEXT NOT NULL,
            score      REAL DEFAULT 0.0
        )
        """
    )
    await db.commit()
    print("[async] Таблица students создана")


async def insert_students(db: aiosqlite.Connection) -> None:
    students = [
        ("Иванов Алексей", "221341", 4.5),
        ("Петрова Мария", "221341", 4.8),
        ("Сидоров Иван", "221342", 3.9),
    ]
    await db.executemany(
        "INSERT INTO students (name, group_name, score) VALUES (?, ?, ?)",
        students,
    )
    await db.commit()
    print(f"[async] Вставлено {len(students)} записей")


async def list_students(db: aiosqlite.Connection) -> None:
    db.row_factory = aiosqlite.Row
    async with db.execute("SELECT * FROM students ORDER BY id") as cursor:
        rows = await cursor.fetchall()
    print("[async] Записи:")
    for row in rows:
        print(f"  {row['id']}: {row['name']} | {row['group_name']} | {row['score']}")


async def delete_student(db: aiosqlite.Connection, student_id: int) -> None:
    cursor = await db.execute("DELETE FROM students WHERE id = ?", (student_id,))
    await db.commit()
    print(f"[async] Удалено строк: {cursor.rowcount} (id={student_id})")


async def main() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()

    async with aiosqlite.connect(DB_PATH) as db:
        await init_db(db)
        await insert_students(db)
        await list_students(db)
        await delete_student(db, 2)
        await list_students(db)

    print(f"\nБаза: {DB_PATH}")


if __name__ == "__main__":
    asyncio.run(main())
