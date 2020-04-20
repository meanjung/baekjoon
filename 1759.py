#1759
# 최소 한 개의 모음, 최소 두 개의 자음
# 서로 다른 L개의 알파벳 소문자들로 구성
def check(combStr):
    vowel=0 #모음
    consonant=0 #자음
    for char in combStr:
        if char in ['a','e','i','o','u']:
            vowel+=1
        else:
            consonant+=1
    if consonant>=2 and vowel>=1:
        return True
    else:
        return False

def solution(L, word, combStr, index):
    if len(combStr)==L:#암호문의 길이가 L이면 검사
        if(check(combStr)==True):
            print(''.join(combStr))
        return
    if index>=len(word):
        return
    solution(L, word, combStr+list(word[index]), index+1) #해당 index의 문자를 추가하거나
    solution(L, word, combStr, index+1) #추가하지 않거나

L,C=input().split()
L=int(L)
C=int(C)
word=list(map(str,input().split()))
word.sort() # 알파벳 순서로 정렬

combStr=[]
index=0

solution(L, word, combStr, index)
