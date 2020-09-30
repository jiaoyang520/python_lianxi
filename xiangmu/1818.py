text = """ 东边来了个喇嘛，西边来了个哑巴，喇嘛手里拎着五斤挞嘛，哑巴腰里别着个喇叭， 别着喇叭的要用喇叭换手里拎着挞嘛的哑巴的挞嘛， 拎着挞嘛的哑巴不愿意用挞嘛换手里拎着喇叭的喇嘛的喇叭。 拎着喇叭的喇嘛用喇叭打了拎着挞嘛的哑巴， 拎着挞嘛的哑巴也用挞嘛打了拎着喇叭的喇嘛。 """
buffer = []
for i in text:
    if text.count(i) == 1:
        print(i, text.rindex(i))
    else:
        for j in buffer:
            if j == i:
                break
        else:
            print(i, text.rindex(i))
            buffer.append(i)