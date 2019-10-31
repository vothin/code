"""
if-else-if多选择分支

			if(条件表达式1):
				当条件表达式1为true时，要执行的语句
				如果该选择分支执行完毕后，整个选择语句结束
			elif(条件表达式2):
				当条件表达式2为true时，要执行的语句
				如果该选择分支执行完毕后，整个选择语句结束
			elif(条件表达式3):
				当条件表达式3为true时，要执行的语句
				如果该选择分支执行完毕后，整个选择语句结束
			elif(条件表达式n):
				当条件表达式n为true时，要执行的语句
				如果该选择分支执行完毕后，整个选择语句结束
			else
				当所有的条件表达式都为false时，要执行的语句
				如果该选择分支执行完毕后，整个选择语句结束
			注意：
			1.无论有多少个分支，最终结果只会执行其中一个分支中的语句
			(只有在所有条件都不成立，并且没有else分支时，才不会执行任何的语句)
			2.当多个条件表达式同时成立时，也只会执行其中的一个分支，
			执行的为最上面的(第一个成立的)选择分支
"""

# 100分制，90分以上为优秀，80-90为良好，60-80为中等，60以下为不及格

score = int(input('请输入你的学分：'))

if 100 >= score >= 90:  # 90-100
    print("该学生成绩优秀")

if 90 > score >= 80:  # 80-90
    print("该学生成绩良好")

if 80 > score >= 60:  # 60-80
    print("该学生成绩中等")

if 60 > score:  # 0-60
    print("该学生成绩不及格")
