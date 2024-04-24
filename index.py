from flask import Flask, render_template, request
from simulation import run_simulation, plot_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        
        data = run_simulation()
        plot_data(data)
        message = "Simulation complete. Check the plot."
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
