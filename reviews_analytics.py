data = []
count = 0
with open('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

print(data[0])


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





wc = {} #word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1  #新增新的key進wc字典

for word in wc:
	if wc[word] > 100000:
		print(word, wc[word])

print(len(wc))
print(wc['Bryant'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔')
print('感謝使用本查詢功能')
	


