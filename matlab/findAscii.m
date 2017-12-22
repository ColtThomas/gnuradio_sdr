function [y] = findAscii(x,str)
% pass in a character array str to find it in vector x
temp = asciitobin(str);
y = strfind(x,temp);

end