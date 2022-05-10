# Python有迭代和分支两大控制结构，通过while、for实现迭代
wordlist = ["angel", "bule", "cat"]
letter_list = []
for word in wordlist:
    print(word)
    for letter in word:
        letter_list.append(letter)
print(letter_list)
# 列表可通过迭代和分支结构来创建，这就是列表解析式
sq_list = [x ** x for x in range(10) if x % 2 != 1]
print(sq_list)
