import dash
import dash_core_components as dcc
import dash_html_components as html
from sodapy import Socrata
import pandas as pd
import plotly.graph_objs as go

'''ASSIGNMENT PROMPT
1. What proportion of trees are in good, fair or poor condition according to
 the 'health' variable?
2. Are stewards (steward variable) having an impact on the health of trees?'''
#DATA
trees_api_url = 'https://data.cityofnewyork.us/resource/5rq2-4hqu.json'
steward_tree_api_URL = 'https://data.cityofnewyork.us/resource/5rq2-4hqu.json?steward=None'
Fair_health_tree_api_URL = 'https://data.cityofnewyork.us/resource/5rq2-4hqu.json?health=Fair&$limit=1000000'
Fair_Health = pd.read_json(Fair_health_tree_api_URL)
None_Fair = len(Fair_Health[Fair_Health['steward']=='None'])
_1or2_Fair = len(Fair_Health[Fair_Health['steward']=='1or2'])
_3or4_Fair = len(Fair_Health[Fair_Health['steward']=='3or4'])
_4orMore_Fair = len(Fair_Health[Fair_Health['steward']=='4orMore'])
fair = len(Fair_Health)
good_health_tree_api_URL = 'https://data.cityofnewyork.us/resource/5rq2-4hqu.json?health=Good&$limit=1000000'
good_Health = pd.read_json(good_health_tree_api_URL)
None_good = len(good_Health[good_Health['steward']=='None'])
_1or2_good = len(good_Health[good_Health['steward']=='1or2'])
_3or4_good = len(good_Health[good_Health['steward']=='3or4'])
_4orMore_good = len(good_Health[good_Health['steward']=='4orMore'])
good = len(good_Health)
poor_health_tree_api_URL = 'https://data.cityofnewyork.us/resource/5rq2-4hqu.json?health=Poor&$limit=1000000'
poor_Health = pd.read_json(poor_health_tree_api_URL)
None_poor = len(poor_Health[poor_Health['steward']=='None'])
_1or2_poor = len(poor_Health[poor_Health['steward']=='1or2'])
_3or4_poor = len(poor_Health[poor_Health['steward']=='3or4'])
_4orMore_poor = len(poor_Health[poor_Health['steward']=='4orMore'])
poor = len(poor_Health)
health_tree_api_URL = 'https://data.cityofnewyork.us/resource/5rq2-4hqu.json?$limit=1000000'
Health = pd.read_json(health_tree_api_URL)
print(list(Health))
Health['latitude'] = Health['latitude'].astype(float)
Health['longitude'] = Health['longitude'].astype(float)

#APP
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#MAP

# REMOVED, WASN'T WORKING -- INTENDED TO BE MAP CODED BY HEALTH
'''fig2 = go.Figure(data=go.Scattergeo(
        lon = Health['longitude'],
        lat = Health['latitude'],
        text = Health['spc_common'],
        mode = 'markers',
        marker_color = Health['health']
        ))

fig2.update_layout(
        title = 'Tree Health Map',
        geo_scope='usa',
    )'''



# HEALTH PROPORTION
dates = ['Tree Health']
HealthTrace = go.Bar(
    x=dates, y=[poor],
    name='poor'
)
HealthTrace1 = go.Bar(
    x=dates, y=[fair],
    name='fair'
)
HealthTrace2 = go.Bar(
    x=dates, y=[good],
    name='good'
)

data1 = [HealthTrace,HealthTrace1,HealthTrace2]
layout = go.Layout(
        title = 'Tree Health Proportional',
    barmode='stack',
    xaxis=dict(tickvals=['Tree Health'])
)

fig1 = go.Figure(data=data1, layout=layout)


dates = ['None', '1 or 2', '3 or 4','4 or more']
trace1 = go.Bar(
    x=dates, y=[None_poor, _1or2_poor, _3or4_poor,_4orMore_poor],
    name='poor'
)
trace2 = go.Bar(
    x=dates, y=[None_Fair, _1or2_Fair, _3or4_Fair,_4orMore_Fair],
    name='fair'
)
trace3 = go.Bar(
    x=dates, y=[None_good, _1or2_good, _3or4_good,_4orMore_good],
    name='good'
)

data = [trace1, trace2, trace3]
layout = go.Layout(
        title = 'Tree Health Proportion by Steward',
    barmode='stack',
    xaxis=dict(tickvals=['None', '1 or 2', '3 or 4','4 or more'])
)

fig = go.Figure(data=data, layout=layout)


df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')



app.layout = html.Div(children=[
    html.H1(children='Tree Health'),

    html.Div(children='''
        A look at the count of trees in poor, fair and good health
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1], 'y': [poor], 'type': 'bar', 'name': 'Poor'},
                {'x': [1], 'y': [good], 'type': 'bar', 'name': 'Fair'},
                {'x': [1], 'y': [fair], 'type': 'bar', 'name': 'Good'}
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                 'xaxis':{
                    'title':'Count of Trees by Health Evaluation'
                },
                'yaxis':{
                     'title':'Count of Trees'
                }
            }
        }
    ),
dcc.Graph(figure=fig1),

html.H1(children='Impact of Steward on Tree Health'),

    html.Div(children='''
        Comparison of tree health based on the number of stewards reported
    '''),
dcc.Graph(figure=fig)

])



if __name__ == '__main__':
    app.run_server(debug=False)

