from flask import Flask, render_template

app = Flask(__name__)

stocks = [
    {
        "symbol": "AAPL",
        "price": 180.12,
        "change": "+1.25%",
        "currency": "USD",
        "shares": 10,
    },
    {
        "symbol": "GOOGL",
        "price": 2850.5,
        "change": "-0.75%",
        "currency": "USD",
        "shares": 5,
    },
    {
        "symbol": "TSLA",
        "price": 720.3,
        "change": "+2.10%",
        "currency": "USD",
        "shares": 8,
    },
    {
        "symbol": "TSLA",
        "price": 720.3,
        "change": "+2.10%",
        "currency": "USD",
        "shares": 8,
    },
    {
        "symbol": "TSLA",
        "price": 720.3,
        "change": "+2.10%",
        "currency": "USD",
        "shares": 8,
    },
    {
        "symbol": "TSLA",
        "price": 720.3,
        "change": "+2.10%",
        "currency": "USD",
        "shares": 8,
    },
]
transactions = [
    { "description": "Spenditure at Walmart", "amount": 50 },
    { "description": "Coffee at Starbucks", "amount": 5 },
    { "description": "Groceries at Target", "amount": 30 },
    { "description": "Dinner at Olive Garden", "amount": 40 },
    { "description": "Gas Station", "amount": 60 },
    { "description": "Costco", "amount": 103 },
    { "description": "Costco", "amount": 103 },
]

@app.route('/')
def home():
    return render_template("home.html", name="Mateo", stocks=stocks, transactions = transactions)

@app.route('/portfolio')
def portfolio():
    portfolio = [
    {
        "symbol": "AAPL",
        "price": 180.12,
        "change": "+1.25%",
        "currency": "USD",
        "shares": 10,
    },
    {
        "symbol": "GOOGL",
        "price": 2850.5,
        "change": "-0.75%",
        "currency": "USD",
        "shares": 5,
    },
    {
        "symbol": "TSLA",
        "price": 720.3,
        "change": "+2.10%",
        "currency": "USD",
        "shares": 8,
    },
    {
        "symbol": "TSLA",
        "price": 720.3,
        "change": "+2.10%",
        "currency": "USD",
        "shares": 8,
    },
    {
        "symbol": "TSLA",
        "price": 720.3,
        "change": "+2.10%",
        "currency": "USD",
        "shares": 8,
    },
    {
        "symbol": "TSLA",
        "price": 720.3,
        "change": "+2.10%",
        "currency": "USD",
        "shares": 8,
    },
]

    return render_template("portfolio.html", name="Mateo", stocks=stocks)

if __name__ == 'main':
        app.run(debug=True, host="0.0.0.0")