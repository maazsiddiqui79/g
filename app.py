from flask import Flask, render_template, redirect, url_for, request, flash


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return redirect('https://the-maaz-portfolio.vercel.app/')
