import xlrd  # excel的读取  xlrd目前支持(2007版)与xls(2003版)
import xlsxwriter
import xlwt
from xlutils.copy import copy

"""
读取：xlrd   写入：xlsxwriter  修改（追加写入）：xlutils
"""
def setStyle(name, height,color, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    # 字体类型：比如宋体、仿宋也可以是汉仪瘦金书繁
    font.name = name
    # 设置字体颜色
    font.colour_index = color
    # 字体大小
    font.height = height
    # 定义格式
    style.font = font

    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    # alignment.horz = color

    style.alignment = alignment

    return style


def write_excel_xls_append(excel_w, result_w):
    # 定义文件路径
    path = r"C:\Users\Administrator\Desktop\01.Python3\TS\day8\TestCaseExcel\测试用例.xls"

    # 打开工作簿，formatting_info样式不变的情况下。
    workbook = xlrd.open_workbook(path, formatting_info=True)  # 打开工作簿

    # 获取工作簿中的所有表格
    sheets = workbook.sheet_names()

    # 获取工作簿中所有表格中的的第一个表格
    # worksheet = workbook.sheet_by_name(sheets[0])

    # rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数

    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格

    # 追加写入数据  参数对应：行，列，值，setStyle字体样式(可以没有)
    # new_worksheet.write(excel_w, 9, result_w)
    new_worksheet.write(excel_w, 9, result_w, setStyle('宋体', 400, 2, False))
    new_workbook.save(path)  # 保存工作簿

    # 提示写入数据成功
    # print("xls格式表格【追加】写入数据成功！")





















# write_excel_xls_append(1,"pass")


# https://www.cnblogs.com/xiaodingdong/p/8012282.html