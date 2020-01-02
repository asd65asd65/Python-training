# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data1 = pd.read_excel("歷年來台旅客統計2 UTF8.xlsx")

df = pd.DataFrame({"年別"       :data1["年別"],
                   "總計旅客人數":(data1["外籍旅客人數"]+data1["華僑旅客人數"])/1000,
                   "總成長率":data1["總計成長率"],
                   "外籍旅客人數":data1["外籍旅客人數"],
                   "外籍旅客成長率":data1["外籍旅客成長率"],
                   "外籍旅客百分比":data1["外籍旅客占總計百分比"],
                   "華僑旅客人數":data1["華僑旅客人數"],
                   "華僑旅客成長率":data1["華僑旅客成長率"],
                   "華僑旅客百分比":data1["華僑旅客占總計百分比"]})

FV="F Visitors"
OCV="OC Visitors"

plt.scatter(df["年別"], df["外籍旅客人數"], 10, color="blue", label=FV)
plt.scatter(df["年別"], df["華僑旅客人數"], 10, color="red", label=OCV)
plt.xlabel("Year")
plt.ylabel("Visitors")
plt.title("Every Year Visitors")
plt.legend()
plt.show()

plt.plot(df["年別"], df["外籍旅客百分比"], color="blue", label=FV)
plt.plot(df["年別"], df["華僑旅客百分比"], color="red", label=OCV)
plt.xlabel("Year")
plt.ylabel("Visitors ( % )")
plt.title("Year / Visitors ( % )")
plt.legend()
plt.show()

plt.subplot(3, 1, 1)
plt.bar(df["年別"], df["總成長率"])
plt.xlabel("Year")
plt.ylabel("Growth")
plt.title("Every Year Totel Visitors Growth")
plt.show()

plt.subplot(3, 1, 2)
plt.bar(df["年別"], df["外籍旅客成長率"], color="blue")
plt.xlabel("Year")
plt.ylabel("Growth")
plt.title("Every Year F Visitors Growth")
plt.show()

plt.subplot(3, 1, 3)
plt.bar(df["年別"], df["華僑旅客成長率"], color="red")
plt.xlabel("Year")
plt.ylabel("Growth")
plt.title("Every Year OC Visitors Growth")
plt.show()

t1 = np.array(data1["年別"])
t2 = np.array(df["總計旅客人數"])
x = pd.DataFrame(t1, columns=["Year"])
t = pd.DataFrame(t2, columns=["Visitors"])
y = t["Visitors"]
lm = LinearRegression()
lm.fit(x, y)
new_year = pd.DataFrame(np.array([2019,2020]))
perdicted_visitors = lm.predict(new_year)
plt.scatter(t1, t2, 10, label="Total Visitors")
regression_visitors = lm.predict(x)
plt.plot(t1, regression_visitors, label="Linear Regression")
plt.xlabel("Year")
plt.ylabel("Visitors")
plt.title("Every Year TotalVisitors")
plt.legend()
plt.show()
print("迴歸係數:", lm.coef_, "截距:", lm.intercept_, "\n")

t1 = np.array(data1["年別"])
t2 = np.array(df["外籍旅客人數"])
x = pd.DataFrame(t1, columns=["Year"])
t = pd.DataFrame(t2, columns=["Visitors"])
y = t["Visitors"]
lm = LinearRegression()
lm.fit(x, y)
new_year = pd.DataFrame(np.array([2019,2020]))
perdicted_visitors = lm.predict(new_year)
plt.scatter(t1, t2, 10, color="blue", label=FV)
regression_visitors = lm.predict(x)
plt.plot(t1, regression_visitors, label="Linear Regression")
plt.scatter(new_year, perdicted_visitors)
plt.xlabel("Year")
plt.ylabel("Visitors")
plt.title("Every Year F Visitors")
plt.legend()
plt.show()
print("迴歸係數:", lm.coef_, "截距:", lm.intercept_, "\n")
print("預測" + str(2019) + "年 外籍旅客人數為:" + str(int(perdicted_visitors[0])) + "人\n")
print("預測" + str(2020) + "年 外籍旅客人數為:" + str(int(perdicted_visitors[1])) + "人\n")

t1 = np.array(data1["年別"])
t2 = np.array(df["華僑旅客人數"])
x = pd.DataFrame(t1, columns=["Year"])
t = pd.DataFrame(t2, columns=["Visitors"])
y = t["Visitors"]
lm = LinearRegression()
lm.fit(x, y)
new_year = pd.DataFrame(np.array([2019,2020]))
perdicted_visitors = lm.predict(new_year)
plt.scatter(t1, t2, 10, color="red", label=OCV)
regression_visitors = lm.predict(x)
plt.plot(t1, regression_visitors, label="Linear Regression")
plt.scatter(new_year, perdicted_visitors)
plt.xlabel("Year")
plt.ylabel("Visitors")
plt.title("Every Year OC Visitors")
plt.legend()
plt.show()
print("迴歸係數:", lm.coef_, "截距:", lm.intercept_, "\n")
print("預測" + str(2019) + "年 華僑旅客人數為:" + str(int(perdicted_visitors[0])) + "人\n")
print("預測" + str(2020) + "年 華僑旅客人數為:" + str(int(perdicted_visitors[1])) + "人\n")