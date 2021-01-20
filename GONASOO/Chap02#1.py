###
### 과목 별 점수들의 평균 점수
###

# type: dictionary
score = {'국어':80, '영어':75, '수학':55}
print('score : ', score)

# extract values from score
# convert dictionary to list
_score = list(score.values())
print('_score : ', _score)

# average
avg = (_score[0]+_score[1]+_score[2])/len(_score)
print('avg : ', avg)
