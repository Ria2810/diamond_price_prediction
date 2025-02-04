from urllib.parse import quote as url_quote
from flask import Flask, render_template, request
import model.model as m

app = Flask(__name__)
features = ['cut', 'color', 'clarity', 'carat_weight', 'cut_quality', 'lab', 'symmetry', 'polish', 'eye_clean', 'culet_size', 'culet_condition', 'depth_percent', 'table_percent', 'meas_length', 'meas_width', 'meas_depth', 'girdle_min', 'girdle_max', 'fluor_color', 'fluor_intensity', 'fancy_color_dominant_color', 'fancy_color_secondary_color', 'fancy_color_overtone', 'fancy_color_intensity']


@app.route("/", methods = ["GET","POST"])
def hello():
    l=[]
    if request.method == "POST":
        for i in features:
            try:
                l.append(float(request.form[i]))
            except ValueError:
                l.append(request.form[i])
        sales_p = m.predict_pipe(l)
        #print(sales_p)



    return render_template('index.html', sale=sales_p)






'''
@app.route("/sub", methods = ['POST'])
def submit():
    if request.method == "POST":
        cut = request.form['cut']
    return render_template('sub.html', v1 = cut)

'''
if __name__ == "__main__":
    app.run(debug=True)