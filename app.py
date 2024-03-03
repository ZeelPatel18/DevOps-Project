import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'default_user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'default_password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'default_db')

# Initialize MySQL
mysql = MySQL(app)

@app.route('/')
def product_list():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM products')
    products = cur.fetchall()
    cur.close()
    return render_template('index.html', products=products)

@app.route('/submit', methods=['POST'])
def submit():
    product_name = request.form.get('name')
    price = request.form.get('price')
    quantity = request.form.get('quantity')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO products (product_name, price, quantity) VALUES (%s, %s, %s)', (product_name, price, quantity))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('product_list'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
