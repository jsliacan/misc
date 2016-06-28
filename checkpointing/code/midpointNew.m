
%	Mid-point algorithm being tested for periods in indices of intervals that are merged... 

k = 128;
cp = 1:k;	% check points
in = ones(1,k); % intervals
A = cp;
Y = in;
C = 1;
indexVector = 0;

sumYigger = 0;

for l = 1:50*k
	sumin = ([Y(l,:) 0] + [0 Y(l,:)])(2:k);	% lengths of neighYouring intervals added together
	index = find(logical(sumin == min(sumin)))(1);	% index is the first time when I_i + I_{i+1} is minimal
	indexVector = [indexVector index];
	newin = [Y(l,1:index-1) Y(l,index)+Y(l,index+1) Y(l,index+2 : k) 0];	% create new intervals
	newcp = [A(l,1:index-1) A(l,index+1 : k) 0];	% create new check points
	mx = max([max(newin(1:index-1)) max(newin((index+1):k))]);
	if mx > newin(index)
		sumYigger = [sumYigger 0];
	else 
		sumYigger = [sumYigger 1];
	end
	newcp(k) = newcp(k-1) + (mx + newin(index))*1/2;	% set the 
	newin(k) = newcp(k) - newcp(k-1);
	
	
	A = [A; newcp];	% keeping track of checkpoint positionings
	Y = [Y; newin];	% keeping track of interval lengths
	
	if(l>1)
		t = Y(l,:);
		C = [C; max(t)/sum(t)*(k+1)];	% keeping track of the measure
	end
end

ind = find(indexVector == 1);

z = indexVector(ind(end-1):(ind(end)-1))


%{
mm = max(Y(ind(end),:));
mi = min(Y(ind(end),:));
y = (mm - mi)/k
y = y/sum(Y(ind(end)))
%}
y = 0;
for i = 1:size(Y,1)
	y = [y (max(Y(ind(end),:)) - min(Y(ind(end),:)))/sum(Y(ind(end),:))];
end

vv = 0;
for j = 1: size(ind,2)
	if(j < size(ind,2))
		vv = [vv sum(Y(ind(j+1),:))/sum(Y(ind(j),:))];
	end
end

y(20:25)
plot(y)

%{
clf	% clear figure window
plot(C)
%}

%{
plot(C)
hold on 
plot(ones(1,50*k)*sqrt(2))
plot(ones(1,50*k)*1.5)
hold off
%}


%{
subplot(3,1,1)
hold on
j = 1;
for i = (50*k-43):(50*k-40)
	subplot(4,1,j)
	plot(Y(i,:)/sum(Y(i,:))*(k+1));
	j = j+1;
end
hold off
%}
%{
subplot(3,1,2)
plot(Y(50*k-43,:)/sum(Y(50*k-43,:))*(k+1));

subplot(3,1,3)
plot(Y(50*k-42,:)/sum(Y(50*k-42,:))*(k+1));
%}
%plot(Y(l-5,:)/sum(Y(l-5,:))*(k+1))

%{
for i = 1:30
	h = Y(l-i,:)/sum(Y(l-i,:))*(k+1);
	subplot(6,5,i)
	plot(h)
end
%}


