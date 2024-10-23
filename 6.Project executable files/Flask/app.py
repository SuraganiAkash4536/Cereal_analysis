from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open(r'C:\Users\PRAKASH.S\Desktop\html.cerals\cerealanalysis (5).pkl', 'rb'))

@app.route('/')
def helloworld():
    return render_template("base.html")

@app.route('/assesment')
def prediction():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def admin():
    a = request.form["mfr"]
    '''if a == 'a':
        a1, a2, a3, a4, a5, a6, a7 = 1, 0, 0, 0, 0, 0, 0
    elif a == 'g':
        a1, a2, a3, a4, a5, a6, a7 = 0, 1, 0, 0, 0, 0, 0
    elif a == 'k':
        a1, a2, a3, a4, a5, a6, a7 = 0, 0, 1, 0, 0, 0, 0
    elif a == 'n':
        a1, a2, a3, a4, a5, a6, a7 = 0, 0, 0, 1, 0, 0, 0    
    elif a == 'p':
        a1, a2, a3, a4, a5, a6, a7 = 0, 0, 0, 0, 1, 0, 0    
    elif a == 'q':
        a1, a2, a3, a4, a5, a6, a7 = 0, 0, 0, 0, 0, 1, 0    
    elif a == 'r':
        a1, a2, a3, a4, a5, a6, a7 = 0, 0, 0, 0, 0, 0, 1    
'''
    b = request.form["type"]
    '''b = 0 if b == 'c' else 1'''

    c = request.form["Calories"]
    d = request.form["Protien"]
    e = request.form["Fat"]
    f = request.form["Sodium"]
    g = request.form["Fiber"]
    h = request.form["Carbo"]
    i = request.form["Sugars"]
    j = request.form["Potass"]
    k = request.form["Vitamins"]
    l = request.form["Shelf"]
    m = request.form["Weight"]
    n = request.form["Cups"]

    t = [[
        int(a),
        int(b), int(c), int(d), int(e), int(f), float(g),float(h),float(i),float(j),float(k),float(l),float(m),float(n)
    ]]
    
    # Debugging output
    print(t)
    print(len(t), len(t[0]))

    y = model.predict(t)
    return render_template("prediction.html", z=y[0])

if __name__ == '__main__':
    app.run(debug=True)