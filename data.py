import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
import random

df=pd.read_csv("data.csv")
data=df["reading_time"].tolist()

#fig = ff.create_distplot([data],["Reading Time"], show_hist=False)
#fig.show()

mean=statistics.mean(data)
sd=statistics.stdev(data)
print("The mean of entire dataset : ",mean )
print("The standard deviation of entire dataset : ", sd)

def random_set_of_data():
    dataset=[]
    for i in range(0,100):
        rand_index=random.randint(0,len(data)-1)
        value=data[rand_index]
        dataset.append(value)
    
    mean=statistics.mean(dataset)
    return mean

def mean_graph(meanList):
    mean = statistics.mean(meanList)
    fig=ff.create_distplot([meanList],["Reading Time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="Mean of Means"))
    fig.show()

def main():
    meanlist=[]
    for i in range(0,1000):
        mean_of_sample=random_set_of_data()
        meanlist.append(mean_of_sample)
    
    mean_graph(meanlist)
    sd=statistics.stdev(meanlist)
    mean=statistics.mean(meanlist)
    print("The mean of means : ",mean)
    print("The standard deviation of means : ", sd)


main()
