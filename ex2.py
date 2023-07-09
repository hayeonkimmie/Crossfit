import crossfitPlan_class2 as cf
import random
import pandas as pd
from datetime import date

if __name__ == '__main__':
    
    try:
        today = date.today()
        randomDayCount = random.randint(2, 5)                      
        
        ex = cf.Crossfit(randomDayCount)
        dayCount, breakdayCount = ex.crossfitScheduleCount()
        exerciseDay = ex.crossfitDayOfWeek(dayCount)
        exerciseDay = ' '.join(exerciseDay)
        ex2 = cf.CrossfitSoju(exerciseDay, dayCount)
        sojuDay, totalPerStageCount, maxSojuCount = ex2.crossfitSojuDayPlan()
        sojuDay =''.join(sojuDay)
        ex3 = cf.CrossfitSojuCnt(dayCount, sojuDay, totalPerStageCount, maxSojuCount)
        sojuDictList, eatTotal = ex3.crossfitSojuCnt()
        sojuDictList = ' '.join(sojuDictList)
        remindSoju = maxSojuCount - eatTotal
        
        data = [{
            'TodayDate' : today,
            'ExerCiseDayCount' : dayCount,
            'ExerCiseDay' : exerciseDay,
            'SojuDay' : sojuDay,
            'TotalStageCount' : totalPerStageCount,
            'MaxSojuCount' : maxSojuCount,
            'FixSojuCount' : eatTotal,
            'RemindSojuCount' : remindSoju,
            'PlanSoju' : sojuDictList
            }]
        
        crossfitPlan = pd.DataFrame(data).reset_index(drop = True)
        print(crossfitPlan)
        
        crossfitPlan.to_csv('crossfitPlan.csv', index = False)
        
    except Exception as e:
        print('에러로 인한 데이터 프레임 미생성 재실행하기!!!')
        print(e)