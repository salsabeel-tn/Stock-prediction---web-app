import streamlit as st
from datetime import date

#All required packages are available and imported here.
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["Date"],y=data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=data["Date"],y=data['Close'], name='stock_close'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

st.title("Stock Prediction WebApp")

stocks = ('AAPL',"GOOG","MSFT","GME")

selected_stock = st.selectbox("Select a company stock to predict",stocks)

n_years = st.slider("Years of prediction",1,4)

period=n_years * 365

data_load_state = st.text("Loading data....")
data = load_data(selected_stock)
data_load_state.text("Successfully loaded the data!")

st.subheader('Raw data')
st.write(data.tail())

plot_raw_data()

#todo: Forecasting


