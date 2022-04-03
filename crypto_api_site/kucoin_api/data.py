from turtle import color
import kucoinwallet
import matplotlib.pyplot as plt  
account_balance = kucoinwallet.account_balance
def barchart():
    fig = plt.figure(figsize=(10,5))
    ax = fig.add_axes([0,0,1,1])
    labels = list(account_balance.keys())
    values = list(account_balance.values())
    ax.bar(labels,values,color='green',width=0.1)
    plt.xlabel("currency")
    plt.ylabel("value")
    plt.title("kucoin coins")
    plt.show()
barchart()