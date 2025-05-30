from flask import Flask
from flask import render_template,request

app = Flask(__name__)


@app.route("/")
def home():
    content = 'Flask-Jinja-Test'
    return render_template(
        "hello.html",
        title='Hello',
        content=content
    )


@app.route('/', methods=["GET", "POST"])
def main_function():
    if request.method == "POST":
        text = request.form
        emails = text['email']
        output = "Received: " + emails
        return render_template("show.html", prediction=output)
    else:
        return render_template("index.html")

@app.route("/handled")
def bad_route_handled():
    try:
        raise ArithmeticError('Hello')
    except Exception:
        pass
    return render_template(
        "hello.html",
        title='Hello',
        content='Flask-Jinja-Test'
    )


@app.route("/unhandled")
def bad_route_unhandled():
    raise ArithmeticError('Hello')
    return render_template(
        "hello.html",
        title='Hello',
        content='Flask-Jinja-Test'
    )


@app.route("/bad_template")
def bad_template():
    return render_template(
        "bad.html",
        title='Bad',
       content='Flask-Jinja-Test'
    )
        
        
@app.route("/exit")
def exit_app():
    from flask import request
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('No shutdown')
    func()
    return 'Done'
        
        
if __name__ == '__main__':
    app.run()


