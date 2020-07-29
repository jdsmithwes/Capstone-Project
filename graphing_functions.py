import plotly.io as pio
import plotly.express as px

def plotly_line (df,x,y):
    """Function that provides line graphs in Plotly Express"""
    fig = px.line(df,x=x, y=y)
    fig.show()

def plotly_scatter(df,x,y,trendline,color,trendline):
    """Function for creating a scatterplot in Plotly Express"""
    fig = px.scatter(df,x, y=y,color=color,trendline=trendline)
    fig.show()

def Plotly_bar(df,x,y,title,color):
    """Function for creating a plotly express bar chart"""
    fig = px.bar(df, x=x, y=y, title=title,color=color)
    fig.show()