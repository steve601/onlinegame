from flask import Flask,request,render_template
from source.main_project.pipeline.predict_pipeline import PredicPipeline,UserData

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('game.html')

@app.route('/predict',methods = ['POST'])
def do_prediction():
    form_inputs = UserData(
        gender=request.form.get('gen'),
        location=request.form.get('loc'),
        gamegenre=request.form.get('game'),
        ingamepurchases=request.form.get('purch'),
        gamedifficulty=request.form.get('diff'),
        sessionsperweek=request.form.get('sess'),
        avgsessiondurationminutes=request.form.get('dur'),
        playerlevel=request.form.get('level'),
        achievementsunlocked=request.form.get('ach')
    )
    form_inputs_df = form_inputs.get_data_as_df()
    
    predict_pipe = PredicPipeline()
    pred = predict_pipe.predict(form_inputs_df)
    
    if pred == 0:
        msg = 'Level of engagement of the player is likely to be low'
    if pred == 1:
        msg = 'Level of engagement of the player is likely to be medium'
    else:
        msg = 'Level of engagement of the player is likely to be high'
        
    return render_template('game.html',text=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0")