x = [1 0 0 0 0 1 0 1 0 1 1 0 0 1 1 0 1 0 1 0 1];
bintoascii(x);
x = [2 0 1 1 1 2 1 2 2 2 2];
M = 4;
M2ascii(x,M)
% Nbit = log2(M)
% 
% a = dec2bin(x,Nbit).'
% b = reshape(a,1,[]) - '0'
% NB = 7*floor(length(b)/7)
% c=b(1:NB)
% y = bintoascii(c);