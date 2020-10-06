def CountNoWords(inputs):
    sub1 = "EDFFX2AD"
    sub2 = "DFFQXLAD"
    print('The count of ' + sub1 + ' is', inputs.count(sub1))
    print('The count of ' + sub2 + ' is', inputs.count(sub2))


if __name__ == '__main__':
    string = """EDFFX2AD \dat_out_sig_reg[0]  ( .D(N69), .E(N96), .CK(clk), .Q(dat_out[0])
         );
  EDFFX2AD \dat_out_sig_reg[1]  ( .D(N70), .E(N94), .CK(clk), .Q(dat_out[1])
         );
  EDFFX2AD \dat_out_sig_reg[2]  ( .D(N71), .E(N92), .CK(clk), .Q(dat_out[2])
         );
  DFFQXLAD \dat_out_sig_reg[8]  ( .D(N77), .CK(clk), .Q(dat_out[8]) );
  DFFQXLAD \dat_out_sig_reg[15]  ( .D(N84), .CK(clk), .Q(dat_out[15]) );
  DFFQXLAD \dat_out_sig_reg[6]  ( .D(N75), .CK(clk), .Q(dat_out[6]) );
  DFFQXLAD \dat_out_sig_reg[11]  ( .D(N80), .CK(clk), .Q(dat_out[11]) );"""
    CountNoWords(string)
