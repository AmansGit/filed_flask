Test_Merchant_ID = "EUaDzL49823769709188"
Test_Merchant_Key = "3pEcI4RLMTlISrJd"
transaction_url = "https://securegw-stage.paytm.in/order/process"


# For Staging 
environment = LibraryConstants.STAGING_ENVIRONMENT

# For Production 
# environment = LibraryConstants.PRODUCTION_ENVIRONMENT

# Find your mid, key, website in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
mid = "Test_Merchant_ID"
key = "Test_Merchant_Key"
website = "WEBSTAGING"
# client_id = "YOUR_CLIENT_ID_HERE"

callbackUrl = "MERCANT_CALLBACK_URL"
MerchantProperty.set_callback_url(callbackUrl)

MerchantProperty.initialize(environment, mid, key, client_id, website)
 # If you want to add log file to your project, use below code
file_path = '/path/log/file.log'
mode = "w"
handler = logging.FileHandler(file_path, mode)
formatter = logging.Formatter("%(name)s: %(levelname)s: %(message)s")
handler.setFormatter(formatter)
MerchantProperty.set_log_handler(handler)
MerchantProperty.set_logging_disable(False)
MerchantProperty.set_logging_level(logging.DEBUG)