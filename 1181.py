#1181
num=int(input())
words_list=[];
for i in range(num):
    word=str(input())
    word_count=len(word)
    words_list.append((word, word_count))
words_list=list(set(words_list))
# 중복을 허용하지 않는다.
# set 내부에 있는 값들은 순서가 존재하지 않는다.
words_list.sort(key=lambda word: (word[1], word[0]))
# 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬
# 두 번째 인자를 기준으로 오름차순으로 정렬
for word in words_list:
    print(word[0])

