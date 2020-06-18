
from flask import Flask, jsonify, request

from libs.cases import get_covid_cases
from libs.timedate import getdate

# from libs import reader
# from libs import countries

# creating out flask object
app = Flask(__name__)

# creating our app decorator
# returning an API end point by using jsonify
@app.route("/api/v1", methods=["GET"])
@app.route("/api/v1/<date>", methods=["GET"])
def index(date=None):

    query_date= request.args.get("date")  # queryparams
    # body_data = request.jsonify

    # print(body_data) # This is used when you want to pass data to the request.

    # cases=get_covid_cases(URL)
    if date is None:
        yesterday = getdate()
        cases = get_covid_cases(yesterday)
        if query_date is not None:
            d = query_date
        else:
            d = getdate()
        cases = get_covid_cases(d)
    else:
        cases = get_covid_cases(date)
    #     if request.args.get("date") is not None:
    #         d = query_date
    #     else:
    #         getdate()
    #    # print("date: " + date)
    # else:
    #     # print(date)
    #     cases = get_covid_cases(date)

    return jsonify({'total_cases':cases})

if __name__=="__main__":
    app.run(debug=True)