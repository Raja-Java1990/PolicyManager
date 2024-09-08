import pymysql
from controller.app import app
from util.sqlConfig import mysql
from flask import jsonify
from flask import flash, request

from model.Policy import Policy


@app.route('/getAllpolicy')
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
@app.route('/addpolicy', methods =['POST'])
def addPolicy():
    data = request.get_json()
    if not data:
        return jsonify({"error":"No input data provided"}),400

    try:
        policy= Policy.from_dict(data)
        print(policy)
        policy.policyId = 100
        return jsonify({"Policy got created":policy.policyId }),201
    except Exception as e:
        return jsonify({"error":str(e)}),500


if __name__ == "__main__":
    app.run()

