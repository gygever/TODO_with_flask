from model import app, db, Tasks

form_tasks = []

@app.route('/')
def hello_world():
    global form_tasks
    tasks = Tasks.query.all()
    for i in tasks:
        form_tasks.append(str(i.id)+' Название: '+i.title+' Описание:'+i.content)
    return '\n'.join(i for i in form_tasks)


if __name__ == '__main__':
    app.run()
