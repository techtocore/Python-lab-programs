from flask import Flask, make_response, request, redirect, render_template, Response, url_for, abort, send_from_directory

import matplotlib.pyplot as plt
import matplotlib
import csv
import numpy as np
import pandas as pd
import sys

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('hi.html')


''' 
@app.route('/input')
def input():
    return render_template('t1.html')
'''


@app.route('/q1/<state>')
def q1(state):
    with open('Air_Quality_RIRuo_2010.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # print(csv_reader)
        #print (state)
        p = 0
        t = 0
        for row in csv_reader:
            #print (row[0])
            if (row[0] == state):
                # print("hi")
                p = p + int(row[7])
                t = t+1
        #print ("The average is: ")
        #print (int((p/t)))
        h = str(int(p/t))
        m = "The average is: " + h
        return m


@app.route('/q2/<state>')
def q2(state):
    with open('Air_Quality_RIRuo_2010.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        Moderate = 0
        High = 0
        Critical = 0
        Null = 0
        #quality = []
        for row in csv_reader:
            #print (row[0])
            if (row[0] == state):
                if(row[8] == "Moderate"):
                    Moderate = Moderate + 1
                if(row[8] == "High"):
                    High = High + 1
                if(row[8] == "Critical"):
                    Critical = Critical + 1
                if(row[8] == "Null"):
                    Null = Null + 1
        quality = [Moderate, High, Critical, Null]

        labels = 'Moderate', 'High', 'Critical', 'Null'

        plt.pie(quality, labels=labels)
        plt.axis('equal')
        # plt.show()
        plt.savefig('static/graph.png')
        return app.send_static_file('graph.png')

@app.route('/q3/<c>')
def q3(c):
    with open('Air_Quality_RIRuo_2010.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # print(csv_reader)
        p = 100000
        a = "a"
        b = "b"
        t = 0
        k = 0
        for row in csv_reader:
            if(k == 0):
                k = 1
                continue
            #print (row[0])
            if(c == "1"):
                if(p > int(row[3])):
                    p = int(row[3])
                    a = row[0]
                if(t < int(row[3])):
                    t = int(row[3])
                    b = row[0]
            if(c == "2"):
                if(p > int(row[5])):
                    p = int(row[5])
                    a = row[0]
                if(t < int(row[5])):
                    t = int(row[5])
                    b = row[0]
            if(c == "3"):
                if(p > int(row[7])):
                    p = int(row[7])
                    a = row[0]
                if(t < int(row[7])):
                    t = int(row[7])
                    b = row[0]
            # k=k+1
        d = ("City with lowest of the parameter: " + a)
        e = (" ,  City with highest of the parameter: " + b)
        return (d+e)


'''
@app.route('/inputvalue')
def index1(inputvalue):
  return ('hey' + inputvalue)


@app.route('/input', methods=['POST'])
def input_post():
    data = request.form['text1']
    return redirect(url_for('index1', inputvalue=data))
    #print(data, file=sys.stdout)        # logging to console
    #return redirect(url_for('input'))   # redirecting to /input
    #return render_template('hello.html', name=data)
    '''


@app.route('/input1')
def input():
    return render_template('data.html')


@app.route('/input1', methods=['POST'])
def input_post():
    data = request.form['data']
    print(data, file=sys.stdout)        # logging to console
    return redirect(url_for('q1', state=data))   # redirecting to /input


@app.route('/input2')
def input2():
    return render_template('data1.html')


@app.route('/input2', methods=['POST'])
def input_post2():
    data = request.form['data1']
    print(data, file=sys.stdout)        # logging to console
    return redirect(url_for('q2', state=data))   # redirecting to /input


@app.route('/input3')
def input3():
    return render_template('data2.html')


@app.route('/input3', methods=['POST'])
def input_post3():
    data = request.form['data2']
    print(data, file=sys.stdout)        # logging to console
    return redirect(url_for('q3', c=data))   # redirecting to /input


if __name__ == "__main__":
    app.run(debug=True)
