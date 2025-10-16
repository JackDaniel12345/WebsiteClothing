from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated in-memory database (for demo purposes)
laundry_items = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = {
            'name': request.form['name'],
            'clothing_type': request.form['clothing_type'],
            'quantity': request.form['quantity'],
            'status': 'Pending Pickup'
        }
        laundry_items.append(item)
        return redirect(url_for('index'))

    return render_template('index.html', items=laundry_items)

if __name__ == '__main__':
    app.run(debug=True)
