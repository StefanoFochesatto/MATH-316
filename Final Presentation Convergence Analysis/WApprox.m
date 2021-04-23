function [hist, p] = WApprox(n)
%This function takes a number of iterations n, and returns 
%every approximation to pi from the Wallis Product up to n iterations. 
hist = [];
p = 2;
for i = 1:n
    p = p*((4*i^2)/((4*i^2) - 1));
    hist = [hist; p];
end