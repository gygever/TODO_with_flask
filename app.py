from model import app, db, Tasks
from flask import render_template


@app.route('/')
def hello_world():
    tasks = Tasks.query.all()
    return render_template('index.html', tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)
