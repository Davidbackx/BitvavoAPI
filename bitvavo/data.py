import bitvavo.bitvavowallet as bitvavowallet
import matplotlib.pyplot as plt

currencys = bitvavowallet.currencys
currencys_with_current_value = bitvavowallet.currentvalues
def draw_pie_chart_of_all_currencys():
    #make 2 pie charts
    fig , (ax1,ax2) =plt.subplots(1,2)
    #assign values and labels for first pie chart
    values = ([val for key,val in currencys.items()])
    labels = ([key for key,val in currencys.items()])
    #make the first pie chart
    ax1.pie(values,labels=labels,autopct='%.2f%%')
    ax1.set_title("totalinvested per currency")
    ax1.legend(values,loc="center left",fontsize=10)
    #assign the widt,height for the window
    fig.set_size_inches(10.5, 5.5)
    #assign the values for the second pie chart, the labels for the second pie chart are the same as the first
    currentvalues = ([round(val,2) for key,val in currencys_with_current_value.items()])
    ax2.pie(currentvalues,labels=labels,autopct='%.2f%%')
    ax2.legend(currentvalues,loc="center right",fontsize=10)
    ax2.set_title("Current values of all account currencys")
    #display the pie chart
    plt.show()
draw_pie_chart_of_all_currencys()   