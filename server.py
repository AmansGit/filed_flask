from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
from services.services_processor import PaymentGateway
from services.validation_services import Validations

app = Flask(__name__)

app.config['SECRET_KEY'] = '1$\x9c\xce\xael\x1f,\x92\xabz\xc8\x82x\xbc\xfd'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class CreditCardDetails(db.Model):
	__tablename__ = 'Credit card details'
	transact_id =	db.Column(db.Integer, primary_key=True)
	order_id = 		db.Column(db.String(50))
	full_name = 	db.Column(db.String(50), nullable=False)
	number = 		db.Column(db.Integer ,unique=True, nullable=False)
	expire_date = 	db.Column(db.String(10), nullable= False)
	sec_code = 		db.Column(db.Integer, nullable=False)
	amount = 		db.Column(db.Integer, nullable= False)


	def __repr__(self):
		return f"Credit card owner:{full_name} with card number: {number} and {expire_date}"

"""
	Below code is for creating orders using 'Razorpay' which works succesfully and able to create orders, 
				but not able to get payment_id and thats the reason why I'm not able to create payment link.
	So, for this reason, I created three functions as mentioned in the task doc adn through that I just created
		order_id and response as asked.

"""
# @app.route('/processPayment', methods=['POST'])
# def paymentGateways():
# 	data = []
# 	status, err_msg = validate(request.get_json())
# 	# try:
# 	if status:
# 		request_json = request.get_json()

		# name = request_json["full_name"]
		# number = request_json["number"]
		# expire_date = request_json["expire_date"]
		# cvv = request_json["sec_code"]
		# amount = request_json["amount"]
# 		print("amamamamamama:::::", type(amount))

# 		if amount < 2000:
# 			rzp = RazorPay.razorOrder(request_json)	#CheapPaymentGateway
# 			print("RZP:: ",rzp["id"])
# 			pay_id = RazorPay.razorPayment(rzp["id"])
# 			response_code = 200


# 		# elif amount > 20 and amount <= 500:
# 		# 	pypl = paypalGateway()			#ExpensivePaymentGateway

# 		# elif amount > 500:
# 		# 									#PremiumPaymentGateway

# 	else:
# 		response_code = 500

# 	# except Exception as e:
# 	# 	response_code = 500

# 	response = {
# 			"STATUS": str(response_code),
# 			"ERR_MSG": err_msg,
# 			"DATA": rzp
# 	}
# 	return jsonify(response)

@app.route('/processPayment', methods=['POST'])
def ProcessPayment():
	result = None
	data = []
	err_msg = ""
	request_json = request.get_json()

	# Validation to check all the required data(s) are present or not	
	valid_status, valid_err_msg = Validations.validate(request_json)
	if valid_status:
		name = request_json["full_name"]
		number = request_json["number"]
		expire_date = request_json["expire_date"]
		cvv = request_json["sec_code"]
		amount = request_json["amount"]
		payment_type = None
		if amount <= 0:
			err_msg = "Invalid amount, please try again"
		else:
			if amount <= 20:
				result, status = PaymentGateway.CheapPaymentGateway(request_json)
				payment_type = 'CheapPaymentGateway'

			if amount > 20 and amount <= 500:
				result, status = PaymentGateway.ExpensivePaymentGateway(request_json)
				payment_type = 'ExpensivePaymentGateway'

			if amount > 500:
				result, status = PaymentGateway.PremiumPaymentGateway(request_json)
				payment_type = 'PremiumPaymentGateway'
			
			err_msg = "Successful"
			try:
				payment = CreditCardDetails(order_id= result["id"], full_name=name, 
							number=number, expire_date=expire_date,	sec_code=cvv, amount=amount)
				db.session.add(payment)
				db.session.commit()
			except Exception as e:
				pass	
	else:
		response_code = 400

	if status:
		response_code = 200
	else:
		response_code = 500
	response = {
		"STATUS": response_code,
		"ERR_MSG": err_msg,
		"DATA": result
	}
		
	return jsonify(response)
	


if __name__ == '__main__':
	
	db.init_app(app)
	app.run(debug = True, port=5000)