import razorpay 
import json
YOUR_ID = "rzp_test_srE4r5f1lsA7j4"
YOUR_SECRET = "GZsFgEYrq6gVYjM7zuTtPia3"

client = razorpay.Client(auth=(YOUR_ID, YOUR_SECRET))

client.set_app_details({"title" : "flask", "version" : "1.1.2"})

# Create Order
class RazorPay:
	def __init__(self, request_json):
		# name = self.request_json["full_name"]
		# number = self.request_json["number"]
		# expire_date = self.request_json["expire_date"]
		# cvv = self.request_json["sec_code"]
		# amount = self.request_json["amount"]
		# currency = self.request_json["currency"]
		# receipt = self.request_json["receipt"]
		pass
	def razorOrder(request_json):
		amount = request_json["amount"]

		currency = request_json["currency"]
		receipt = request_json["receipt"]
		# payment_capture = request_json["payment_capture"]


		print("AMOUNT::", amount)
		order_amount = amount
		# print("order_amount::::::",type(json.dumps(order_amount)))
		order_currency = currency
		print(currency)
		order_receipt = receipt
		notes = {'Shipping address': 'Bommanahalli, Bangalore'}		# OPTIONAL
		print("client.order.create: ", dir(client.order.create))
		val = client.order.create({
			"amount":order_amount, 
			"currency":'INR', 
			"receipt":order_receipt
		})
		order_id = val["id"]
		pay_id = client.order.payments(order_id)
		print("payment_id ====", pay_id)
		return val
		# print("val: ", val)
		# print("CLIENT::------>",client)

	# def razorFetchAllOrder():
	# 	count = 2
	# 	skip = 1
	# 	resp = client.order.fetch_all()
	# 	return resp

	def razorPayment(o_id):
		# order_id = self.o_id
		print("ORDER_ID:: ",o_id)
		# client.payment.capture(payment_id, amount, data={})




	# def razorPayment():
	# 	payment_id = "pay_29QQoUBi66xm2f"

	# 	payment_amount = 1000
	# 	payment_currency = "INR"
	# 	resp = client.payment.capture(payment_id, payment_amount, {"currency":"payment_currency"})