from flask import Flask
from flask import request
from flask import jsonify
from validator import validate
from validator import rules as R
from decimal import Decimal
import csv
import json

app = Flask(__name__)

# test route
@app.route('/ping')
def res():
    return jsonify({"message": "pong"})

# get all data
@app.route('/getAll')
def getAll():
    with open('../datasets/dataset.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        response = {}
        for num, row in enumerate(spamreader, start=1):
            response[num] = (', '.join(row))
        return jsonify(response)

# getFiltered data by indicator and value
# state: OK/error message: response message
@app.route('/getFiltered', methods=['POST'])
def getFiltered():
    res = {"indicator":"","value":0}
    res['indicator'] = request.form['indicator']
    res['value'] = request.form['value']
    # print(request)
    # Rules to verify before
    rule = {"indicator": [R.Required(), R.Min(7)],
            "value": [R.Required(), R.Min(0)]}

    result, validated_data, _ = validate(res, rule, return_info=True)
    
    # result of Decimal validation
    if result == True:
        inputValue = decimal_cast(validated_data['value'])
        if inputValue == None:
            result = False

    #if basic validation is true
    if result == True:
        
        indicator = validated_data['indicator']
        # fixed value, can be other aditional parameter
        fixed_filter = "TOT"
        res = {}
        # open .csv and use filter (first inqueality , second indicator , third value)
        with open('../datasets/dataset.csv', newline='') as csvfile:
            listReader = csv.reader(csvfile, delimiter=',', quotechar='|')
            listFilteredTOT = filter(lambda p: p[6].replace('"','') == fixed_filter, listReader)
            listFilteredIndicator = filter(lambda p: p[2].replace('"','') == indicator, listFilteredTOT)
            listFilteredValue = filter(lambda p: Decimal(p[14]) > Decimal(inputValue), listFilteredIndicator)
            index = 0
            
            # Filter by country name, can be all data, some fields, etc
            for x in listFilteredValue:
                y = slice(1,15,13)
                res[index] = x[y]
                index = index + 1

            return jsonify({"status": "OK", "message": res})
    else:
        return jsonify({"status": "error", "message": "Please enter valid parameters"})

def decimal_cast(val, default=None):
    try:
        return Decimal(val)
    except:
        return default

if __name__ == '__main__':
    app.run(debug=True)
