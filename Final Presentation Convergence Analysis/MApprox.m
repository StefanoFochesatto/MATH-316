function [hist, p] = MApprox(n)
%This function takes a number of iterations n, and returns 
%every approximation to pi from the Machin formula up to n iterations.
hist = [];
p = 0;
for i = 0:n-1
    p = p + 4*(4*((((-1)^i)*(1/5)^(2*i+1))/(2*i + 1)) - ((((-1)^i)*(1/239)^(2*i+1))/(2*i + 1))) ;
    hist = [hist; p];
end