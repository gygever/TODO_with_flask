from model import Tasks, db
from flask import render_template, request, Flask

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)


@app.route('/')
def show():
    tasks = Tasks.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        task_title = request.form['title']
        task_content = request.form['content']
        task = Tasks(title=task_title, content=task_content)
        db.session.add(task)
        db.session.commit()
        tasks = Tasks.query.all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id_del>', methods=['POST'])
def delete(id_del):
    task = Tasks.query.get(id_del)
    db.session.delete(task)
    db.session.commit()
    tasks = Tasks.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/edit/<int:id_red>', methods=['GET', 'POST'])
def edit(id_red):
    pass


if __name__ == '__main__':
    app.run(debug=True)
