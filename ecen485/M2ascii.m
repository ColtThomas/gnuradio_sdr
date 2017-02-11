function [ y ] = M2ascii( x,M )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
if any(x) > M
    error('input vector contains values larger than M-1')
elseif any(x) < 0
    error('no negative numbers permitted')
else
Nbit = log2(M);

a = dec2bin(x,Nbit).';  % you have to convert the decimal value to binary, but let Nbit tell how many bits to represent the data (avoid 0000000101, etc)
b = reshape(a,1,[]) - '0';
NB = 7*floor(length(b)/7);
c=b(1:NB);
y = bintoascii(c);
end

