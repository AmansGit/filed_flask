import requests as request

sandbox_acc = "sb-owqcv4838057@business.example.com"
CLIENT_ID = "AbsPM7v5uJHlZTBLAAq1JuKgAN9BDgrwh4xue0risChCmZHm64H4DNu6ok7kimp20knL2wSDaPCB6idh"
SECRET_ID = "EOaKy_Er2DgBxie3LSaymP6kpjue8mWNli2XMhQgW0nni7xdYu-uwp__zqI5GANEMZVSokZLyYUHyW2A"

api_call = request.get("https://api-m.sandbox.paypal.com")
print(api_call)


def paypalGateway():
	pass