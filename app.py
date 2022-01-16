import pickle
from flask import Flask, request, render_template,jsonify

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def index():
    return render_template('index.html', pred=0)
@app.route('/predict', methods=['POST'])
def predict():
    data = [float(request.form['Age_of_Subject']),
            float(request.form['Time_class']),
            float(request.form['Rating_class']),
            float(request.form['Medium_class']),
            float(request.form['spent_study']),
            float(request.form['spent_fitness']),
            float(request.form['spent_sleep']),
            float(request.form['spent_social']),
            float(request.form['platform_media']),
            float(request.form['spent_tv']),
            float(request.form['no_meals']),
            float(request.form['weight']),
            float(request.form['Stress']),
            float(request.form['Time_utilized']),
            float(request.form['find_yourself']),
            float(request.form['miss'])
            ]
    data = [data]
    print(data)

    predictions = model.predict(data)
    print('INFO Predictions: {}'.format(predictions))

    dic_pred = {0: "Insufficient_Weight", 1: "Normal Weight", 2: "Overweight ",
                3: "Obesity"}

    #predi = dic_pred[predictions[0]]

    return jsonify({'res':str(predictions[0])})


def main():
    """Run the app."""
    app.run(host='0.0.0.0', port=8000, debug=False)


if __name__ == '__main__':
    main()