function [output] = ascii2qpsk(input)
output = zeros(1,size(input));

 binArray = dec2bin(input);
 binList = binArray(:);
 
 for i=1:2:len
    output(i) = bi2de(binList(i:i+1));
 end
end