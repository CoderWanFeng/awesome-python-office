# 导入这个库：python-office，简写为office
import office

#1行代码，验证是否绑定成功
office.excel.merge2excel(dir_path=r'C:\程序员晚枫\excel-merge\excel',output_file='test.xlsx')

#参数作用：
# dir_path = 文件夹的位置，建议把需要合并的多个excel文件放到同一个文件夹里。
# output_file = 最终合并的excel文件放在哪里、叫什么名字，可以不填，默认是：merge2excel.xlsx