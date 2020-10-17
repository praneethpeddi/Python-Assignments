"""Program to convert a string to a dictionary"""


def create_dictionary(inputs):
    """This function converts a string to a Dictionary"""
    converted_dict = {}
    outputs = inputs.split(' ', 1)
    converted_dict[outputs[0]] = outputs[1]
    print(converted_dict)


def main():
    """This function contains the function that are being called to do some task"""
    string = r"""EDFFX2AD \dat_out_sig_reg[0]  ( .D(N69), .E(N96), .CK(clk), .Q(dat_out[0]));"""
    create_dictionary(string)


if __name__ == '__main__':
    main()
