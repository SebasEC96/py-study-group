from sassutils.wsgi import SassMiddleware
import requests
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'main': ('static/sass', 'static/css', '/static/css')
})


@app.errorhandler(404)
def page_not_found(e):
    return 'ERROR 404', 404


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/user/<name>')
def profile(name):
    request = requests.get('https://api.github.com/users/'+name)
    profile = request.json()
    if ('message' in profile):
        return redirect(url_for('error404'))
    else:
        date = datetime.strptime(
            profile['created_at'], "%Y-%m-%dT%H:%M:%S%z").date().strftime("%d/%m/%y")
        return render_template('profile.html', profile=profile, date=date)


@app.route('/error')
def error404():
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
