
%	Mid-point algorithm


k = 100;

cp = 1:k;	% check points
in = ones(1,k); % intervals
A = cp;
B = in;
C = 1;
for l = 1:100*k
	sumin = ([B(l,:) 0] + [0 B(l,:)])(2:k-1);	% lengths of neighbouring intervals added together
	index = find(logical(sumin == min(sumin)))(1);	% index is the first time when I_i + I_{i+1} is minimal
	newin = [B(l,1:index-1) B(l,index)+B(l,index+1) B(l,index+2 : k) 0];	% create new intervals
	newcp = [A(l,1:index-1) A(l,index+1 : k) 0];	% create new check points
	newcp(k) = newcp(k-1) + (max([max(newin(1:index-1)) max(newin((index+1):k))]) + newin(index))*0.5;	% set the 
	newin(k) = newcp(k) - newcp(k-1);
	
	
	A = [A; newcp];	% keeping track of checkpoint positionings
	B = [B; newin];	% keeping track of interval lengths
	
	if(l>1)
		C = [C; max([B(l-1,:), newin(k)])/newcp(k)*(k+1)];	% keeping track of the measure
	end
end

plot(C);
