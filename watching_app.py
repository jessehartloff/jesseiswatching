from flask import Flask, send_from_directory, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    resp = make_response(send_from_directory('public', "index.html"))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.route('/<path:filename>')
def serve_static(filename):
    resp = make_response(send_from_directory('public', filename))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
