from flask import Flask, render_template
import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd

from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.trading.requests import GetPortfolioHistoryRequest

import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

API_KEY = os.getenv('ALPACA_API_KEY')
SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')

# Initialize Alpaca clients
trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
data_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

def get_portfolio_data():
    """Fetch portfolio data from Alpaca"""
    try:
        # Get portfolio history
        portfolio_request = GetPortfolioHistoryRequest(
            period="1M",
            timeframe="1D",
            extended_hours=False
        )
        
        portfolio_history = trading_client.get_portfolio_history(portfolio_request)
        
        # Convert to DataFrame
        df = pd.DataFrame({
            'timestamp': portfolio_history.timestamp,
            'equity': portfolio_history.equity,
            'profit_loss': portfolio_history.profit_loss,
            'profit_loss_pct': portfolio_history.profit_loss_pct
        })
        
        # Convert timestamp to datetime
        df['date'] = pd.to_datetime(df['timestamp'], unit='s')
        df.set_index('date', inplace=True)
        
        return df
    except Exception as e:
        print(f"Error fetching portfolio data: {e}")
        return None

def get_current_positions():
    """Fetch current positions from Alpaca"""
    try:
        positions = trading_client.get_all_positions()
        
        positions_data = []
        for position in positions:
            positions_data.append({
                'symbol': position.symbol,
                'price': round(float(position.current_price), 2),
                'change': f"{float(position.unrealized_plpc) * 100:.2f}%",
                'currency': 'USD',
                'shares': int(float(position.qty))
            })
        
        return positions_data
    except Exception as e:
        print(f"Error fetching positions: {e}")
        return []

def generate_portfolio_graph():
    """Generate portfolio graph HTML"""
    df = get_portfolio_data()
    
    if df is not None and not df.empty:
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['equity'],
            mode='lines',
            name='Portfolio Value',
            line=dict(color='#32746d', width=3),
            hovertemplate='<b>Date:</b> %{x}<br><b>Value:</b> $%{y:,.2f}<extra></extra>'
        ))
        
        fig.update_layout(
            title='Portfolio Performance Over Time',
            title_font_size=18,
            xaxis_title='Date',
            yaxis_title='Portfolio Value ($)',
            template='plotly_white',
            hovermode='x unified',
            margin=dict(l=0, r=0, t=40, b=0),
            autosize=True
        )
        
        fig.update_yaxes(tickformat='$,.0f')
        return pyo.plot(fig, output_type='div', include_plotlyjs=True, config={'responsive': True})
    else:
        return "<div style='text-align: center; padding: 50px;'>No portfolio data available</div>"

@app.route('/')
def home():
    graph_html = generate_portfolio_graph()
    real_positions = get_current_positions()
    if real_positions:
        stocks_to_display = real_positions
        return render_template("home.html", 
                            name="Mateo", 
                            stocks=stocks_to_display, 
                            graph_html=graph_html)
    else:
        return render_template("home.html", 
                            name="Mateo",
                            graph_html=graph_html)

@app.route('/portfolio')
def portfolio():
    graph_html = generate_portfolio_graph()
    real_positions = get_current_positions()
    if real_positions:
        return render_template("portfolio.html", 
                         name="Mateo", 
                         stocks=real_positions,
                         graph_html=graph_html)
    else:
        return render_template("portfolio.html", 
                         name="Mateo", 
                         graph_html=graph_html)
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")