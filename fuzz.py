import sys
import os
import os 
import time 
import datetime 
import statistics


current_dir = os.path.dirname(os.path.abspath(__file__))

empirical_dir = os.path.join(current_dir, 'empirical')
sys.path.append(empirical_dir)

import report
import frequency

def fuzzAverage(Mylist):
    try:
        answer = report.Average(Mylist)
    except ZeroDivisionError as e:
        error_message = f"Error in report.Average - Inputs: {Mylist} Error: {e}"
        print(error_message)
        answer = False
    return answer

def fuzzMedian(Mylist):
    try:
        median = report.Median(Mylist)
    except TypeError as e:
      error_message = f"Error in report.Median - Inputs: {Mylist} Error: {e}"
      print(error_message)
      median = False
    return median

def fuzzReportProp(res_file):
    try:
        report.reportProp(res_file)
        result = True
    except FileNotFoundError as e:
        error_message = f"Error in report.reportProp - Inputs: {res_file} Error: {e}"
        print(error_message)
        result = False
    return result

def fuzzReportDensity(res_file):
    try:
        report.reportDensity(res_file)
        result = True
    except FileNotFoundError as e:
        error_message = f"Error in report.reportDensity - Inputs: {res_file} Error: {e}"
        print(error_message)
        result = False
    return result

def fuzzReportProportion(res_file, output_file):
    try:
        frequency.reportProportion(res_file, output_file)
        result = True
    except FileNotFoundError as e:
        error_message = f"Error in frequency.reportProportion - Inputs: {res_file} Error: {e}"
        print(error_message)
        result = False
    return result

if __name__=='__main__':
    list1 = []
    list2 = ["String1", "String2"]
    file_path = 'Invalid File Path'

    fuzzAverage(list1)
    fuzzMedian(list2)
    fuzzReportDensity(file_path)
    fuzzReportProp(file_path)
    fuzzReportProportion(file_path, file_path)