import pickle
from flask import Flask, request, render_template,jsonify
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', pred=0)


model = pickle.load(open('model.pkl', 'rb'))
@app.route('/predict', methods=['POST']) #always point immediate function
def predict():

    data = [
                        float(request.form['Age_of_Subject']),
                        float(request.form['Time_class']),
                        (request.form['Rating_class']),
                        (request.form['Medium_class']),
                        float(request.form['spent_study']),
                        float(request.form['spent_fitness']),
                        float(request.form['spent_sleep']),
                        float(request.form['spent_social']),
                        (request.form['platform_media']),
                        float(request.form['spent_tv']),
                        float(request.form['no_meals']),
                        (request.form['weight']),
                        (request.form['Stress']),
                        (request.form['Time_utilized']),
                        (request.form['find_yourself']),
                        (request.form['miss'])
                        ]


    # data[2].replace({'Very poor': 4, 'Average': 0,'Good': 2,'Excellent': 1,'Poor': 3}, inplace=True)
    dic={'Very poor': 4, 'Average': 0,'Good': 2,'Excellent': 1,'Poor': 3}
    data[2]=dic[data[2]]


    # data[3].replace({'Laptop/Desktop': 1, 'Smartphone': 2, 'Smartphone or Laptop/Desktop': 3, 'Any Gadget': 5, 'Tablet': 4}, inplace=True)
    dic = {'Laptop/Desktop': 1, 'Smartphone': 2, 'Smartphone or Laptop/Desktop': 3, 'Any Gadget': 5, 'Tablet': 4}
    data[3] = dic[data[3]]


    # data[8].replace({'Instagram': 2, 'Whatsapp': 13, 'Youtube': 14, 'Linkedin': 3, 'Facebook': 1,'Twitter': 11,'Snapchat': 8,'Reddit': 7,'Telegram': 10,'Talklife': 9,'Omegle': 5,
    #                 'Elyment': 0,'Quora':6}, inplace=True)
    dic = {'Instagram': 2, 'Whatsapp': 13, 'Youtube': 14, 'Linkedin': 3, 'Facebook': 1,'Twitter': 11,'Snapchat': 8,'Reddit': 7,'Telegram': 10,'Talklife': 9,'Omegle': 5,
                    'Elyment': 0,'Quora':6}
    data[8] = dic[data[8]]

    # data[11].replace({'Remain Constant': 2, 'Increased': 1, 'Decreased': 0}, inplace=True)
    dic = {'Remain Constant': 2, 'Increased': 1, 'Decreased': 0}
    data[11] = dic[data[11]]

    # data[12].replace({'Cooking': 9, 'Scrolling through social media': 48, 'Listening to music': 29, 'Watching web series': 65, 'Coding and studying for exams': 8, 'live stream watching': 78, 'Reading': 44,
    #      'Online gaming': 36, 'Sleep': 51}, inplace=True)
    dic = {'Cooking': 9, 'Scrolling through social media': 48, 'Listening to music': 29, 'Watching web series': 65, 'Coding and studying for exams': 8, 'live stream watching': 78, 'Reading': 44,
          'Online gaming': 36, 'Sleep': 51}
    data[12] = dic[data[12]]

    # data[15].replace({'School/college': 39, 'Roaming around freely': 36, 'Travelling': 44, 'Friends,relatives': 15, 'Eating outside': 10,'Colleagues': 9}, inplace=True)
    dic = {'School/college': 39, 'Roaming around freely': 36, 'Travelling': 44, 'Friends,relatives': 15, 'Eating outside': 10,'Colleagues': 9}
    data[15] = dic[data[15]]

    booldic={'Yes':1,'No':0}
    data[13]=booldic[data[13]]
    data[14]=booldic[data[14]]
    print(data)
    data = [data]

    result = model.predict(data)
    return jsonify({"Health_status":str(result[0])})




tmodel = pickle.load(open('treatment.pkl', 'rb'))
@app.route('/treatment', methods=['POST'])
def treatment():
    # (request.form['MetalHealthStatus'])
    data = [
            (request.form['PartTimeEmployment']),
            1,
            (request.form['EducationStatus']),
            (request.form['DeviceWithoutPhone']),
            (request.form['PreviousMentalTreatment']),
            (request.form['Disabled']),
            (request.form['RegularAccessInternet']),
            (request.form['LiveWithFamily']),
            (request.form['StudyGap']),
            float(request.form['Income']),
            (request.form['ReadWithoutCurriculum']),
            (request.form['LongConcentration']),
            (request.form['Anxiety']),
            (request.form['Depression']),
            (request.form['ObsessiveThinking']),
            (request.form['MoodSwings']),
            (request.form['PanicAttacks']),
            (request.form['CompulsiveBehavior']),
            (request.form['Tiredness']),
            (request.form['Age']),
            (request.form['Gender'])
            ]

    dic={'High School or GED':3,'Phd ongoing':4,'graduated':2,'Undergraduate':5,'Masters ongoing':7,'Completed Masters':0,'highschool ongoing':1,'Completed Phd':1}
    data[2]= dic[data[2]]

    dic={'30-44':1,'18-29':0,'45-60':2,'>60':3}
    data[19]=dic[data[19]]

    if(data[20]=='Male'):
        data[20]=1
    else:
        data[20]=0

    booldic = {'Yes': 1, 'No': 0}
    data[0]=booldic[data[0]]
    # data[1]=booldic[data[1]]
    data[3]=booldic[data[3]]
    data[4]=booldic[data[4]]
    data[5]=booldic[data[5]]
    data[6]=booldic[data[6]]
    data[7]=booldic[data[7]]
    data[8]=booldic[data[8]]
    data[10]=booldic[data[10]]
    data[11]=booldic[data[11]]
    data[12]=booldic[data[12]]
    data[13]=booldic[data[13]]
    data[14]=booldic[data[14]]
    data[15]=booldic[data[15]]
    data[16]=booldic[data[16]]
    data[17]=booldic[data[17]]
    data[18]=booldic[data[18]]

    print(data)
    data = [data]

    result = tmodel.predict(data)
    return jsonify({"treatment": str(result[0])})



def main():
    """Run the app."""
    app.run(host='0.0.0.0', port=8000, debug=False)


if __name__ == '__main__':
    main()
