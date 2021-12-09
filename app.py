import numpy as np
import flask
import pickle
from extension import DATABASE
from config import config
from tax import user
from flask import Flask, render_template, request


app = Flask(__name__)
app.config.from_object(config)
DATABASE.init_app(app)



@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 13)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


def maybeMakeNumber(s):
    if not s:
        return s
    try:
        f = float(s)
        i = int(f)
        return i if f == i else f
    except ValueError:
        return s

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list1 = to_predict_list
        mapp = {}
        loaded_model_string = pickle.load(open("maping.pkl", "rb"))
        li = list(to_predict_list1.values())
        li = list(map(maybeMakeNumber, li))
        mapp['TIN'] = li[0]
        mapp['Country (Legal establishment)'] = li[1]
        mapp['Incorporation type'] = li[2]
        sub2 = loaded_model_string['Taxpayer Category'][li[3]]
        mapp['Taxpayer Category'] = sub2
        mapp['Registered As Individuals'] = li[4]
        mapp['Number of Employee in company'] = li[5]
        sub2 = loaded_model_string['Qatari Company'][li[6]]
        mapp['Qatari Company'] = sub2
        mapp['Profit sharing %'] = li[7]
        sub2 = loaded_model_string['Owner Type'][li[8]]
        mapp['Owner Type'] = sub2
        mapp['Ownership %'] = li[9]
        mapp['Currency'] = li[10]
        mapp['DnBRatings'] = li[11]
        mapp['Establishment Type'] = li[12]
        mapp['Due Date'] = li[13]
        sub2 = loaded_model_string['Compliance Status'][li[14]]
        mapp['Compliance Status'] = sub2
        sub2 = loaded_model_string['Tax Type'][li[15]]
        mapp['Tax Type'] = sub2
        sub2 = loaded_model_string['Economic Sector'][li[16]]
        mapp['Economic Sector'] = sub2
        sub2 = loaded_model_string['Payment Status'][li[17]]
        mapp['Payment Status'] = sub2
        sub2 = loaded_model_string['Filing Status'][li[18]]
        mapp['Filing Status'] = sub2
        mapp['Total Payment'] = li[19]
        mapp['Tax Amount'] = li[20]
        mapp['Late Filing penalty'] = li[21]
        mapp['Late Payment Penalty'] = li[22]
        mapp = list(mapp.values())
        user_model=user()
        user_model.TIN = mapp[0]
        user_model.Country = mapp[1]
        user_model.Incorporation_type = mapp[2]
        user_model.Taxpayer_Category = mapp[3]
        user_model.Registered_As_Individuals = mapp[4]
        user_model.Number_of_Employee_in_company = mapp[5]
        user_model.Qatari_Company = mapp[6]
        user_model.Profit_sharing = mapp[7]
        user_model.Owner_Type = mapp[8]
        user_model.Ownership = mapp[9]
        user_model.Currency = mapp[10]
        user_model.DnBRatings = mapp[11]
        user_model.Establishment_Type = mapp[12]
        user_model.Due_Date = mapp[13]
        user_model.Compliance_Status = mapp[14]
        user_model.Tax_Type = mapp[15]
        user_model.Economic_Sector = mapp[16]
        user_model.Payment_Status = mapp[17]
        user_model.Filing_Status = mapp[18]
        user_model.Total_Payment = mapp[19]
        user_model.Tax_Amount = mapp[20]
        user_model.Late_Filing_penalty = mapp[21]
        user_model.Late_Payment_Penalty = mapp[22]

        del to_predict_list['Registered As Individuals']
        del to_predict_list['Number of Employee in company']
        del to_predict_list['Profit sharing %']
        del to_predict_list['Owner Type']
        del to_predict_list['Incorporation type']
        del to_predict_list['Due Date']
        del to_predict_list['TIN']
        del to_predict_list['Country (Legal establishment)']
        del to_predict_list['Currency']
        del to_predict_list['Establishment Type']
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        if int(result) == 0:
           prediction = 'very low risk'
           if mapp[18] == 'Non Filers':
               reason = "The entered TIN has not filed the tax but the amount is very less so, it is categorised  as very low risk "
           else:
               reason = "The entered TIN has very low amount to be paid so, it is categorised  as very low risk "
        elif  int(result) == 1:
           prediction = 'low risk'
           reason = "They may be late filers and the amount is low so it is categorised as low risk"
        elif int(result) == 2:
            prediction = 'moderate risk'
            reason = "The entered TIN may not file or pay in proper time and the amount is also moderate so, it is categorised  as very moderate risk"
        elif int(result) == 3:
            prediction = 'high risk'
            reason = "The entered TIN may not filed or not payed in proper time and the amount is high"
        else:
           prediction = 'very high risk'
           reason = "The following TIN  not filed or not payed  and the amount is  higher"

        user_model.Risk_factor = prediction
        user_model.Reason = reason
        user_model.save()
        return render_template("result.html", prediction= prediction , reason = reason)




if __name__ == "__main__":
    app.run(debug=True, port=8000)