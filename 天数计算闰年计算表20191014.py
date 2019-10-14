# 定义year、month和day表示输入的年、月和日
year=int(input('请输入年份'))
month=int(input('请输入月份'))
day=int(input('请输入日期'))

# 定义变量february_days,赋值为28
february_days=28
if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
    # 如果符合闰年的条件，则将february_days更改为29
    february_days = 29

# 定义变量days，用来表示这是一年中的第几天
days = 0
# 如果月份是1，则输入的日期就是今年中的第几天，比如1月10日，就是一年中的第10天
if month == 1:
    days += day
# 如果月返是2，则输入的日期加上第一个月的31天就是一年中的第几天
elif month == 2:
    days = 31 + day
# 如果月份是3，则输入的日期加上第一个月的31天，以及第二个月的天数february_days(可能28，可能29，上面已经计算好)
# 就是一年中的第几天，其他月份依次类推
elif month == 3:
    days = 31 + february_days + day
elif month == 4:
    days = 31 + february_days + 31 + day
elif month == 5:
    days = 31 + february_days + 31 + 30 + day
elif month == 6:
    days = 31 + february_days + 31 + 30 + 31 + day
elif month == 7:
    days = 31 + february_days + 31 + 30 + 31 + 30 + day
elif month == 8:
    days = 31 + february_days + 31 + 30 + 31 + 30 + 31 + day
elif month == 9:
    days = 31 + february_days + 31 + 30 + 31 + 30 + 31 + 31 + day
elif month == 10:
    days = 31 + february_days + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
elif month == 11:
    days = 31 + february_days + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
elif month == 12:
    days = 31 + february_days + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day

# 拼接结果后输出
print('%s年%s月%s日是今年的第%s天' % (year,month,day,days))
