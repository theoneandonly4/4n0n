from flask import Flask, escape, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/service')
@app.route('/service/<service>')
@app.route('/service/<service>/<view>')
def service(service=None, view=None):
    if service == None:
        return 'Services Table Page with most popular Services'
    else:
        if view == None:
            view = 'all'
        return 'Service page for %s with view %s' % (escape(service), escape(view))

@app.route('/posts')
@app.route('/post/<post>')
def post(post=None):
    return 'Blog entry: %s' % escape(post)

@app.route('/about')
def about():
    return '4n0n info'

@app.route('/contact')
def contact():
    return '4n0n contact info'

@app.route('/support-us')
def support():
    return 'How to support 4n0n'
