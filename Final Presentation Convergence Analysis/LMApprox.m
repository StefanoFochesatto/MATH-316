function [hist, p] = LMApprox(n)
%This function takes a number of iterations n, and returns 
%every approximation to pi from the Leibniz\Madhava series up to n iterations. 
hist = [];
p = 0;
for i = 0:n-1
    p = p + 4*(((-1)^i)/(2*i + 1));
    hist = [hist; p];
end