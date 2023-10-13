from flask import Flask, render_template,request,flash,url_for,redirect

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return "About Food4u!"

@app.route('/contact')
def contact():
    return "Contact Food4u!"

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Replace these values with your desired login credentials
        if username == 'admin' and password == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Invalid credentials. Try again.', 'danger')
            return redirect(url_for('login'))
            
    return render_template('login.html')


# Checkout Feature
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Handle the checkout process: update inventory, process payment, etc.
        # ...
        pass
    return render_template('checkout.html')

@app.route('/place_order')
def placed():
    return render_template('order_placed.html')

if __name__ == '__main__':
    app.run(debug=True)
