import crossfitPlan_class as cf
import random
import pandas as pd
from datetime import date

if __name__ == '__main__':
    
    try:
        today = date.today()
        randomDayCount = random.randint(2, 5)
        totalPerstageCount = random.randint(1, 3)   
        maxSojuCount = random.randint(3, 12)                        
        
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
        print('데이터 프레임 미생성 재실행')
        print(e)

#TODO : 어차피 ex.py 에서 randomDayCount, totalPerstageCount, maxSojuCount 변수를 우선적으로 받는데, class.py 에서 
#TODO : self.totalPerStageCount = random.randint(1, 2) #! 소주 최대 2차, self.maxSojuCount = random.randint(2, 6) #! 소주 전체 병수 최소 2병 ~ 최대 6병를 또 받고 있어서 비효율적으로 보임.....

    