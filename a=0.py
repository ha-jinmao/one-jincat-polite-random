import time 
import random
import sys
while True:
    a=0
    print("欢迎使用近猫随机整数")
    for p1 in range(5):
        choice=input("你要取整数还是小数？（整数回答“整”，小数回答“小”）")
        if choice not in ("整", "小") :
            if p1<4:
                print("何意味？only“整”或“小”can do，不服就滚")
            else:
                print("“整”和“小”就两个字，都打不出？你妈生了个啥子？！来找茬的？")
                sys.exit()        
        else:
            break           
    for i in range(2):
        while True:
            try:
                if choice=="整":
                        a=int(input("请输入最大数"))
                        time.sleep(0.5)
                        b=int(input("请输入最小数"))
                        time.sleep(0.5)
                        break
                else:
                    a = float(input("请输入最大数"))
                    b = float(input("请输入最小数"))
                    break
            except ValueError:
                if choice=="整":         
                    print("请输入整数！")
                else:
                    print("请输入整数或小数！")
        if a<b:
            print("关爱盲人，温暖同行\n近猫人文关怀已将您输入的相反数据倒换，请确认：")
            a,b=b,a
            print("请确认最大数：",a)
            time.sleep(2)
            print("请确认最小数：",b)
            time.sleep(2)
        if choice=="整":
            for p in range(5):
                user1=input("是否包含最大数（请输入是或否）")
                time.sleep(0.5)
                user2=input("是否包含最小数（请输入是或否）")
                if user1 not in ("是", "否") or user2 not in ("是", "否"):
                        if p<4:
                            print("你瞎吗？只能输入“是”或“否”，不服就滚")
                        else:
                            print("“是”和“否”就两个选项，你五次都没选中，这概率比拼多多提现成功的还低，你却做到了，原来这就是传说中的天赋。\n亲，这边建议带着你的答非所问去看精神科，算了，这种治好了也流口水\n滚吧，老子不伺候了。")
                            sys.exit()        
                else:
                    break           
            c = None 
            try:
                if user1=="是":
                    if user2=="是":
                        c=random.randint(b, a)
                    if user2=="否":
                        c=random.randint(b+1, a)
                if user1=="否":
                    if user2=="是":
                        c=random.randrange(b, a)
                    if user2=="否":
                        c=random.randrange(b+1, a)
            except ValueError:
                c = None  
        else:
            c = random.uniform(b, a)
        if c is not None:
            print(c)
            time.sleep(2)
            for p12 in range(5):
                z=input("是否再来一次（是，否）")
                if z not in ("是", "否") :
                    if p12<4:
                        print("何意味？only“是”或“否”can do，不服就滚")
                    else:
                        print("“是”和“否”就两个字，都打不出？你妈生了个啥子？！来找茬的？")
                        sys.exit()        
                else:
                    break           
            if z=="是":
                print("好")
                break  # 跳出 for i，让 while True 重新开始
            else:
                print("再见")
                sys.exit()  
               
        elif i==0:
            print("你的胆子真是肥嘟嘟的\n不听近猫言，吃亏在眼前。我劝你好好检查：\n最大值是否等于最小值，或当你选择不包含其中一数时，最大值与最小值的差是否小于1。当你选择不包含两数时，最大值与最小值的差是否小于2")
            d=input("你有一次机会改：(想就输入“是”)")
            if d=="是":
                print("只有一次！")
            else :
                break
        else :
            print("给你机会你不中用啊，滚！")
            sys.exit()
    