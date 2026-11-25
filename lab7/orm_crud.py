"""CRUD через SQLAlchemy ORM.

Задание повышенной сложности №2.
"""

from lab7.models import Student, SessionLocal, init_db, DB_PATH


def _to_dict(student: Student) -> dict:
    return {
        "id": student.id,
        "name": student.name,
        "group_name": student.group_name,
        "score": student.score,
    }


def create_student(name: str, group_name: str, score: float) -> dict:
    with SessionLocal() as session:
        student = Student(name=name, group_name=group_name, score=score)
        session.add(student)
        session.commit()
        session.refresh(student)
        return _to_dict(student)


def get_all() -> list[dict]:
    with SessionLocal() as session:
        students = session.query(Student).order_by(Student.id).all()
        return [_to_dict(s) for s in students]


def get_by_id(student_id: int) -> dict | None:
    with SessionLocal() as session:
        student = session.get(Student, student_id)
        return _to_dict(student) if student else None


def update_score(student_id: int, score: float) -> dict | None:
    with SessionLocal() as session:
        student = session.get(Student, student_id)
        if not student:
            return None
        student.score = score
        session.commit()
        session.refresh(student)
        return _to_dict(student)


def delete_student(student_id: int) -> bool:
    with SessionLocal() as session:
        student = session.get(Student, student_id)
        if not student:
            return False
        session.delete(student)
        session.commit()
        return True


def main() -> None:
    # Для демонстрации база пересоздаётся при каждом запуске.
    # Веб-интерфейс использует ту же students_orm.db — после demo данные будут сброшены.
    if DB_PATH.exists():
        DB_PATH.unlink()
    init_db()

    print("[CREATE]")
    create_student("Иванов Алексей", "221341", 4.5)
    create_student("Петрова Мария", "221341", 4.8)
    create_student("Сидоров Иван", "221342", 3.9)

    print("[READ]")
    for s in get_all():
        print(f"  {s['id']}: {s['name']} | {s['group_name']} | {s['score']}")

    print("[UPDATE] id=2 → score=5.0")
    update_score(2, 5.0)

    print("[DELETE] id=3")
    delete_student(3)

    print("[READ после изменений]")
    for s in get_all():
        print(f"  {s['id']}: {s['name']} | {s['group_name']} | {s['score']}")

    print(f"\nБаза: {DB_PATH}")


if __name__ == "__main__":
    main()
