import logging


class Validator:
	# def __init__(self,)

	def validate_process_payment_json(self, request_json):
		self.logger.info("Validating payment JSON")
		status = True
		err_msg = ""

		if "name" not in request_json:
			err_msg += " 'name' key is missing"
			status = False
		if "number" not in request_json:
			err_msg += " 'number' key is missing"
			status = False
		if "expire_date" not in request_json:
			err_msg += " 'expire_date' key is missing"
			status = False
		if "cvv" not in request_json:
			err_msg += " 'cvv' key is missing"
			status = False

		return status, err_msg