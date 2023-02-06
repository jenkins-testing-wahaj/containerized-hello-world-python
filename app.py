from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', message="Hello World..!!")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


# #!/usr/bin/env python
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# @app.route('/hello/')
# def hello_world():
#     return 'Hello World!\n'

# @app.route('/hello/<username>') # dynamic route
# def hello_user(username):
#     return 'Why Hello %s!\n' % username

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')     # open for everyone