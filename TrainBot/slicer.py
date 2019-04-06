def show_balances(daily_balances):
	for day in range(-3, -1):
		balance_slice = daily_balances[day:day+2]

		print("slice for day {} {}".format(abs(day), balance_slice))
		