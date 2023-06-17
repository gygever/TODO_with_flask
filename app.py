from model import app, db, Tasks


@app.route('/')
def hello_world():
    res = Tasks.query.all()
    return res[0].title + ' '  + res[0].content


if __name__ == '__main__':
    app.run()
