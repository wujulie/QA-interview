

def main():
    name_list = ["德瑞克", "尚恩", "傑夫", "馬基"]
    score_list = []
    for i in name_list:
        n = int(input(i + "的原始分數為:"))
        score_list.append(n)
    print("\n")


    for name, score in zip(name_list, score_list):
        ori = score
        temp = 5 - (score % 5)
        if (temp <= 3) :
            score = score + temp
        if score < 40:
            print(name + "調整後分數為:" + str(ori))
        else:
            print(name + "調整後分數為:" + str(score))



if __name__ == '__main__':
    main()


















# for name, score in zip(name_list, score_list):
#         if score < 40:
#             score = score
#             temp = 5 - (score % 5)
#             if (temp <= 3): score = score + temp
#         print(name + "調整後分數為:" + str(score))