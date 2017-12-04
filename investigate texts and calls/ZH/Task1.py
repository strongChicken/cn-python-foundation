"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)




texts_one = []
texts_two = []
for index in range(len(texts)):
    texts_one.append(texts[index][0])
    texts_two.append(texts[index][1])


texts_sum = []
for text_one in texts_one:
    texts_sum.append(text_one)
for text_two in texts_two:
    texts_sum.append(text_two)


texts_sum_list = []
texts_sum_list = list(set(texts_sum))



calls_one = []
calls_two = []
for indexs in range(len(calls)):
    calls_one.append(calls[indexs][0])
    calls_two.append(calls[indexs][1])


calls_sum = []
for call_one in calls_one:
    calls_sum.append(call_one)
for call_two in calls_two:
    calls_sum.append(call_two)


calls_sum_list = []
calls_sum_list = list(set(calls_sum))       #the way is from "菜鸟教程"

sum_num = len(list(set(calls_sum_list + texts_sum_list)))

print("There are {} different telephone numbers in the records.".format(sum_num))




"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
