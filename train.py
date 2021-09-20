from PIL import Image
import numpy as np

i = Image.open('Images/numbers/0.9.png')
iar = np.array(i)
u = str(iar.tolist())
test = u.split('],')
print('this is the test image')
print('\n')

print(test)
with open('data.txt', 'r') as j:
    e = j.read()
k = e.split('\n')
score = []
result = []
for r in range(0, len(k)):
    first = k[r].split('::')
    pixel = first[1].split('],')
    # print('\n')
    # print('this is the notepad image 0.1.png')
    # print(pixel)
    # comparing pixel by pixel
    for rishi in range(64):
        if pixel[rishi] == test[rishi]:
            score.append(int(first[0]))
for q in range(0, 9):
    result.append(score.count(q))
m = max(result)
print(result)
print(result.index(m))
confidence = (m/576) * 100
gg = round(confidence)
print(gg, '%')
