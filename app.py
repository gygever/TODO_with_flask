from model import Tasks, app, db
from flask import render_template, request


@app.route('/')
def show():
    tasks = Tasks.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/add')
def add():
    pass


@app.route('/delete/<int:id_del>', methods=['POST'])
def delete(id_del):
    task = Tasks.query.get(id_del)
    db.session.delete(task)
    db.session.commit()
    tasks = Tasks.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
