data = []
count = 0
with open('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sumlen = 0
for d in data:
	sumlen = sumlen +len(d)

print('留言平均長度是', sumlen/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new),'筆留言長度小於100')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)

# list comprehesion 快寫法
good = [d for d in data if 'good' in d]
print(good)
bad = ['bad' in d for d in data]
print(bad)

bad = []
for d in data:
	bad.append('bad' in d)




print('一共有', len(good),'筆留言提到good')
print(good[0])
print(good[1])

