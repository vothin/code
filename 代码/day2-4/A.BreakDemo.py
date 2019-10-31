'''

	 * break,结束整个循环


'''

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("break")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
