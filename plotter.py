from flask import Flask, render_template,request
import matplotlib.pyplot as plt
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def plot():
    if (request.method == 'POST'):
        '''Add entry to the database'''
        Xpoints = request.form.get('Xpoints')
        Ypoints = request.form.get('Ypoints')
        kind = request.form.get('kind')
        Xpoints=list(map(int,Xpoints.split(',')))
        Ypoints=list(map(int,Ypoints.split(',')))
        if kind=="a":
            plt.plot(Xpoints,Ypoints)
        elif kind=="b":
            plt.bar(Xpoints,Ypoints)
        elif kind=="c":
            plt.pie(Xpoints,labels=Ypoints)
        elif kind=="d":
            plt.hist(Xpoints,bins=3,label=Ypoints)
        elif kind=="e":
            plt.scatter(Xpoints,Ypoints)
        plt.show()
    return render_template('index.html')

app.run(debug=True)
