import os #作業系統 operating system
#讀取檔案
products = []
if os.path.isfile('products.csv'): #檢查檔案在不在
	print('找到了')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品名稱,價錢' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
		print(products)
else:
	print('找無')


#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])


#印出所有購買紀錄
for p in products:
	print(p[0] + '的價錢是' + p[1])


#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品名稱,價錢\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

