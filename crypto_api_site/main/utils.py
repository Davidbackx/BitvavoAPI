import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO.IO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(coin,value):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Percentage of all coins')
    fig, ax1 = plt.subplots()
    ax1.pie(value,coin,autopct='%.2f%%')
    ax1.set_title("totalinvested per currency")
    ax1.legend(value,loc="center left",fontsize=10)
    fig.set_size_inches(10.5, 5.5)
    graph = get_graph()
    return graph

