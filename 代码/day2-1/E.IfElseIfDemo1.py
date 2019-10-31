score = int(input('请输入你的学分：'))

if 100 >= score >= 90:
    print("该学生成绩优秀")
else:
    if 90 > score >= 80:
        print("该学生成绩良好")
    else:
        if 80 > score >= 60:
            print("该学生成绩中等")
        else:
            if 60 > score:
                print("该学生成绩不及格")
