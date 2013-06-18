# -*- coding: utf8 -*-

def get_inserted_money (my_money_dict) :

	#1: 돈을 투입합니다.
	inserted_money_sum = 0  #최종 투입된 금액

	while(True):
		print "*************자판기***************"
		print '\n내 주머니 상황'
		print '--------------------'
		for key,value in sorted(my_money_dict.items()):
			print "%d원이 %d개 있어요" % (key,value)
		print "입금을 마치면 음료구매 설명을 진행합니다"

		inserted_money = raw_input('\n돈을 넣으세요(입금을 마치려면 엔터) : ')
		
		#엔터치면 돈 투입 끝으로 간주하고 while loop를 종료한다
		if not inserted_money:
			break
		#입력 데이터를 숫자형으로 형변환 (왜냐면 $raw_input()은 숫자입력도 문자열로 입력을 받기때문)
		inserted_money = int(inserted_money)
		# 입력받은 돈이 100, 500, 1000, 5000 이 아니면 제대로 하라고 메세지를 띄운다
		if inserted_money not in my_money_dict:
			print "100원, 500원, 1000원, 5000원만 투입하세요"
			continue
		#없는 지폐나 동전을 투입하면 제대로 하라고 메세지를 띄운다
		if my_money_dict[inserted_money]==0:
			print "그 돈은 당신 지갑에 없어요^^; 있는 돈만 넣으세요"
			continue

		#투입한 만큼 지갑에서 돈을 뺀다. (해당 돈의 갯수에서 하나 빼기)
		my_money_dict[inserted_money] -= 1
		
		#누적해서 투입된 돈의 합을 표시한다.
		inserted_money_sum += inserted_money
		print '지금까지 %d가 투입되었네요' % inserted_money_sum


	#투입된 돈의 총 합이 0이상이 아니면..입금이 안된 것임
	if inserted_money_sum <= 0: 
		print '돈이 입금되지 않았네요. 프로그램 종료 합니다'
		return 0

	print '지금까지 %d가 투입되었네요' % inserted_money_sum
	return inserted_money_sum

def buy_product(inserted_money_sum):
	#doctest
	"""
	>>> buy_product(0)
	0
	"""
	
	#만약 투입된 금액이 없으면 실행하지 않는다. 메인에서 처리해도 됨.
	if inserted_money_sum == 0:
		return 0
		
	print "\n**********자판기***********"
	while(True):
		print '지금까지 %d가 투입되었네요' % inserted_money_sum
		print "음료 현황입니다\n"
		
		#현재 음료 현황을 보여줍니다
		for drink in products_dict:
			if products_dict[drink]['number'] > 0:
				print "%s는 %d원이에요" % (drink , products_dict[drink]['price'])
			else:
				print "%s는 %d원이지만 품절이에요. 구매하지마!" % (drink , products_dict[drink]['price'])
		
		drink_to_buy = raw_input('원하는 음료수의 이름을 입력하세요. 엔터를 누르면 구매를 끝내고 반환합니다. : ')
		
		#엔터를 누르면 구매하지 않고 반환함
		if not drink_to_buy:
			print "\n지금까지 투입했던 %d원을 반환합니다" % inserted_money_sum
			change_return(inserted_money_sum, my_money_dict)
			break
			
		#자판기에 없는 음료를 구매하면 없다고 띄워줌
		if drink_to_buy not in products_dict:
			print "\n그런 음료는 없어요 ^^ 있는거 구매하세요"
			continue
		
		#다떨어진 음료를 구매하면 다른거 구매하라고 함. 없으면 품절로 뜨지만 그래도 누르는 반항아들이 있을까봐 추가해둔 코드
		if products_dict[drink_to_buy]["number"]==0:
			print "\n그 음료는 다 떨어졌어요. 다른 음료를 구매하세요"
			continue
			
		#투입된 돈이 음료 가격보다 크거나 같으면 음료를 반환해줌
		if inserted_money_sum >= products_dict[drink_to_buy]["price"]:
			print "\n털컹"
			print "원하신 %s가 반환되었어요." % drink_to_buy
			#음료 갯수를 -1 한다
			products_dict[drink_to_buy]["number"] = products_dict[drink_to_buy]["number"]-1
			#투입되었던 돈을 음료수 가격만큼 조정한다
			inserted_money_sum = inserted_money_sum - products_dict[drink_to_buy]["price"]
			
			#거스름돈이 남았으면 반환하던지, 구매를 계속하던지 한다
			if inserted_money_sum:
				answer = raw_input("거스름돈을 반환하고 구매를 종료하려면 아무거나 입력하세요. 엔터를 누르면 구매를 계속합니다\n")
				if not answer:
					continue
				else:
					print "거스름돈 %d 원을 반환할게요 ^^ 또 이용해주세요" %inserted_money_sum
					change_return(inserted_money_sum, my_money_dict)
					break
			#거스름돈이 없으면 이별 인사한다
			else:
				print "거스름돈이 없어요^^ 또 이용해주세요"
				break
					
		#투입된 돈이 작으면 돈이 모자라다고 함
		else:
			print "\n돈이 모자라요. 다른 음료를 구매해주세요"
			continue
			
#거스름돈 반환이 복잡해서 따로 함수로 뺌
def change_return(change, my_money_dict):
	#5000원부터 100원까지 큰돈부터 내 주머니에 차례대로 넣어주고 change는 그만큼 감소시킨다
	kind_of_money = [5000,1000,500,100]
	while(True):
		for i in range(0,4):
			money_kind = kind_of_money[i]
			while(change >= money_kind) :
				change = change - money_kind
				my_money_dict[money_kind] += 1
		break
	
# 메인 로직
if __name__ == '__main__':

	products_dict = {
					'vita500'   : {'price' : 500, 'number' : 2},
					'milk'      : {'price' : 700, 'number' : 13},
					'coffee'    : {'price' : 900, 'number' : 8}
#                    '음료 이름' : {가격, 갯수}
					}

	#               { 돈의종류 : 돈의갯수 }
	my_money_dict = {5000 : 2 , 1000 : 1, 500 : 2 , 100 : 8}

	while(1):
		#돈 투입하기
		inserted_money_sum=inserted_money = get_inserted_money(my_money_dict)
		#음료 구매하기
		buy_product(inserted_money_sum)