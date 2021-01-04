#Autor: Alexis Lopez
#Version: 1.0
#This is an excel csv column analizer with an event counting

#Needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF

#Global variables
csv_input="/test.csv"
column_of_interest=['fruta']
events= ["mango"]

#This function receives a csv file and the user parameters
def data_input():
    print (pd.read_csv('test.csv'))
    print("done INPUT")
#This function transforms the csv data in to manegable data
def data_transformation(csv_input):
    data_set=pd.read_csv('test.csv')                                            #Reading the csv as a data set
    data_analizing(data_set)
    print("done TRANSFORMING")
#This function performs the data analisis acording to the user needs
def data_analizing(data_set):
    event_counter= data_set.pivot_table(index=['fruta'], aggfunc='size')        #Counting repetitions con selected column
    data_set_a=pd.DataFrame(data_set,columns= ['antes'])                        #Generating data set for comparison
    data_set_b=pd.DataFrame(data_set,columns= ['despues'])                      #Generating data set for comparison
    data_set_a['intentsMatch?'] = np.where(data_set_a['antes'] == data_set_b['despues'], 'True', 'False') #comparing both datasets and generating one column with the result
    intents_counter= data_set_a.pivot_table(index=['intentsMatch?'], aggfunc='size') #Counting False and Trues
    print(intents_counter)
    data_visualization(event_counter, intents_counter)
    print("done ANALIZING")
#This function creates the plots and text boxes for the report
def data_visualization(event_counter, intents_counter):
    #Inten Repetitions Plot
    event_counter.plot(kind='bar')
    plt.ylabel('Repetitions Count')
    plt.xlabel('Intent')
    plt.title("Intent Repetitions")
    plt.show()
    #INtents Mismatch Plot
    intents_counter.plot(kind='bar',colormap='Paired')
    plt.ylabel('Repetitions Count')
    plt.xlabel('Events')
    plt.title("Intents Mismatch")
    plt.show()

    data_reporting()

    print("done VISUALIZING")
#This function creates the pdf final report
def data_reporting():

    print("done RESPORTING")

data_transformation(csv_input)
#data_input()
