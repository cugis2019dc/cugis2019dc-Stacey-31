# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:06:25 2019

@author: STEM
"""

import pandas as pd
dir(pandas)
import plotly
from plotly.offline import plot
import plotly.graph_objs as go

wodf = pd.read_excel("GISdata.xlsx",sheet_name = "womenOccupation")
wodf

wodf = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")

womenoccupation = go.Bar(x=wodf["occupation"], y=wodf["women"], marker = {"color":wodf["women"], "colorscale" : "RdBu"})               

plot([womenoccupation])

titles = go.Layout(title = "Percentage of Women Employed by Occupation",
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Occupation",
                        )
                    ),

                    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",
                            )
                      )
                    )

fig = go.Figure(data=[womenoccupation], layout=titles)
plot(fig)
