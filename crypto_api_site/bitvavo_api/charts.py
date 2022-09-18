from cProfile import label
import wallet as wallet
import data_overview as data_overview
import predictions as predictions
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
# from bitvavovariables import bitvavo_api,bitvavo_secret_api
import os

currencys = wallet.total_invested

def draw_pie_chart_of_all_currencys():
    #make 2 pie charts
    fig , ax1 =plt.subplots()
    #assign values and labels for first pie chart
    values = ([item["total"] for item in currencys])
    labels = ([item["symbol"] for item in currencys])
    #make the first pie chart
    ax1.pie(values,labels=labels,autopct='%.2f%%')
    ax1.set_title("totalinvested per currency")
    # ax1.legend(values,loc="center left",fontsize=10)
    #assign the widt,height for the window
    fig.set_size_inches(10.5, 5.5)
    #save the pie chart
    DIR = 'D:\\David\\bitvavoApi\\crypto_api_site\\main\\static\\main\\images\\piechart_coins.png'
    plt.rcParams["savefig.directory"] = os.chdir(os.path.dirname(DIR))
    plt.savefig('piechart_coins.png')

# def val_and_current_val_per_coin():
#     coin = ([key for key,val in currencys.items()])
#     value = ([round(val,3) for key,val in currencys.items()])
#     currentval = ([val for key,val in currencys_with_current_value.items()])
#     color = [] 
#     for i in range(len(coin)):
#         if value[i] > currentval[i]:
#             color.append("RED")
#         elif value[i] == currentval[i]:
#             color.append = "ORANGE"
#         else:
#             color.append("GREEN")
#     X = np.arange(len(coin))
#     width = 0.35
#     fig,ax = plt.subplots()
#     rects1 = ax.bar(X-width/2,value,width)
#     rects2 = ax.bar(X+width/2,currentval,width,color=color)
#     ax.set_xlabel("coins")
#     ax.set_ylabel("value")
#     ax.set_title("total invested and currentval per coin")
#     ax.set_xticks(X,coin)
#     ax.legend()
#     ax.bar_label(rects1,padding=0.35)
#     ax.bar_label(rects2,padding=0.35)
#     fig.tight_layout()
#     plt.show()
# draw_pie_chart_of_all_currencys()
# #val_and_current_val_per_coin()

def line_chart_currency(currency,days):
    coin_info = data_overview.last_days_coin(currency,days)
    price = ([item["last"] for item in coin_info])
    timestamps = ([datetime.fromtimestamp(item["timestamp"]/1000).date() for item in coin_info])
    plt.figure(figsize=(10,6))
    plt.plot(timestamps,price,color='green',marker='o')
    plt.title(f'{currency} from the last {days} days')
    DIR = 'D:\\David\\bitvavoApi\\crypto_api_site\\main\\static\\main\\images\\linechart_coins.png'
    plt.rcParams["savefig.directory"] = os.chdir(os.path.dirname(DIR))
    plt.savefig('linechart_coins.png')
currencies = wallet.total_invested
current_val = wallet.current_value
def val_and_current_val_per_coin():
    coin = ([item["symbol"] for item in currencies])
    value = ([item["total"] for item in currencies])
    currentval = ([item["total_value"] for item in current_val])
    color = [] 
    for i in range(len(coin)):
        if value[i] > currentval[i]:
            color.append("RED")
        elif value[i] == currentval[i]:
            color.append = "ORANGE"
        else:
            color.append("GREEN")
    X = np.arange(len(coin))
    width = 0.35
    fig,ax = plt.subplots()
    rects1 = ax.bar(X-width/2,value,width)
    rects2 = ax.bar(X+width/2,currentval,width,color=color)
    ax.set_xlabel("coins")
    ax.set_ylabel("value")
    ax.set_title("total invested and currentval per coin")
    ax.set_xticks(X,(coin))
    ax.legend()
    ax.bar_label(rects1,padding=width)
    ax.bar_label(rects2,padding=width)
    fig.set_size_inches(10,5)
    #D:\\David\\bitvavoApi\\crypto_api_site\\main\\static\\main\\images\\barchart_coins.png
    #D:\\David\\Programeer projecten\\BitvavoAPI\\crypto_api_site\\main\\static\\main\\images\\barchart_coins.png
    DIR = 'D:\\David\\bitvavoApi\\crypto_api_site\\main\\static\\main\\images\\barchart_coins.png'
    plt.rcParams["savefig.directory"] = os.chdir(os.path.dirname(DIR))
    plt.savefig('barchart_coins.png')

def macd(currency):
    ema_12 = predictions.ema2(currency,12)
    ema_12_val = ([ema_12[idx]["ema"] for idx,_ in enumerate(ema_12)])
    ema_12_time =([ema_12[idx]["time"] for idx,_ in enumerate(ema_12)])
    ema_26 = predictions.ema2(currency,26)
    ema_26_val = ([ema_26[idx]["ema"] for idx,_ in enumerate(ema_26)])
    ema_26_time = ([ema_26[idx]["time"] for idx,_ in enumerate(ema_26)])
    print(ema_26_val)
    signal_line = predictions.ema2(currency,9)
    signal_val = ([signal_line[idx]["ema"] for idx,_ in enumerate(signal_line)])
    print(signal_val)
    time = ([signal_line[idx]["time"] for idx,_ in enumerate(signal_line)])
    print(time)
    plt.plot(ema_12_time,ema_12_val,label="EMA-12")
    plt.plot(ema_26_time,ema_26_val,label="EMA-26")
    plt.plot(time,signal_val,label="signal line")
    plt.show()
macd("ADA-EUR")