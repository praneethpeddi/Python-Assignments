import pytest
import re


def is_valid_email(email_to_verify):
	if re.match("^[a-zA-Z0-9_+&*<>-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email_to_verify) is not None:
		return True
	else:
		return False


data_to_verify = [
					{"data" : 'praneeth..peddi@gmail.com', 	"exp_result" : False},
					{"data" : 'praneeth+peddi@gmail.com', 	"exp_result" : True},
					{"data" : 'peddi@yahoo.co', 			"exp_result" : True},
					{"data" : '-abc@gmail', 				"exp_result" : False},
					{"data" : 'praneeth@gmail-com',		 	"exp_result" : False},
					{"data" : 'xyz@@gmail.com.', 			"exp_result" : False},
					{"data" : 'abc-123@hello.com', 			"exp_result" : True},
					{"data" : 'abc-xyz@hello.co.in786fgf', 	"exp_result" : False},
					{"data" : '1Abc@gmail.com', 			"exp_result" : True},
					{"data" : 'abc<xyz@gmail.com', 			"exp_result" : True},
					{"data" : 'praneeth-peddi@gmail.com', 	"exp_result" : True},
				]

@pytest.mark.parametrize("email", data_to_verify)
def test_is_valid_email(email):
    actual_value = is_valid_email(email["data"])
    assert actual_value == email["exp_result"], f"return value from the function 'is_valid_email' is {actual_value}', expected : {email['exp_result']}"