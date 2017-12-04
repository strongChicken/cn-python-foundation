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


BLR_call = []
BLR_rece = []
BLR_BLR = []
for index in range(len(calls)):
    call_num = calls[index][0]
    if '080' == call_num[1:4]:
        BLR_call.append(call_num)

        rece_num = calls[index][1]
        BLR_rece.append(rece_num)

        if '080' == rece_num[1:4]:
            BLR_BLR.append(rece_num)

aim_set = set()
for temp in BLR_rece:
    if ' ' == temp[5]:
        code_mobi = temp[0:4]
        aim_set.add(code_mobi)

    if '(' == temp[0]:
        code_area = temp[1:temp.index(")")]
        if code_area not in aim_set:
            aim_set.add(code_area)
    if ' ' != temp[4] and '140' == temp[0:3]:
        aim_set.remove(temp)

aim_list_sort = sorted(aim_set)
last_list = "\n".join(aim_list_sort)
print("The numbers called by people in Bangalore have codes:{}\n".format(last_list))

proportion = (float)(len(BLR_BLR))/len(BLR_call) * 100
result = "%0.2f%%" % proportion         #the way is from Internet
print("{} percent of calls from fixed lines in Bangalore are callsto other fixed lines in Bangalore.".format(result))






"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字母顺序输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
