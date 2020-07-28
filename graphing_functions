import plotly.io as pio

def plotly_groupby(x_data,y_data,graph_type,transformation_type):
    """Function to plot graphs in plotly that use groupby in pandas"""
    data = [dict(
    type = graph_type,
    x = x_data,
    y = y_data,
    mode = 'markers',
    transforms = [dict(
    type = transformation_type,
    groups = x,
    styles = [
        dict(target = 'Moe', value = dict(marker = dict(color = 'blue'))),
        dict(target = 'Larry', value = dict(marker = dict(color = 'red'))),
        dict(target = 'Curly', value = dict(marker = dict(color = 'black')))
    ]
  )]
)]

fig_dict = dict(data=data)
pio.show(fig_dict, validate=False)