score = int(input('请输入你的学分：'))

if 90 <= score <= 100:
    print("该学生成绩优秀")
elif 90 > score >= 80:
    print("该学生成绩良好")
elif 80 > score >= 60:
    print("该学生成绩中等")
elif 60 > score:
    print("该学生成绩不及格1")
