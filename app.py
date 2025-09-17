
from flask import Flask  ,render_template
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np



df1 = pd.read_csv("D:\\Project\\static\\q-commerce.csv")
df2 = pd.read_csv("D:\\Project\\static\\offline_retail.csv")
year = 2022
for x in range(3):
    fig = go.Figure(data=[
        go.Scatter(
            x=df1['Month'],
            y=df1[f'{year}'],
            mode='lines',
            name='Q-Commerce',
            line=dict(color='red', width=3) 
        )
    ])

    fig.add_trace(go.Scatter(
        x=df2['Month'],
        y=df2[f'{year}'],
        mode='lines',
        name='Offline Retail',
        line=dict(color='blue', width=3)
    ))

    fig.update_layout(
        xaxis_type='category',
        title=' ',
        xaxis_title='Months',
        yaxis_title='Total Sales (in cr)'
    )

    fig.write_html(f"D:\\Project\\static\\graph_{year}.html")
    year = year +1







q_pred = []
off_pred = []


for x in range(12):
    X = np.array([2022, 2023, 2024]).reshape(-1, 1)
    y1 =[int(df1["2022"][x]) , int(df1["2023"][x]) ,int(df1["2024"][x])]
    y2 = [int(df2["2022"][x]) , int(df2["2023"][x]) ,int(df2["2024"][x])]

    model1 = LinearRegression()
    model1.fit(X, y1)

    model2 = LinearRegression()
    model2.fit(X, y2)

    qcom_prediction = int(round(model1.predict([[2025]])[0]))
    off_prediction = int(round(model2.predict([[2025]])[0]))
    q_pred.append(qcom_prediction)
    off_pred.append(off_prediction)


fig = go.Figure(data=[
    go.Scatter(
        x=df1['Month'],
        y=q_pred,
        mode='lines',
        name='Q-Commerce',
        line=dict(color='red', width=3) 
    )
])

fig.add_trace(go.Scatter(
    x=df2['Month'],
    y=off_pred,
    mode='lines',
    name='Offline Retail',
    line=dict(color='blue', width=3)
))

fig.update_layout(
    xaxis_type='category',
    title=' ',
    xaxis_title='Months',
    yaxis_title='Total Sales (in cr)'
)

fig.write_html(f"D:\\Project\\static\\graph_2025.html")



app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/2022")
def page_2022():
    return render_template("2022.html")

@app.route("/2023")
def page_2023():
    return render_template("2023.html")

@app.route("/2024")
def page_2024():
    return render_template("2024.html")

@app.route("/2025")
def page_2025():
    return render_template("2025.html")


if __name__ == "__main__":
    app.run(debug=True)
