import os
import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from forms import CheckData  # custom made package


app = Flask(__name__)
boostrap = Bootstrap5(app)
app.config['SECRET_KEY'] = os.urandom(32)
db = SQLAlchemy()
key = '337f50a0cbf008693f4a3eda316c994e'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CheckData()
    response = None
    if form.validate_on_submit():
        symbol = form.symbol.data.upper()
        response = requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{symbol}?limit=120&apikey='+key).json()
        return render_template('index.html', form=form, response=response)
    return render_template('index.html', form=form, response=response)


if __name__ == '__main__':
    app.run(debug=True)
