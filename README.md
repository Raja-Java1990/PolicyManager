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