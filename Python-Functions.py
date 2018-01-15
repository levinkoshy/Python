items = ["Mic", "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 134]

str_items = []
num_items = []


for i in items:
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass


print(str_items)

print(num_items)

#split -numbers,strings
def parse_list(some_list):
    str_list_items = []
    num_list_items = []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass
    return str_list_items, num_list_items


print(parse_list(items))

#Sum
def my_sum(num_list):
    total=0
    for i in num_list:
        if isinstance(i, float) or isinstance(i, int):
            total +=i
    return total

print(my_sum(items3))
#3580.243

#Average
def my_average(num_list):
    total=0
    count=0
    for i in num_list:
        if isinstance(i, float) or isinstance(i, int):
            total +=i
            count +=1
    return total/(count*1.0)



import datetime


default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""


def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.date.today()
        text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        for name in names:
            new_amount = "%.2f" %(amounts[i])
            new_msg = unf_message.format(
                    name=name,
                    date=text,
                    total=new_amount
                )
            i += 1
            print(new_msg)



make_messages(default_names, default_amounts)


