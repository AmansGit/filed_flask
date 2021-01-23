from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
from services.razorpay import RazorPay
from services.paypal import paypalGateway

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
db = SQLAlchemy(app)



class CreditCardDetails(db.Model):
	__tablename__ = 'transaction details'
	transact_id =	db.Column(db.Integer, primary_key=True)
	order_id = 		db.Column(db.Integer)
	full_name = 	db.Column(db.String(50), unique=False, nullable=False)
	number = 		db.Column(db.Integer ,unique=True, nullable=False)
	expire_date = 	db.Column(db.DateTime, nullable= False)
	sec_code = 		db.Column(db.Integer, nullable=False)
	# current_date = 	datetime.now()
	
	# if current_date > expire_date:
	# 	error_msg = "Expired credit card"
	# else:
	# 	error_msg = "Success"
	amount = db.Column(db.Integer, nullable= False)


	# def __repr__(self):
	# 	return f"Credit card owner:{full_name} with card number: {number} and {expire_date}"

# NOTE: it contains data recieved from payment gatways integration
# class PaymentGatewayAPILog(db.Model):
# 	__tablename__ = 'payment gateway log'


@app.route('/processPayment', methods=['POST'])
def paymentGateways():
	data = []
	status, err_msg = validate(request.get_json())
	# try:
	if status:
		request_json = request.get_json()

		name = request_json["full_name"]
		number = request_json["number"]
		expire_date = request_json["expire_date"]
		cvv = request_json["sec_code"]
		amount = request_json["amount"]
		print("amamamamamama:::::", type(amount))

		if amount < 2000:
			rzp = RazorPay.razorOrder(request_json)	#CheapPaymentGateway
			print("RZP:: ",rzp["id"])
			pay_id = RazorPay.razorPayment(rzp["id"])
			response_code = 200


		# elif amount > 20 and amount <= 500:
		# 	pypl = paypalGateway()			#ExpensivePaymentGateway

		# elif amount > 500:
		# 									#PremiumPaymentGateway

	else:
		response_code = 500

	# except Exception as e:
	# 	response_code = 500

	response = {
			"STATUS": str(response_code),
			"ERR_MSG": err_msg,
			"DATA": rzp
	}
	return jsonify(response)


	


def validate(request_json):
	err_msg = ""
	status = True
	if 'full_name' not in request.get_json():
		err_msg += "full_name not in body "
		status = False
	if 'number' not in request.get_json():
		err_msg += "number not in body"
		status = False
	if 'expire_date' not in request.get_json():
		err_msg += " expire_date not in body"
		status = False
	if 'sec_code' not in request.get_json():
		err_msg += " sec_code not in body"
		status = False
	if 'amount' not in request.get_json():
		err_msg = "amount not in body"
		status = False
	return status, err_msg


if __name__ == '__main__':
	app.run(debug = True, port=5000)