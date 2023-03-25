from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/aml', methods=['GET','POST'])
def aml():
    data =  {
    "Inputs": {
        "input1": [       
        {
            "Pregnancies": 0,
            "Glucose": 137,
            "BloodPressure": 40,
            "SkinThickness": 35,
            "Insulin": 168,
            "BMI": 43.1,
            "DiabetesPedigreeFunction": 2.288,
            "Age": 33,
            "Outcome": 1
        }
        ]
    },
    "GlobalParameters": {}
    }

    body = str.encode(json.dumps(data))

    url = 'http://20.70.9.109:80/api/v1/service/brain/score'
    # Replace this with the primary/secondary key or AMLToken for the endpoint
    api_key = '9KOw0kBlhyVauSeGfgeu72LH4UEx52Wd'

    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")


    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))


@app.route('/about')
def about():
    return 'About'
