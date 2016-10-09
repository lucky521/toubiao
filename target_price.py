# this script help to get the best target_price
import random 

#target_price = 0  # our target 
#company_data = [1,2,3,4,5]  #XXX: need to change here
#control_price = 100

#evaluate_price = control_price
#company_num = len(company_data)
#total_price = 0

############################################
CONTROL_PRICE = 100

############################################
#TODO: remove max and min
def get_total_price(num, data):
	if num <= 0:
		print "num <=0 !"
		return 0
	if len(data) != num:
		#print "error data len is not num"
		return 0

	if num < 5:
		sorted_data = data
		#print data
		#print sorted_data

	elif num >= 5 and num <= 10:
		#print "remove 1 max and 1 min"
		sorted_data = sorted(data)
		sorted_data.pop()
		del sorted_data[0]
		#print data
		#print sorted_data

	elif num > 10 and num <= 15:
		#print "remove 2 max and 2 min"
		sorted_data = sorted(data)
		sorted_data.pop()
		sorted_data.pop()
		del sorted_data[0]
		del sorted_data[0]
		#print data
		#print sorted_data

	elif num > 15 and num <= 20:
		#print "remove 3 max and 3 min"
		sorted_data = sorted(data)
		sorted_data.pop()
		sorted_data.pop()
		sorted_data.pop()
		del sorted_data[0]
		del sorted_data[0]
		del sorted_data[0]
		#print data
		#print sorted_data

	elif num > 20 and num <= 25:
		#print "remove 4 max and 4 min"
		sorted_data = sorted(data)
		sorted_data.pop()
		sorted_data.pop()
		sorted_data.pop()
		sorted_data.pop()
		del sorted_data[0]
		del sorted_data[0]
		del sorted_data[0]
		del sorted_data[0]
		#print data
		#print sorted_data

	elif num > 25 and num <= 30:
		#print "remove 5 max and 5 min"
		sorted_data = sorted(data)
		sorted_data.pop()
		sorted_data.pop()
		sorted_data.pop()
		sorted_data.pop()
		sorted_data.pop()
		del sorted_data[0]
		del sorted_data[0]
		del sorted_data[0]
		del sorted_data[0]
		del sorted_data[0]
		#print data
		#print sorted_data

	tmp_total_price = 0
	for i in sorted_data:
		tmp_total_price += i

	#print "Company num (", len(data), ") -> (" , len(sorted_data), ")"
	return  tmp_total_price / len(sorted_data)


# depend on get_total_price()
#TODO: we can edit k value
def get_evaluate_price(control_price, total_price):
	k = 0.5
	return control_price * k + total_price * (1-k)


#XXX: be careful for int() or round()
def evaluate_one_target_price(target_price, evaluate_price):
	result_score = 0
	base_score = 15
	if target_price == evaluate_price:
		return base_score

	elif target_price > evaluate_price:  # we report higher
		diff = round ( (target_price - evaluate_price) / (evaluate_price * 0.01) )
		#print "diff = ", diff
		loss_score = diff

		result_score = base_score - loss_score
		if result_score < 0:
			result_score = 0
		return result_score

	else: # we report lower
		diff = round ((evaluate_price - target_price) / (evaluate_price * 0.01) )
		#print "diff = ", diff

		if diff > 5: # we report lower than 5
			diff -= 5
			loss_score = diff * 2
			result_score = base_score + 5 - loss_score
			if result_score < 0:
				result_score = 0
			return result_score

		else: # diff <= 5
			add_score = diff
			if add_score > 5: # add 5 for most
				add_score = 5
			result_score = base_score + add_score
			return result_score



# Actually best score is 0.95 * evaluate_price
def find_target_value(try_company_data):
	#print "###########################"
	print "Find target value"

	#try_target_price = 0  # our target need to be also in company_data!!
	#try_company_data = [ 89, 90, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 92, 93, 94, 95]
	control_price = 100

	
	total_price = get_total_price(len(try_company_data), try_company_data)
	evaluate_price = get_evaluate_price(control_price, total_price)
	print "Company num = ",  len(try_company_data)
	print "total_price = ", total_price
	print "evaluate_price = ", evaluate_price

	sorted_score = {}
	for pri in try_company_data:
		tmp_eval = evaluate_one_target_price(pri, evaluate_price)
		print "Score for ", pri, " is ", tmp_eval
		#sorted_score[tmp_eval] = pri 
	#sorted_score.sort()
	#print sorted_score[len(sorted_score)-1]





##########################################
# function test

# test evaluate_one_target_price
def test_evaluate_one_target_price():
	for diff in range(-50, 50):
		print CONTROL_PRICE + diff, CONTROL_PRICE, "->", evaluate_one_target_price(CONTROL_PRICE + diff, CONTROL_PRICE)


# test get_total_price
def test_get_total_price():

	all_scores = 0
	all_times = 200000
	for test_times in range(0, all_times):
		print '#########################'
		test_data = [ random.randint(88, 91) for i in range(0,  10 + random.randint(0, 10)) ]
		print 'test_data is ', test_data


		total_price_ = get_total_price(len(test_data), test_data)
		print 'total_price is ' , total_price_
		evaluate_price_ = get_evaluate_price(CONTROL_PRICE, total_price_ )
		print "evaluate_price is ", evaluate_price_
		#find_target_value(test_data)
		print "Best sore is ", round( evaluate_price_ * 0.95)

		all_scores += ( evaluate_price_ * 0.95 )

	print "ALL test -> ", all_scores / all_times



##########################################

def test_main():

	#print "###########################"
	#print "test evaluate_one_target_price"
	#test_evaluate_one_target_price()

	print "###########################"
	print "test get_total_price"
	test_get_total_price()




##########################################

if __name__ == '__main__':
	test_main()
	#find_target_value( [ 89, 90, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 92, 93, 94, 95])











