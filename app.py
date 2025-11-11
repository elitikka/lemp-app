from flask import Flask
import mysql.connector

app = Flask(__name__)
@app.route('/')
def home():
 # Connect to MySQL
 conn = mysql.connector.connect(
host="localhost",
 user="exampleuser",
 password="BemmusKa94.",
 database="exampledb"
 )

 cursor = conn.cursor()
 cursor.execute("SELECT 'Sivu on personoitu'")
 personointi = cursor.fetchone()
 cursor.execute("SELECT 'Versiohallintaan käytetty: https://github.com/elitikka/lemp-app'")
 versiohallinta = cursor.fetchone()
 cursor.execute("SELECT NOW();")
 time = cursor.fetchone()


 # Clean up
 cursor.close()
 conn.close()
 return f"<h1>{personointi[0]}</h1><h2>{versiohallinta[0]}</h2><h3>{str(time[0])}</h3>"
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)