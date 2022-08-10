
import wallet
import matplotlib.pyplot as plt
import numpy as np
from bitvavovariables import bitvavo_api,bitvavo_secret_api

# currencys = bitvavowallet.currencys
# currencys_with_current_value = bitvavowallet.currentvalues
# def draw_pie_chart_of_all_currencys():
#     #make 2 pie charts
#     fig , ax1 =plt.subplots()
#     #assign values and labels for first pie chart
#     values = ([val for key,val in currencys.items()])
#     labels = ([key for key,val in currencys.items()])
#     #make the first pie chart
#     ax1.pie(values,labels=labels,autopct='%.2f%%')
#     ax1.set_title("totalinvested per currency")
#     ax1.legend(values,loc="center left",fontsize=10)
#     #assign the widt,height for the window
#     fig.set_size_inches(10.5, 5.5)
#     #display the pie chart
#     plt.show()
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

# def line_chart_currency(currency):
#     purchases = bitvavowallet.get_orders_currency(bitvavo_api,bitvavo_secret_api,currency)
#     price = []
#     amount = []
#     timestamp = []
#     for order in purchases:
#         price.append(order["price"])
#         amount.append(order["amount"])
#         timestamp.append(order["timestamp"])
#     timestamp.sort()
#     x = np.linspace(timestamp[0],timestamp[-1],50)
#     plt.plot(x,price)

#     plt.show()
currencies = wallet.total_invested
current_val = wallet.current_value
# print(current_val)
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
    ax.set_xticks(X,coin)
    ax.legend()
    ax.bar_label(rects1,padding=0.35)
    ax.bar_label(rects2,padding=0.35)
    fig.tight_layout()
    plt.show()
val_and_current_val_per_coin()