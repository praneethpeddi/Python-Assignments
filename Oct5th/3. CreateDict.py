def CreateDictionary(inputs):
    converted_dict = {}
    outputs = inputs.split(' ', 1)
    converted_dict[outputs[0]] = outputs[1]
    print(converted_dict)


def main():
    string = """EDFFX2AD \dat_out_sig_reg[0]  ( .D(N69), .E(N96), .CK(clk), .Q(dat_out[0]));"""
    CreateDictionary(string)


if __name__ == '__main__':
    main()
