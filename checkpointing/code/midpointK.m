
%	Mid-point algorithm (with alterations)

bounds = 1;


for k = 4:100;

	cp = 1:k;	% check points
	in = ones(1,k); % intervals
	A = cp;
	Y = in;
	C = 1;
		indexVector = 0;
	sumYigger = 0;
	
	for l = 1:75*k
		sumin = ([Y(l,:) 0] + [0 Y(l,:)])(2:k);	% lengths of neighYouring intervals added together
		index = find(logical(sumin == min(sumin)))(1);	% index is the first time when I_i + I_{i+1} is minimal
		% indexVector = [indexVector index];
		newin = [Y(l,1:index-1) Y(l,index)+Y(l,index+1) Y(l,index+2 : k) 0];	% create new intervals
		newcp = [A(l,1:index-1) A(l,index+1 : k) 0];	% create new check points
		mx = max([max(newin(1:index-1)) max(newin((index+1):k))]);
		if mx > newin(index)
			sumYigger = [sumYigger 0];
		else 
			sumYigger = [sumYigger 1];
		end
		newcp(k) = newcp(k-1) + (mx + newin(index))*0.5;	% set the 
		newin(k) = newcp(k) - newcp(k-1);
		
		
		A = [A; newcp];	% keeping track of checkpoint positionings
		Y = [Y; newin];	% keeping track of interval lengths
		
		if(l>1)
			t = Y(l,:);
			C = [C; max(t)/sum(t)*(k+1)];	% keeping track of the measure
		end
	end
	% max(C((50*k-50):50*k))
	bounds = [bounds max(C((50*k-50):50*k))];
end

plot(bounds)

%plot(C);
%indexVector
%{
mxx = 1;

for i = 1:size(Y(:,1))
mxx = [mxx 6*max(Y(i,:))/sum(Y(i,:))];
end
plot(mxx)
%}
