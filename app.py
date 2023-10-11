from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_name = request.form.get('product_name')
    price = float(request.form.get('price'))
    quantity = int(request.form.get('quantity'))

    if 'cart' not in session:
        session['cart'] = []
        
    cart_item = {
        'product_name': product_name,
        'price': price,
        'quantity': quantity,
    }

    session['cart'].append(cart_item)
    return redirect(url_for('index'))    

@app.route('/about')
def about():
    return "About Food4u!"

@app.route('/contact')
def contact():
    return "Contact Food4u!"


if __name__ == '__main__':
    app.run(debug=True)
