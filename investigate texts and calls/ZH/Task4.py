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

sell_num = []
receive_list = []
for temp in calls:
     receive_num = temp[1]
     receive_list.append(receive_num)

for index in range(len(calls)):
    call_num = calls[index][0]
    if (call_num not in receive_list) and (call_num not in sell_num):   
        sell_num.append(call_num)

for index_text in range(len(texts)):
    send_num = texts[index_text][0]
    if send_num in sell_num:
        sell_num.remove(send_num)

for temp_rece in texts:
    rece_num = temp_rece[1]
    if rece_num in sell_num:
        sell_num.remove(rece_num)


sell_num = sorted(sell_num)
sell_num = "\n".join(sell_num)
print("These numbers could be telemarketers: \n{}".format(sell_num))


"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字母顺序输出。
"""

