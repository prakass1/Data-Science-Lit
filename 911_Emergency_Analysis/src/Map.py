# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 19:51:26 2019

@author: subash
"""

import plotly.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd

def plotMap(data):
    init_notebook_mode(connected=True)

    scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
             [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

    data_emer = [dict(type='scattergeo',
            colorscale = scl,
            lon = data["lat"],
            lat = data["lng"],
            locations = data["twp"],
            #locationmode = 'USA-states',
            text = data['E-Type'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
            colorbar = {'title':"Emergencies"}
            )]

    layout = dict(title = 'Emergency',
              geo = dict(#scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )

    fig = dict( data=data_emer, layout=layout )
    plot( fig, validate=False)



if __name__ == '__main__':
    plotMap(data)