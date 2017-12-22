% homework 10

% lab 1 for 487
clear all; close all;
%%%%%%%%%%
% part 1 %
%%%%%%%%%%

%sampFreq = 48000; % sampling frequency of our microphone
sampFreq = 16800; %


F0 = 2000; % center frequency
passBandWidth = 500; % Hz
F_2 = F0 + passBandWidth/2;
F_1 = F0 - passBandWidth/2
% transitionBandWidth = 500; % Hz
% Fp = F0 + passBandWidth / 2; % passband frequency point
% Fs = Fp + transitionBandWidth; % stopband frequency point
% A = 41; % attenuation for our desired window (Hamming)
% 
% % convert to radians per second
% W0 = 2*pi*F0/sampFreq;
% Wp = 2*pi*Fp/sampFreq;
% Ws = 2*pi*Fs/sampFreq;
passBandWidthW = passBandWidth*2*pi/sampFreq;
w2 = F_2*2*pi/sampFreq;
w1 = F_1*2*pi/sampFreq;

% We calculate M with the equation for the Hamming Window in Table 7.2, 
% pg.539
M = round(8*pi/passBandWidthW);

% build the low pass filter
N = 1+M % length of the filter itself
L = N/2; % We want to shift this to where the middle sample is at 0
n = (-L:L)'; % This is our sample index

window = hamming(length(n));
figure;
plot(window);
xlabel('Frequency in rad/sample');
ylabel('Hamming Filter Amplitude');

% Ideal impulse response equation
hideal = w2/pi*sinc(w2*(n-M/2)/pi) - w1/pi*sinc(w1*(n-M/2)/pi); % our ideal pulse from eq 1 in handout
figure;
freqz(hideal.*window);





