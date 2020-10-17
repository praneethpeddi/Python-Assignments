def check_for_valid_email(email):
    if ('@' not in email) or ('.' not in email):
        return False
    if email.count('@') > 1 or email.count('.') > 2:
        return False
    if ".." in email or ".@" in email or "@." in email or "._." in email:
        return False
    email = email.replace('@', ' ')
    email = email.replace('.', ' ')
    email_split = email.split()
    if len(email_split) < 3:
        return False
    for i in email_split[0]:
        if not i.isalnum() and i != '_' and i != '-':
            return False
    for i in email_split[1]:
        if not i.isalnum():
            return False
    if len(email_split[2]) > 3 or len(email_split[2]) == 0:
        return False
    return True


def test_validate_email(input):
    for i in input:
        actual_res = check_for_valid_email(i["data"])
        if actual_res == i["exp_result"]:
            print('valid')
        else:
            print("not valid")


def main():
    data_to_verify = [{"data": 'p+eddi@gm.ail', 		"exp_result": True},
                      {"data": 'xyz@yahoo.com', 		"exp_result": True},
                      {"data": 'abc-@hello.co', 		"exp_result": False},
                      {"data": '--abc-123@hello.com', 	"exp_result": False}]
    test_validate_email(data_to_verify)


if __name__ == "__main__":
    main()
