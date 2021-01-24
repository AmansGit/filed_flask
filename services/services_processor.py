import uuid

class PaymentGateway:
	def __init__(self):
		pass
	# THree payment Gateways:
	def CheapPaymentGateway(request_json):

		amount = request_json["amount"]
		status_code = True
		response = {
			"id": "cpg-" + str(uuid.uuid4()),
			"entity": "cheapOrder",
			"amount": amount
		}
		print("CHEAP::", response)
		return response, status

	def ExpensivePaymentGateway(request_json):
		amount = request_json["amount"]
		status_code = True
		response = {
			"id": "epg-" + str(uuid.uuid4()),
			"entity": "expensiveOrder",
			"amount": amount
		}
		return response, status_code

	def PremiumPaymentGateway(request_json):
		amount = request_json["amount"]
		status_code = True
		response = {
			"id": "ppg-" + str(uuid.uuid4()),
			"entity": "premiumOrder",
			"amount": amount
		}
		return response, status_code	
