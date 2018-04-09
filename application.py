from flask import Flask, render_template, request
import pandas as pd
import datetime
import json

names = []
app = Flask(__name__)
if __name__ == '__main__':
	app.run()

@app.route('/')
def index():
	df = pd.read_csv('Running Log.csv')
	datas = []
	for i in range(len(list(df['Date']))):
		data = []
		data.append(list(df['Date'])[i])
		data.append(format(list(df['Distance'])[i], '.2f'))
		data.append(list(df['Place'])[i])
		data.append(list(df['Time'])[i])
		datas.append(data)
	print(datas)

	return render_template('index.html', datas=datas)

@app.route("/nameData", methods=["POST"])
def nameData():
	df = pd.read_csv('Running Log.csv')
	date = str(request.form.get("date"))
	date = date[5:7] + '/' + date[-2:] + '/' + date[0:4]
	distance = float(request.form.get('distance'))
	time = request.form.get('time')
	place = request.form.get('place')
	df2 = pd.DataFrame([[date,distance,time,place]], columns=['Date','Distance','Time','Place'])
	df = df.append(df2, ignore_index=True)
	df.to_csv("Running Log.csv", index=False)
	return json.dumps({"date":date, "distance":distance, "time": time, "place": place})




