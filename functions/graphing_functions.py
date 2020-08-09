import plotly.io as pio
import plotly.express as px

def plotly_line (df,x,y):
    """Function that provides line graphs in Plotly Express"""
    fig = px.line(df,x=x, y=y)
    fig.show()

def plotly_scatter(df,x,y,trendline,color):
    """Function for creating a scatterplot in Plotly Express"""
    fig = px.scatter(df,x, y=y,color=color,trendline=trendline)
    fig.show()

def Plotly_bar(df,x,y,title,color):
    """Function for creating a plotly express bar chart"""
    fig = px.bar(df, x=x, y=y, title=title,color=color)
    fig.show()


def ROC_Curve (Model, X,y):
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.15)
    model = Model
    visualizer = ROCAUC(Model)

    visualizer.fit(X_train, y_train)        # Fit the training data to the visualizer
    visualizer.score(X_test, y_test)        # Evaluate the model on the test data
    visualizer.show()