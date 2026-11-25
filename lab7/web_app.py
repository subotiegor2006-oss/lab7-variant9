"""Веб-интерфейс к БД на Flask.

Задание повышенной сложности №9.
"""

from flask import Flask, redirect, render_template_string, request, url_for

from lab7.models import Student, SessionLocal, init_db

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Студенты — ЛР №7</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 800px; margin: 30px auto; padding: 0 16px; }
    h1 { color: #2c3e50; }
    table { border-collapse: collapse; width: 100%; margin: 16px 0; }
    th, td { border: 1px solid #ddd; padding: 8px 12px; text-align: left; }
    th { background: #2980b9; color: #fff; }
    tr:nth-child(even) { background: #f5f7fa; }
    form { margin: 12px 0; display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }
    input, button { padding: 6px 10px; font-size: 14px; }
    button { cursor: pointer; }
    .del { background: #e74c3c; color: #fff; border: none; border-radius: 3px; }
    .add { background: #27ae60; color: #fff; border: none; border-radius: 3px; }
  </style>
</head>
<body>
  <h1>Студенты (веб-интерфейс к БД)</h1>
  <p>ЛР №7, вариант 9 — Flask + SQLAlchemy</p>

  <form method="post" action="{{ url_for('add') }}">
    <input name="name" placeholder="ФИО" required>
    <input name="group_name" placeholder="Группа" required>
    <input name="score" type="number" step="0.1" min="0" max="5" value="4.0" required>
    <button class="add" type="submit">Добавить</button>
  </form>

  <table>
    <thead>
      <tr><th>ID</th><th>ФИО</th><th>Группа</th><th>Балл</th><th></th></tr>
    </thead>
    <tbody>
      {% for s in students %}
      <tr>
        <td>{{ s.id }}</td>
        <td>{{ s.name }}</td>
        <td>{{ s.group_name }}</td>
        <td>{{ s.score }}</td>
        <td>
          <form method="post" action="{{ url_for('delete', student_id=s.id) }}" style="margin:0">
            <button class="del" type="submit">Удалить</button>
          </form>
        </td>
      </tr>
      {% else %}
      <tr><td colspan="5">Нет записей</td></tr>
      {% endfor %}
    </tbody>
  </table>
</body>
</html>
"""


@app.route("/")
def index():
    with SessionLocal() as session:
        students = session.query(Student).order_by(Student.id).all()
    return render_template_string(PAGE, students=students)


@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"].strip()
    group_name = request.form["group_name"].strip()
    score = float(request.form["score"])
    with SessionLocal() as session:
        session.add(Student(name=name, group_name=group_name, score=score))
        session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:student_id>", methods=["POST"])
def delete(student_id: int):
    with SessionLocal() as session:
        student = session.get(Student, student_id)
        if student:
            session.delete(student)
            session.commit()
    return redirect(url_for("index"))


def main() -> None:
    init_db()
    print("Веб-интерфейс: http://127.0.0.1:5000/")
    app.run(debug=True)


if __name__ == "__main__":
    main()
