import plotly.io as pio

def plotly_line (df,x,y):
    """Function that provides line graphs in Plotly Express"""
    fig = px.line(df,x=x, y=y)
    fig.show()