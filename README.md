# PolicyManager
Policy Manager 

#SQL Table Script 
CREATE TABLE Policy (
    policyId int NOT NULL AUTO_INCREMENT,
    policyName varchar(255),
    startDate Date,
    durationInYears int,
	company varchar(255),
	initialDeposite float,
	policyType varchar(255),
	userTypes varchar(255),
	termsPerYear int,
	termAmount float,
	interest float,
    PRIMARY KEY (policyId)
);

#CURL for postman
#to Get All policy
curl --location 'http://127.0.0.1:5000/getAllpolicy'

#to create new policy
curl --location 'http://127.0.0.1:5000/addpolicy' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "policyName": "ACCIDENTAL Life",
    "startDate": "2024-09-08",
    "durationInYears": 5,
    "company": "IRCTC",
    "initialDeposite": 2000,
    "policyType": "Vehicle Insurance",
    "userTypes": "Regular",
    "termsPerYear": 4,
    "termAmount": 500,
    "interest": 3,
    "userId": "001"
}'