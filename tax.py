from extension import DATABASE

class user(DATABASE.Document):
    TIN = DATABASE.IntField(required=True , unique=True)

    Country = DATABASE.StringField(required=True)

    Incorporation_type = DATABASE.StringField(required=True)

    Taxpayer_Category = DATABASE.StringField(required=True)

    Registered_As_Individuals = DATABASE.StringField(required=True)

    Number_of_Employee_in_company = DATABASE.IntField(required=True)

    Qatari_Company = DATABASE.StringField(required=True)

    Profit_sharing = DATABASE.IntField(required=True)

    Owner_Type = DATABASE.StringField(required=True)

    Ownership = DATABASE.IntField(required=True)

    Currency = DATABASE.StringField(required=True)

    DnBRatings = DATABASE.IntField(required=True)

    Establishment_Type = DATABASE.StringField(required=True)

    Due_Date = DATABASE.StringField(required=True)

    Compliance_Status = DATABASE.StringField(required=True)

    Tax_Type = DATABASE.StringField(required=True)

    Economic_Sector = DATABASE.StringField(required=True)

    Payment_Status = DATABASE.StringField(required=True)

    Filing_Status = DATABASE.StringField(required=True)

    Total_Payment = DATABASE.FloatField(required=True)

    Tax_Amount = DATABASE.FloatField(required=True)

    Late_Filing_penalty = DATABASE.FloatField(required=True)

    Late_Payment_Penalty = DATABASE.FloatField(required=True)

    Risk_factor = DATABASE.StringField(required=True)

    Reason = DATABASE.StringField(required=True)

