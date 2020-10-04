from flask import Flask, render_template, request
import googleclouddebugger

app = Flask(__name__)


@app.route("/")
def main():
    model = {"title": "Convert Fahrenheit to Celsius"}
    return render_template('index.html', model=model)


@app.route("/temp", methods=['GET', 'POST'])
def temp():

    if request.method == 'GET':
        model = {"title": "Convert Fahrenheit to Celsius",
                 "fah": "Enter a number", "cel": ""}

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        input = data["fahrenheit"]
        if input.isnumeric():
            fahrenheit = float(input)
            celsius = (fahrenheit - 32.0) * 5.0 / 9.0
        else:
            fahrenheit = "Enter a number"
            celsius = "Invalid Input"

        model = {"title": "Convert Fahrenheit to Celsius",
                 "fah": fahrenheit, "cel": celsius}

    return render_template('temp.html', model=model)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    print('An error occurred during a request.')
    return 'An internal error occurred.', 500


# Enable's the Debugger.
try:
    googleclouddebugger.enable()
except (ImportError, RuntimeError, RuntimeError, Exception) as ext:
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
