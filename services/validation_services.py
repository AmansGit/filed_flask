from datetime import datetime

class Validations:
	def __init__(self):
		pass
	def validate(request_json):
		err_msg = ""
		status = True
		if 'full_name' not in request_json or not request_json['full_name']:
			err_msg += "full_name not in body "
			status = False
		if 'number' not in request_json or not request_json['number'] or len(str(request_json['number'])) != 16:
			err_msg += " number not in body"
			status = False
		if 'expire_date' not in request_json or not request_json['expire_date']:
			err_msg += " expire_date not in body"
			status = False
	# Validation for expire Date::		
		else:
			status = True
			current_date = datetime.now()
			current_month, current_year = current_date.month, current_date.year
			month, year = request_json['expire_date'].split("/")

			if(len(str(year)) == 4):
				if(int(year) == current_year):
					if(int(month) > 12 or int(month) < current_month):
						status = False
				elif(int(year) < current_year):
					status = False
			else:
				status = False
			if(not status):
				err_msg += " Date Expired"
		
		if 'sec_code' not in request_json:
			err_msg += " sec_code not in body"
			status = False
		
		if 'amount' not in request_json:
			err_msg = "amount not in body"
			status = False

		err_msg = err_msg.lstrip().rstrip()		# To strip left and right whitespaces
		return status, err_msg