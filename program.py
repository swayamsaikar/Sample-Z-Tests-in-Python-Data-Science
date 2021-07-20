import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

ReadingTimeData = pd.read_csv('medium_data.csv')["reading_time"]

mean = statistics.mean(ReadingTimeData)
std = statistics.stdev(ReadingTimeData)

print(f"Mean of the ReadingTimeData is -> {mean}")
print(f"Standard Deviation of the ReadingTimeData is -> {std}")

first_std_start, first_std_end = mean-std, mean+std,
second_std_start, second_std_end = mean-(2*std), mean+(2*std),
third_std_start, third_std_end = mean-(3*std), mean+(3*std),

print(f"std1 start and end :- {first_std_start},{first_std_end}")
print(f"std2 start and end :- {second_std_start},{second_std_end}")
print(f"std3 start and end :- {third_std_start},{third_std_end}")


def random_mean_set(counter):
    dataset = []

    # for 30 times it will generate a random index and find the value on that particular randomIndex in the ReadingTimeData array and append that value in the dataset array
    for i in range(0, counter):
        # this function will generate a random number or integer between 0 and total length of ReadingTimeData
        randomIndex = random.randint(0, len(ReadingTimeData)-1)

        # And then we are finding the value on that particular randomIndex in the ReadingTimeData
        randomIndexValue = ReadingTimeData[randomIndex]

        # And then we are appending the value we got in the dataset array or list
        dataset.append(randomIndexValue)

        # and we are repeating this same process for 30 times with this for loop

    mean_of_dataset = statistics.mean(dataset)

    return mean_of_dataset


def plotGraph(meanList):
    arr = meanList

    figure = ff.create_distplot([arr], ["reading_time"], show_hist=False)

    # added Traces to indicate teh location of mean 1st std,2nd std and 3rd std

    # start traces
    figure.add_trace(go.Scatter(x=[mean, mean], y=[
                     0, 0.20], mode="lines", name="Mean"))
    figure.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[
                     0, 0.20], mode="lines", name="first_std_start"))
    figure.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[
                     0, 0.20], mode="lines", name="second_std_start"))
    figure.add_trace(go.Scatter(x=[third_std_start, third_std_start], y=[
                     0, 0.20], mode="lines", name="third_std_start"))

    # end Traces
    figure.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[
        0, 0.20], mode="lines", name="first_std_end"))

    figure.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[
                     0, 0.20], mode="lines", name="second_std_end"))

    figure.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[
                     0, 0.20], mode="lines", name="third_std_end"))

    figure.show()


def setup():
    # in this list we will store all the returned means from the random_mean_set() function
    meanList = []

    for i in range(0, 100):
        # This function will find the means of 30 random data samples and return that mean (repeat this process for 30 times so we will get 100 means)
        set_of_returned_means = random_mean_set(30)

        # appending each mean that random_mean_set() returned (for 30 times)
        meanList.append(set_of_returned_means)

    meanOfMeanList = statistics.mean(meanList)
    stdOfMeanList = statistics.stdev(meanList)

    print(f"Mean of the Mean List is -> {meanOfMeanList}")
    print(
        f"Standard Deviation of the Mean List is -> {stdOfMeanList}")

    z_Score = (meanOfMeanList - mean)/std
    print(f"Z-Score is :- {z_Score}")

    plotGraph(meanList)


setup()
