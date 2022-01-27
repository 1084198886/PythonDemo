"""
xlwings操作excel
"""
import time

import xlwings as xw

xls_filename = 'example.xls'
app = xw.App(visible=True, add_book=False)  # visible--表示处理过程是否可视,True时会自动打开文件   add_book--是否打开新的Excel程序


def create_excel(filename):
    """
    创建Excel文件
    """
    # if not os.path.exists(filename):     文件存在也要新建覆盖，执行add方法，否则app.books[0]将取不到
    print(f'start create {filename} ...')
    ex = app.books.add()
    ex.save(f'./{filename}')  # 创建Excel文件
    time.sleep(0.5)


create_excel(xls_filename)

# wb = xw.Book(xls_filename)  # 打开文件方式1
# wb = app.books.open(xls_filename)  # 打开文件方式2

wb = app.books[0]  # 取第一个创建的Excel文件
sht = wb.sheets('sheet1')
print('工作表绝对路径:', wb.fullname)  # 返回工作表绝对路径

# 注意：  Excel是基于1的索引的元组，命名范围或两个Range对象来实例化范围

# 注意： 尽量减少与Excel的交互次数。 执行sht.range('A1').value = [[1,2],[3,4]] 总是比
# sht.range('A1').value = [1, 2] 和sht.range('A2').value = [3, 4] 执行2次  更有效。


for i in range(20):
    sht.range('A1').columns.autofit()  # 列宽自适应
    sht.range('B1', 'B20').color = (181, 175, 175)  # 给单元格上背景色，传入RGB值
    sht.range('A1').rows.autofit()  # 行高自适应
    sht.range(f"A{i + 1}").value = f"{i + 1}"  # 单元格中写入数据
    sht.range(f"C{i + 1}").value = f"A{i + 1}_value_value_value_value"

    sht.range('C1').columns.autofit()  # 列宽自适应
    sht.range('C1').rows.autofit()  # 列宽自适应

sht.range('A30:A31').value = [[1, 2, 3, 4], [2, 3, 4, 5]]  # 一次性给一个区间赋值

print('读取单元格区间内容：', sht.range('A1', 'C20').value)
# sht.range('A1', 'A2').clear()  # 清除单元格内容和格式

print('获取单元格的列标：', sht.range('B2').column)
print('获取单元格的行标：', sht.range('B3').row)
print('获取单元格的列宽：', sht.range('B3').column_width)
print('获取单元格的行高：', sht.range('B3').row_height)
print('获取单元格的颜色：', sht.range('B1', 'B20').color)
sht.range('B1').color = None  # 清除单元格颜色

sht.range('A21').formula = '=SUM(A3:A9)'  # 输入公式，相应单元格会出现计算结果
print('获取单元格公式：', sht.range('A21').formula_array)

sht.range('A22').value = ['Foo-big1', 'Foo-big2', 'Foo-big3']  # 单元格中写入批量数据,1个list表示1行

sht.range('A25').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0],
                          [10.0, 20.0, 30.0], ['s1', 's2', 's3']]  # 单元格中写入批量数据,列表中的每个list占用1行

print('expand()方法读取表中批量数据：', sht.range('A24', 'C27').expand().value)

print('在活动的工作簿app：', app.books.active)
print('在活动的工作表sheet：', app.books.active.sheets.active)

sht.range('A35').options(transpose=True).value = [1, 2, 3, 4]  # 列方向向Excel写入列表
sht.range('A39').value = [1, 2, 3, 4]

"""
xlwings与numpy 和 pandas的联动
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 支持写入numpy array数据类型
sht.range('F1').value = np.array([('f', 'g', 'h'), ('f1', 'g2', 'h3')])

# 支持将pandas DataFrame数据类型写入excel
df = pd.DataFrame([[1, 2, np.nan], [3, np.nan, 5]], columns=['a', 'b', 'c'])
sht.range('F2').value = df

vu = sht.range('F3').options(pd.DataFrame, expand='table').value
print("将数据读取，输出类型为DataFrame：", vu)

s = pd.Series([1, 2, 3, np.nan, 6.0, 5.], name='title1')
print("pd.Series： \n", s)

sht.range('A45').value = s

fig = plt.figure()
plt.plot([1, 2, 3, 4, 5])
sht.pictures.add(fig, name='MyPlot', update=False, left=sht.range('F8').left,
                 top=sht.range('F8').top)  # 将Matplotlib图作为图片粘贴到Excel中   注意range只有left,top属性

"""
操作sheet2
"""
sht2 = wb.sheets('sheet2')
sht2.range('A1').value = "A1111"

"""
以下方法时保存后自动 释放资源，然后关闭
"""
# wb.save()
# wb.close()
# app.quit()
