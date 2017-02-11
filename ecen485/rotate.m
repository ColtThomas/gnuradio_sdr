function [Out] = rotate(In )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
Out = In;
for n=1:size(In,2)
    switch In(n)
        case 0
            Out(n) = 1;
        case 1 
            Out(n) = 3;
        case 2
            Out(n) = 0;
        case 3
            Out(n) = 2;
        otherwise 
    end
end

end

