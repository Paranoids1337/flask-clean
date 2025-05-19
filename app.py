from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Lakecity,Minnesota',
        'salary': '$1000'
    },
    {
        'id': 2,
        'title': 'Data Science',
        'location': 'Redwing,Minnesota',
        'salary': '$1500'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Texas,USA',
        'salary': '$2500'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Remote',
        'salary': '$3000'
    }
]

# Home page route


@app.route('/')
def home():
    return render_template('index.html',
                           jobs=JOBS)
# Contact page route


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # for now, just print it in terminal
        print(f"Name: {name} , Email: {email} , Message: {message}")
        return F"Thank you , {name}! Your message has been received. We will respond to you at {email}."
    return render_template('contact.html')  # Make sure this route is defined

# Thank-you page route


@app.route('/thank-you')
def thankyou():

    # Make sure the file name matches exactly
    return render_template('thank-you.html')

# About.html page route


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
