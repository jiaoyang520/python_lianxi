age = 19

if age >= 18:
    print("以满18岁，欢迎来到英雄联盟！")
else:
    print("未满18岁约，不能玩的")

age1 = input("请输入你的年龄:")
age1 = int(age1)
if age1 >= 18:
    print("欢迎来到网咖！")
else:
    print("你还未成年")

age2 = 1000

if age2 >=0 and age2 <= 120:
    print("输入的年龄合法！")
else:
    print("您输入的年龄不正确！")


mr_id_card = True
sjj_id_card = False
if mr_id_card or sjj_id_card:
    print("欢迎入住")
else:
    print("不能入住")

is_student = True
if not is_student:
    print("能进入学校")
else:
    print("不能进入学校!")


holiday_name = "情人节"
if holiday_name == "情人节":
    print("买鲜花看点影")
elif holiday_name == "平安夜":
    print("买苹果，吃大餐")
elif holiday_name == "生日":
    print("买蛋糕")
else:
    print("都是节日，你却单着呢！")


has_ticket = True
knife_length = 23
if has_ticket:
    print("火车票通过")
    if knife_length >= 20:
        print("刀具超过20不能上火车")
    else:
        print("安检通过key上火车了")
else:
    print("没有火车票不能进入")

