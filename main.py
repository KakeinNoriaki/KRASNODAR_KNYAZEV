text = input()
text_list = list(text)

count = 1

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        break
print(text[0] + str(count))

print('Хоба, новый комит')