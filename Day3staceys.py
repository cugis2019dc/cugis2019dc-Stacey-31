# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:13:57 2019

@author: STEM
"""

def cadbury(a,b,c):
    print("there is",a,"dark",b,"white and",c,"milk chocolates")

cadbury(5,8,6)


cadbury1="milk choclate"
cadbury2="dark chocolate"
cadbury3="white chocolate"
cadburymilk=6
cadburydark=5
cadburywhite=8


print(cadbury1)
print(cadbury2)
print(cadbury3)
print(cadburymilk)
print(cadburydark)
print(cadburywhite)

choc1={"dark":5}
choc2={"milk":8}
choc3={"white":3}
print(choc1,choc2,choc3)

chocolatebox={"dark":5,"milk":6,"white":3}
chocolatebox


Steve={"M":32}
Lia={"F":28}
Vin={"M":45}
Katie={"F":38}

Cities={"NY":"New York", "DC":"Washington DC", }
Age={"Steve":32,"Lia":28,"Vin":45,"Katie":38}
gender={"Steve":"M","Lia":"F","Vin":"M","Katie":"F"}

#List
List=[['steve',32,'M'],['Lia',28,'F'],['Vin',45,'M'],['Katie',38,'F']]
List

student=[Age,gender]

import pandas
dir(pandas)

studentdf=pandas.DataFrame(List,columns=("name","age","gender"))
studentdf

studentdf["name"]
studentdf["age"]
studentdf["gender"]

List2=[["milk",5],["dark",8],["white",3]]
List2
import pandas
dir(pandas)

List2df=pandas.DataFrame(List2,columns=("chocotype","quantity"))

List2df=pandas.DataFrame(List2df,index("1","2","3"))

import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go 

studentbar= go.Bar(x=studentdf["name"],y=studentdf["age"])
plot([studentbar])

import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go 

studentdar= go.Bar(x=List2df["chocotype"],y=List2df["quantity"])
plot([studentdar])

titles = go.Layout(title = "number of chocolate by type")
studentdar= go.Bar(x=List2df["chocotype"],y=List2df["quantity"])
fig = go.Figure(data=[studentdar], layout=titles)
plot(fig)
