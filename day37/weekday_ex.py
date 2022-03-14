import datetime

# 날짜를 입력하면 요일을 출력하는 함수 정의
def  get_weekday(yyyy, mm, dd):
    days = ['월', '화', '수', '목', '금', '토', '일']
    week_idx = datetime.date(yyyy, mm, dd).weekday()
    print(days[week_idx] + "요일")

# get_weekday() 호출
get_weekday(2022, 3, 14)

'''
now = datetime.datetime.today()             # 날짜와 시간
print(now)
print("{}년".format(now.year))
print(str(now.month) + "월")
'''

today = datetime.date.today()
print(today)


# 특정한 날짜
theday = datetime.date(2022, 3, 13)
print(theday)

days = ['월', '화', '수', '목', '금', '토', '일']

# 요일
week_idx = datetime.date(2022, 3, 12).weekday()
print(week_idx)         # 0 - 월, 1 - 화, ..... 6-일
print(days[week_idx] + "요일")