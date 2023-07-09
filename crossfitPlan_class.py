import random

day_dict = {'월' : 1, '화' : 2, '수' : 3, '목' : 4, '금' : 5}

#TODO : 크로스핏 주기와 일정 계획

class Crossfit:
    
    def __init__(self, dayCount):
        self.dayCount = dayCount
            
    def crossfitScheduleCount(self):
        breakdayCount = 5 - self.dayCount 
        return self.dayCount, breakdayCount

    def crossfitDayOfWeek(self, dayCount):    
        global day_dict
        exerciseDay = sorted(random.sample(list(day_dict.keys()), self.dayCount), key = lambda x:day_dict[x])
        return exerciseDay

    #TODO 주간 크로스핏 운동 참여 날 음주 가능 요일 수와 해당 요일
    #TODO 가능한 소주 병수, stage(1차, 2차, 3차), stage 마다 먹을 소주량
    #TODO 음주는 주 1회로 한정

class CrossfitSoju():
    
    def __init__(self, exerciseDay, dayCount):
        self.exerciseDay = exerciseDay
        self.dayCount = dayCount
        
    global sojuDay

    def crossfitSojuDayPlan(self):        
        
        global day_dict

        try:
            self.sojuDay = sorted(random.sample(self.exerciseDay, 1), key = lambda x: day_dict[x]) 
        except ValueError:
            self.sojuDay = 'X'
            print('ValueError 발생 - 재셔플')  
        
        self.totalPerStageCount = random.randint(1, 2) #! 소주 최대 2차
        self.maxSojuCount = random.randint(2, 6) #! 소주 전체 병수 최소 2병 ~ 최대 6병
    
        return self.sojuDay, self.totalPerStageCount, self.maxSojuCount


    global aimCount
    global eatTotal
    eatTotal = 0
    aimCount = 0
    
class CrossfitSojuCnt():

    def __init__(self, dayCount, sojuDay, totalPerStageCount, maxSojuCount):
        self.dayCount = dayCount
        self.sojuDay = sojuDay
        self.totalPerStageCount = totalPerStageCount
        self.maxSojuCount = maxSojuCount
        self.sojuDictList = []
                
    def crossfitSojuCnt(self):
        
        if self.sojuDay == 'X':
            print('Shuffle 다시!!')
            pass
        else:
            global aimCount
            global eatTotal
            
            for per in range(1, self.totalPerStageCount + 1): 
                if per == 1:
                    aimCount = int(self.maxSojuCount * 0.7) #! 1차 부터는 최대 소주량의 70%
                    eatTotal += aimCount
                
                else:                              
                    aimCount = int(aimCount * 0.3)  #! 2차 부터는 남은 소주량의 30%
                    eatTotal += aimCount
                
                self.sojuDictList.append(f'{per}차 : {aimCount}병')
                
                if aimCount <= 3: #! 잔여 되는 소주
                    continue           
            return self.sojuDictList, eatTotal
          
        
#crossfitDayOfWeek()
#crossfitSojuDayPlan()
#? -------------------------------------------------------------------------------------------------

#* 매 분 마다,
#* roundCnt 3 / 5 / 6 / 7 / 10  
#* BOX: 크로스핏을 하는 체육관 혹은 센터
#* workOutOfTheName #* 매일 박스에서 이루어지는 운동
#* BW 비더블로 Body Weight의 준말, 자신의 체중
#* LB : 파운드(10LB, 15LB, 20LB, 25LB, 30LB)

#* penalty #* 목표치를 못 채울 수록 penalty (Unbroken, breakpenalty)
#* AMRAP 제한시간 내 최대한의 반복하는 운동 방식(As many Reps As Possible)
#* EMOM (Every Minute on the Minute): 매 분마다 정해진 운동을 수행
#* AFAP 최대한 빨리 수행할 것 (As Fast As Possible)
#* ForTime 정해진 반복수를 최대한 빠른 시간 내 하는 방식
#* NorEP 자세가 완벽하지 못해 개수로 인정되지 않는 것
#* PR Personal Record의 약자. 자신의 최대기록
#* UNBROKEN : 쉬는시간 없이 끝까지 수행
#* LADDER : 무게 또는 횟수를 계속 올리며 진행
#* Chipper: 수행해야 할 여러개의 운동을 순서대로 마치 문제를 해결하는 것처럼 해결
#* Scaling: 운동의 난이도를 개인의 수준에 맞게 조절, 체력, 기술 능력, 부상 여부 등을 고려하여 운동을 조정

#! 고려사항 : 목표 설정(체력 향상, 근력 강화, 체중 감량, 기술 개선...)
#! 운동 요소 선택 : 웨이트 리프팅, 유산소 운동, 체중 감량을 위한 운동, 근력 강화를 위한 운동
#! 주기와 일정: 개인의 일정과 가능한 운동 일수를 고려하여 주기와 일정을 계획, 
#! 일주일에 몇 번 운동할 것인지, 휴식일은 어떻게 배치할지
#! 운동 선택과 조정
#! 일정 주기마다 진행 상황 평가
#! 안전과 휴식 고려