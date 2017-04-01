import numpy
from gnuradio import gr

class pn_correlator(gr.basic_block):
    """
    docstring for block pn_correlator
    """

    pnLength = 0
    pnBits = 0
    pnPolynomial = (0)
    def __init__(self,bits,polynomial):
        gr.basic_block.__init__(self,
            name="pn_correlator",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
        self.pnBits = bits
        self.pnLength = pow(2,self.pnBits)-1
        self.pnPolynomial = numpy.zeros(bits+1)
        # this takes an int and puts it into a binary array
        temp = bin(polynomial)[::-1] #char array of binary.
        print "iterating from 0 to ",len(temp), " for ",temp
        for i in range(0,len(temp)):
            if(temp[i]=='1'):
                self.pnPolynomial[i]=1

        #fancy way of turning an int into a binary number in array format
        # self.pnPolynomial = [int(polynomial) for polynomial in bin(8)[2:]]
        print "bits: ",self.pnBits," length: ",self.pnLength, " polynomial: ",self.pnPolynomial

        self.set_history(self.pnLength) # setting history to 1, means 0 history

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items;
            # if(ninput_items_required[i]<1):
            #     ninput_items_required[i]=1;
            # print "------------------------------------------"
            # print "input items required: ",ninput_items_required[i]
            # print "output items required: ",noutput_items
            # print "------------------------------------------"

    def getPN(self):
        # Generates the maximal-length shift register
        # sequence based on X^7 + X^6 + 1
        # See "Linear Feedback Shift Register" in Wikipedia

        # for a pn of 7 bits, period of 127
        # pn = numpy.zeros(127)
        # STATE = numpy.zeros(7)
        # STATE[0] = 1
        #
        # for idx in range(0,126):
        #
        #     ### generate output
        #     pn[idx] = STATE[0]
        #
        #     # update states
        #     STATE[0] = STATE[1]
        #     STATE[1] = STATE[2]
        #     STATE[2] = STATE[3]
        #     STATE[3] = STATE[4]
        #     STATE[4] = STATE[5]
        #     STATE[5] = (STATE[6]+pn[idx])%2 # basically acts as an xor
        #     STATE[6] = pn[idx]
        #     # print STATE
        #

        # pn = numpy.zeros(7);
        # STATE = numpy.zeros(3);
        # STATE[0] = 1;
        # for idx in range(0,6):
        #     pn[idx] = STATE[0];
        #
        #     # update states
        #     STATE[0] = STATE[1]
        #     STATE[1] = (STATE[2] + pn[idx])%2
        #     STATE[2] =pn[idx]

        pn = numpy.zeros(self.pnLength)
        STATE = numpy.zeros(self.pnBits)

        STATE[0] = 1;
        for idx in range(0,self.pnLength-1):
            pn[idx] = STATE[0]
            #update the states
            for k in range(1,len(self.pnPolynomial)-1):
                if(self.pnPolynomial[k]==0):
                    STATE[k-1] = STATE[k]
                else:
                    STATE[k-1] = (STATE[k] + pn[idx])%2
            STATE[self.pnBits-1] = pn[idx]

        return pn

    # def sum(self,a,b)

    def general_work(self, input_items, output_items):

        in0 = input_items[0]
        # print "calculate..."
        pn = self.getPN()

        # outputSize = len(in0) + len(pn)-1 # remember pn is a numpy array; get the column count
        # out = numpy.zeros(outputSize)

        abits = 2*in0 - 1 # converts 0 -> -1, 1 -> +1
        apn = 2*pn-1
        # perform an autocorrelation of the input bits with the pn sequence

        # print "pn sequence size: ",len(apn[0:len(apn)+len(abits)-(len(abits)+1)-1:1])
        # print "bits size: ",len(abits[len(abits)+1-len(pn)::1])
        # for idx in range(0,len(pn)-1): # iterate over 126 before totally overlapping the pn sequence
        #     out[idx] = sum(numpy.multiply(abits[0:idx:1],pn[len(pn)-idx::1])) # numpy.multiply is equivalent to .* in matlab
        # for idx in range(len(pn),len(abits)):
        #     out[idx] = sum(numpy.multiply(abits[idx-len(pn):idx:1],apn[::1]))
        # for idx in range(len(abits)+1,len(abits)+len(pn)-1):
        #     out[idx-1] = sum(numpy.multiply(abits[idx-len(pn)::1],apn[0:len(apn)+len(abits)-idx:1]))
        # print "out: ",out
        # for idx in range(0,len(pn)-2):
        #     out[idx] = sum(numpy.multiply(abits(0,idx),pn(end-idx,end)));
        # for idx in range(len(pn)-1,len(bits)):
        #     out[idx] = sum(numpy.multiply(abits(idx-len(pn)+1,idx),apn));
        # for idx in range(len(bits),len(bits)+len(pn)-2):
        #     out[idx] = sum(numpy.multiply(abits(idx-len(pn)+1,end),apn(1,end+len(abits)-idx)));
        # print "PN sequence: ",self.getPN()

        # out[:] = numpy.convolve(apn[::-1],abits)
        # print out[0:30:1]
        # consume(0, len(input_items[0]))

        # method 1 - simple convolution
        out = numpy.convolve(abits,apn[::-1])

        # method 2 - check the input to the pn code
        # for idx in range(0,len(pn)-1):
        #     if(in0(idx)==pn(idx)):
        #         temp = temp+1
        #     else:
        #         temp = temp-1
        # out[idxOut]=temp

        # print "Size of the input: ",len(in0)
        # print "Size of the output: ",len(out)
        # print "Size of the expected output: ",len(output_items[0])
        # print "First: ",out[0]," Last: ",out[len(output_items[0])]
        output_items[0][:] = out[0:len(output_items[0])]
        self.consume_each(len(output_items[0]))
        return len(output_items[0])
