"""Program to count the number of times the sub string is present"""


def count_substring(inputs):
    """Counts the number the words"""
    sub1 = "EDFFX2AD"
    sub2 = "DFFQXLAD"
    count1 = inputs.count(sub1)
    count2 = inputs.count(sub2)
    print(f'The count of {sub1} is {count1}')
    print(f'The count of {sub2} is {count2}')


def main():
    """Function is being called in this function main"""
    data = r"""EDFFX2AD \dat_out_sig_reg[0]  ( .D(N69), .E(N96), .CK(clk), .Q(dat_out[0])
            );
            EDFFX2AD \dat_out_sig_reg[1]  ( .D(N70), .E(N94), .CK(clk), .Q(dat_out[1])
            );
            EDFFX2AD \dat_out_sig_reg[2]  ( .D(N71), .E(N92), .CK(clk), .Q(dat_out[2])
            );
            DFFQXLAD \dat_out_sig_reg[8]  ( .D(N77), .CK(clk), .Q(dat_out[8]) );
            DFFQXLAD \dat_out_sig_reg[15]  ( .D(N84), .CK(clk), .Q(dat_out[15]) );
            DFFQXLAD \dat_out_sig_reg[6]  ( .D(N75), .CK(clk), .Q(dat_out[6]) );
            DFFQXLAD \dat_out_sig_reg[11]  ( .D(N80), .CK(clk), .Q(dat_out[11]) );"""
    count_substring(data)


if __name__ == '__main__':
    main()
