# def substring(s):
#     l = []
#     for i in range(len(s)):
#         temp = s[i]
#         for j in range(i+1,len(s)):
#             if s[j] in temp:
#                 break
#             else:
#                 temp = temp + s[j]
#         l.append(len(temp))
#     # s = []
#     # for i in l:
#     #     s.append(len(i))
#     return max(l)
# print(substring("pwwkeww"))

# a = 5nksjEtieskfijmsxkn
# def f(a):
#     a += 5
    
# f(a)
# print(a)

s = "Python Programming"
print(s.index('o', 5, 10))