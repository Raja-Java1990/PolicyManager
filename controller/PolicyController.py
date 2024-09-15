import pymysql
from controller.app import app
from util.sqlConfig import db
from flask import jsonify
from flask import request
from model.Policy import Policy
from service.PolicyService import validateInputDate, validateInputpolicyType

@app.route('/getAllpolicy')
def getpolicy():
    try:
        #query all policies
        allPolicy = Policy.query.all()
        return jsonify([{"policyId": item.policyId,
            "policyName": item.policyName,
            "startDate": item.startDate,
            "durationInYears": item.durationInYears,
            "company": item.company,
            "initialDeposite": item.initialDeposite,
            "policyType": item.policyType,
            "userTypes": item.userTypes,
            "termsPerYear": item.termsPerYear,
            "termAmount": item.termAmount,
            "interest": item.interest,
            "userId": item.userId} for item in allPolicy])
    except Exception as e:
        print(e)
    finally:
        pass
@app.route('/addpolicy', methods =['POST'])
def addPolicy():
    data = request.get_json()
    if not data:
        return jsonify({"error":"No input data provided"}),400

    try:
        policy= Policy.from_dict(data)
        validateInputpolicyType(policy.policyType)
        validateInputDate(policy.startDate)
        db.session.add(policy)
        db.session.commit()
        return jsonify({"Policy got created":policy.policyId }),201
    except Exception as e:
        return jsonify({"error":str(e)}),500
    finally:
        db.session.close()


if __name__ == "__main__":
    app.run()

