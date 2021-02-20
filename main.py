#!/usr/bin/python
from flask import Flask
from src.fitnessGrapher import masterApplication

deployedApp = "http://health-grapher.herokuapp.com/fitnessGrapher/"
app = Flask(__name__)

@app.route("/")
def hello():
	return f"""
	<a href={deployedApp}><h1>Fitness Understanding Tool (V1)</h1></a>
	<code>This <a href={deployedApp}>application</a> interfaces with the official FitBit Web API to extract and visualize my own personal smartwatch data.<br >
	Explored metrics include daily steps, distance travelled, heart rate, and caloric output.<br >
	Currently requesting data between <em>2019-06-17</em> and <em>2019-11-01</em> inclusively.
	<br>
	<p>Technologies: Python - Flask/Dash framework, Hosted on Heroku</p>
	<br >
	<p>Developed with ❤️ by Kamran Choudhry!</p>
	</code>
	"""

#
masterApplication(app)
#

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)