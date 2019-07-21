from flask import Flask, render_template

app = Flask(__name__)
data = [
    {
        'auther': 'kavita',
        'date_created': 'July-09-2019'
    },
    {
        'auther': 'test1',
        'date_created': 'july-06-2018'
    }
]


@app.route('/')
def hello():
    return render_template('hello.html', posts=data)


if __name__ == '__main__':
    app.run(debug=True)
