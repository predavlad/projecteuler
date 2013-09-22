# for i in range(100):
#     text = ''
#     if i % 3 == 0:
#         text += "Fizz"
#     if i % 5 == 0:
#         text += "Buzz"
#     if not len(text):
#         text = i
#     print text


for i in range(1, 101):
    txt = ''
    for key, val in {3: 'Fizz', 5: 'Buzz'}.items():
        if not i % key:
            txt += val
    if txt == '':
        txt = i
    print txt

# print [i in range(1, 100) if i % 15 != 0 else("Fizz" if i % 3 == 0 else("Buzz" if i % 5 == 0))]
