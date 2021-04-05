from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL
import json, random

SCC = open('../dump-countries-toJson/state-city-country.json')
geolocs = json.load(SCC)

 
app = Flask(__name__)
CORS(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = '####'
app.config['MYSQL_PASSWORD'] = '###'
app.config['MYSQL_DB'] = 'flask-Ng'
mysql = MySQL(app)

@app.route("/")
def insert():
	global geolocs
	cur = mysql.connection.cursor()
	cur.execute(''' select * from purchaseOrdersMain''')
	rv = cur.fetchall()   # a tuple ((col1,col2...coln), (col1,col2, ...coln).... (..))
	geolocs = [random.choice(geolocs) for _ in range(len(rv))]								 

	data = [(*r, *g) for r, g in zip(rv, geolocs)]
	print("\n\nDebug:\n\n")
	print(len(data), len(rv))
	print(data[1:10])
	
	cur.executemany(''' INSERT INTO purchase_orders 
					(Order_ID, First_Name, Last_Name, Email, Product_ID, Quantity, Unit_Price, Country, State, City) values
					(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', data)
	mysql.connection.commit()
	return jsonify(data[1:10])


