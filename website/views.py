from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import json
import io, urllib, base64
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from website.models import DBModel

df=pd.read_csv('D:\GDG Jalandhar\household\data.csv')

df.dropna
df["street"].drop
df["statezip"].drop
df["date"].drop
df=df.drop(['street'],axis=1)
df=df.drop(["city","statezip","country"],axis=1)
yr_renovated_ago=(2022-df["yr_renovated"])
x=df.iloc[:,1:]
y=df['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)
model=LinearRegression()
model.fit(x_train,y_train)

def index(request):
    return render(request, 'website/index.html')

def Prediction(request):
    # print("Data: ",df.head())
    return render(request, 'website/house_price_predict.html')

def ShowAllDataView(request):
    return render(request, 'website/show_all_data.html')

def show_plot(request):
    if request.method == "POST":
        date = request.POST.get('date')
        price = request.POST.get('price')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        sqft_living = request.POST.get('sqft_living')
        sqft_lot = request.POST.get('sqft_lot')
        floors = request.POST.get('floors')
        waterfront = request.POST.get('waterfront')
        view = request.POST.get('view')
        condition = request.POST.get('condition')
        sqft_above = request.POST.get('sqft_above')
        sqft_basement = request.POST.get('sqft_basement')
        yr_built = request.POST.get('yr_built')
        yr_renovated = request.POST.get('yr_renovated')
        # street = request.POST.get('street')

        x=df.iloc[:,1:]
        y=df['price']

        # y_p = [price, bedrooms, bathrooms,sqft_living, sqft_lot, floors, waterfront, view, condition, sqft_above, sqft_basement, yr_built, yr_renovated]
        y_p = [price]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)
        # print(x_train, x_test, y_train, y_test)

        d1 = []
        d2 = []
        d3 = []
        d4 = []
        d5 = []
        d6 = []
        d7 = []
        d8 = []
        d9 = []
        d10 = []
        d11 = []
        d12 = []
        d13 = []

        import random
        for i in range(1):
            x = random.randint(123450, 9085000)
            d1.append(x)
        for i in range(1):
            x = random.randint(1, 2)
            d2.append(x)
        for i in range(1):
            x = random.randint(1, 2)
            d3.append(x)
        for i in range(1):
            x = random.randint(1100, 9999)
            d4.append(x)
        for i in range(1):
            x = random.randint(999,111853)
            d5.append(x)
        for i in range(1):
            x = random.randint(1, 5)
            d6.append(x)
        for i in range(1):
            x = random.randint(0, 0)
            d7.append(x)
        for i in range(1):
            x = random.randint(1, 5)
            d8.append(x)
        for i in range(1):
            x = random.randint(1, 6)
            d9.append(x)
        for i in range(1):
            x = random.randint(655, 1510)
            d10.append(x)
        for i in range(1):
            x = random.randint(0, 1461)
            d11.append(x)
        for i in range(1):
            x = random.randint(1909, 2016)
            d12.append(x)
        for i in range(1):
            x = random.randint(1970, 2016)
            d13.append(x)

        context = {'data': x_train, 'd1': d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5, 'd6':d6, 'd7':d7, 'd8':d8, 'd9':d9, 'd10':d10, 'd11':d11, 'd12':d12, 'd13':d13}
        return render(request, 'website/show_plot.html', context)


    return render(request, 'website/show_plot.html')


