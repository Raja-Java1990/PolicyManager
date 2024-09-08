from util.sqlConfig import db


class Policy(db.Model):
    __tablename__ = 'policy'
    policyId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    policyName = db.Column(db.String(100), nullable=False)
    startDate = db.Column(db.String(100), nullable=False)
    durationInYears = db.Column(db.Integer)
    company = db.Column(db.String(100), nullable=False)
    initialDeposite = db.Column(db.Integer)
    policyType = db.Column(db.String(100), nullable=False)
    userTypes = db.Column(db.String(100), nullable=False)
    termsPerYear = db.Column(db.Integer)
    termAmount = db.Column(db.Integer)
    interest = db.Column(db.Integer)

    def __init__(self, policyId, policyName, startDate,
                 durationInYears, company,
                 initialDeposite, policyType,
                 userTypes, termsPerYear,
                 termAmount, interest):
        self.policyId = policyId
        self.policyName = policyName
        self.startDate = startDate
        self.durationInYears = durationInYears
        self.company = company
        self.initialDeposite = initialDeposite
        self.policyType = policyType
        self.userTypes = userTypes
        self.termsPerYear = termsPerYear
        self.termAmount = termAmount
        self.interest = interest

    @classmethod
    def from_dict(cls, data):
        return cls(
            policyId=data.get('policyId'),
            policyName=data.get('policyName'),
            startDate=data.get('startDate'),
            durationInYears=data.get('durationInYears'),
            company=data.get('company'),
            initialDeposite=data.get('initialDeposite'),
            policyType=data.get('policyType'),
            userTypes=data.get('userTypes'),
            termsPerYear=data.get('termsPerYear'),
            termAmount=data.get('termAmount'),
            interest=data.get('interest')
        )

    def to_dict(self):
        return {
            "policyId": self.policyId,
            "policyName": self.policyName,
            "startDate": self.startDate,
            "durationInYears": self.durationInYears,
            "company": self.company,
            "initialDeposite": self.initialDeposite,
            "policyType": self.policyType,
            "userTypes": self.userTypes,
            "termsPerYear": self.termsPerYear,
            "termAmount": self.termAmount,
            "interest": self.interest,
        }
