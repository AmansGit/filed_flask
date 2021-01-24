import razorpay 
import json
YOUR_ID = "rzp_test_srE4r5f1lsA7j4"
YOUR_SECRET = "GZsFgEYrq6gVYjM7zuTtPia3"

client = razorpay.Client(auth=(YOUR_ID, YOUR_SECRET))

client.set_app_details({"title" : "flask", "version" : "1.1.2"})

# Create Order
class RazorPay:
	def __init__(self, request_json):
		pass
	def razorOrder(request_json):
		amount = request_json["amount"]
		currency = request_json["currency"]
		receipt = request_json["receipt"]
		
		order_amount = amount
		order_currency = currency
		order_receipt = receipt
		notes = {'Shipping address': 'Bommanahalli, Bangalore'}		# OPTIONAL

		val = client.order.create({
			"amount":order_amount, 
			"currency":'INR', 
			"receipt":order_receipt
		})
		order_id = val["id"]
		pay_id = client.order.payments(order_id)
		
		return val

	# def razorFetchAllOrder():
	# 	count = 2
	# 	skip = 1
	# 	resp = client.order.fetch_all()
	# 	return resp