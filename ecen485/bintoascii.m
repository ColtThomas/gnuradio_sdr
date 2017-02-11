function [ y ] = bintoascii( x )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
NChar = length(x)/7; % 7 bits 

xo = reshape(x,7,[]); %reshape x into rows of length 7
c = zeros(NChar,1); % initialize storage of characters

% pseudocode
% loop through # characters 
for n=1:NChar
sp = sprintf('%i' , xo(:,n)) ;   % turn each row into a string. Can also do '5' - '0' to get integer 5
c(n) = bin2dec(sp);     %turns the binary into decimal
y=char(c).';
end

end

