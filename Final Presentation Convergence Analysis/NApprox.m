function [hist, p] = NApprox(n)
%This function takes a number of iterations n, and returns 
%every approximation to pi from the Newton series up to n iterations. 
hist = [];
p = (3*sqrt(3))/4;
for i = 1:n
    x = 24*(-1*factorial(2*i - 2))/(2^(4*i - 2)*((factorial(i-1))^2)*(2*i - 3)*(2*i + 1));
    p = p + x;
    hist = [hist; p];
end