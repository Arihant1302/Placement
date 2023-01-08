from best_model_finder import best_model_
from flask import Flask, render_template, request
app = Flask(__name__,static_folder="static",template_folder='templates')

@app.route('/') # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    if (request.method=='POST'):
        ssc_s = int(request.form.get("ssc_p"))
        hsc_s = int(request.form.get("hsc_p"))
        deg_s = int(request.form.get("deg_p"))
        etest_s = int(request.form.get("etest_p"))
        work_exp = int(request.form.get("work-ex"))
        prediction = best_model_.placement_predictor(ssc_s,hsc_s,deg_s,etest_s,work_exp)
        if(prediction=="Placed"):
            return render_template("test.html")
        else:
            return render_template('test2.html')

if __name__ == '__main__':
    app.run(debug=True)


