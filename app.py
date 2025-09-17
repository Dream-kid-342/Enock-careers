from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =[
    {'id': 1, 'title': 'Data Analyst', 'location': 'New York, NY', 'salary': '$70,000'},
    {'id': 2, 'title': 'Data Scientist', 'location': 'San Francisco, CA', 'salary': '$120,000'},
    {'id': 3, 'title': 'Frontend Engineer', 'location': 'Remote', 'salary': '$110,000'},
    {'id': 4, 'title': 'Backend Engineer', 'location': 'Austin, TX', 'salary': '$130,000'},
    {'id': 5, 'title': 'Full Stack Developer', 'location': 'Seattle, WA', 'salary': '$125,000'},
]

@app.route('/')
def hello_world():
    return render_template("home.html", jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", debug=True)