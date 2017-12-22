h3 = [-0.5 -1 0 1 0.5];
h4 = [-1 0.5 -0.5 1];
h3mag = 0;
h4mag = 0;
omega = 0.5;
% for idx = 1:1:5
%     h3mag = h3mag + h3(idx)*real(exp(-1j*omega*(idx-1)*pi))
%     h4mag = h4mag + h4(idx)*real(exp(-1j*omega*(idx-1)*pi))
% end

norm(h3mag)
norm(h4mag)


N = 1024;
width = 2;
F = -width/2:width/N:width/2-1/N;
grid on
figure(999)
plot(F,(abs(fft(h3,1024))))
figure(1337)
plot(F,(abs(fft(h4,1024))))