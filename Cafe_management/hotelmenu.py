# Here i am defining menu for my restaurant :
menu={
    'Dal Makhani ': 120,
    'Dal fry ':80,
    'Plain yellow Dal':50,
    'White rice':30,
    'jeera rice':50,
    'fried rice':100,
    'pulav':120,
    'Biryani':200,
    'salad':100,
    'coffee':50,
    'Tea':20,
    'cola':20,
    'sprite':20,
    'mazza':30,
    'pinacolda':120    
}

#greetings:

print("Welcome to my restaurant")
print("Dal Makhani:Rs120\nDal fry: Rs80\nPlain yellow Dal: Rs50\nWhite rice: Rs30\njeera rice: Rs50\nfried rice: Rs100\npulav:Rs120\nBiryani: Rs200\nsalad: Rs100\ncoffee:Rs50\nTea:Rs20\ncola: Rs20\nsprite: Rs20\nmazza: Rs30\npinacolda: Rs120")

order_total=0

item_1=input("What do you want to have for today ?")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"okay {item_1} added ")
else:
    print(f"ordered {item_1} is not available today")

another_order=input("would you like to order something else ? (Yes/No)")
if another_order=='Yes':
    item_2=input("What else would you like to have ?")
    order_total+=menu[item_2]
    print(f"okay {item_2} is added")
else:
    print(f"ordered {item_1} is not available today")

print(f"Total to pay {order_total}")