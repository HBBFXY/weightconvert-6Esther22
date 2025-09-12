#weightConvert.py
weightStr=input()
if weightStr[-2:] in ['kg']:
    pd=(eval(weightStr[0:-2]))*2.2046
    print("对应的英制重量为{:.3f}磅".format(pd))
elif weightStr[-2:] in ['pd']:
    kg=(eval(weightStr[0:-2]))/2.2046
    print("对应的公制重量为{:.3f}公斤".format(kg))
else:
    print("输入格式错误")
