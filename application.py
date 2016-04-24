from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def application():
	"""Shows the application form"""
	return render_template("application-form.html")

@app.route("/application")
def application_response():
	"""Confirms receipt of application."""
	first_name = request.args.get("firstname")
	last_name = request.args.get("lastname")
	salary = request.args.get("salreq")
	job_title = request.args.get("jobtitle")

	return render_template("application-response.html",
							firstname=first_name,
							lastname=last_name,
							salreq=salary,
							jobtitle=job_title
							)





if __name__ == "__main__":
    app.run(debug=True)
90             