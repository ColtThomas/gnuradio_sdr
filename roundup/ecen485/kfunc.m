function [K1 K2 ] = kfunc(BnT,zeta,Kp,K0 )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

% zeta = .7071;
% Bn=0.01;
% T=1;
theta=(BnT)/(zeta+1/(4*zeta));

K1 = 4*zeta*theta/(1+2*zeta*theta+theta*theta);
K2 = 4 * (theta*theta)/(1+2*zeta*theta+theta*theta);

K1=K1/(K0*Kp);
K2=K2/(K0*Kp);
end

