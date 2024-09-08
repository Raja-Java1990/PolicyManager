import pymysql
from policyController.app import app
from config.sqlConfig import mysql
from flask import jsonify
from flask import flash, request



@app.route('/policy')
def getpolicy():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM policy")
        policyRows = cursor.fetchall()
        respone = jsonify(policyRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run()

