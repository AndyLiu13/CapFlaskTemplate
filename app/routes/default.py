from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/Climate')
def Climate():
    return render_template('Climate.html')

@app.route('/Solution')
def Solution():
    return render_template('Solution.html')

@app.route('/youth')
def youth():
    return render_template('youth.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/game')
def game():
    return render_template('game.html')
@app.route('/mars')
def mars():
    return render_template('mars.html')

@app.route('/earth')
def earth():
    return render_template('earth.html')
@app.route('/city')
def city():
    return render_template('city.html')
@app.route('/village')
def village():
    return render_template('village.html')
@app.route('/good')
def good():
    return render_template('goodcar.html')
@app.route('/bad')
def bad():
    return render_template('badcar.html')
@app.route('/school')
def school():
    return render_template('school.html')
@app.route('/result')
def result():
    return render_template('results.html')
@app.route('/gasresult')
def gasresult():
    return render_template('gasresult.html')
@app.route('/gascar')
def gascar():
    return render_template('gascar.html')
@app.route('/driveresult')
def driveresult():
    return render_template('driveresult.html')
@app.route('/endresult')
def endresult():
    return render_template('endresult.html')