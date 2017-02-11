%myinit
Eavg = 3;
% Timing loop 
% for zero crossing ted see figure 8.4.7 on pg 456

Kp = 2*2.7*Eavg;
K0=-1;
zeta = .7071;
BnT=0.01;
[K1t K2t] = kfunc(BnT,zeta,Kp,K0); % this will set our K values for our TED PLL

%Phase loop
% for the ML PED Kp=2*Eavg, see figure 7.2.5b on page 373

Kp = 2*Eavg;
K0 = 1;
zeta = .7071;
BnT=0.01;
[K1p K2p] = kfunc(BnT,zeta,Kp,K0); % this will set our K values for our PED PLL