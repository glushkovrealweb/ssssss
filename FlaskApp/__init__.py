from flask import Flask, request, render_template
import sys
app = Flask(__name__)
app.debug = True
@app.route("/")
def hello():
    return render_template('main.html')

@app.errorhandler(Exception)
def handle_500(e=None):
    app.logger.error(
        '{}'.format(traceback.format_exc())
    )
    return '{}'.format(traceback.format_exc())	


if __name__ == "__main__":
    app.run()