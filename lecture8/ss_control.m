% generate random space-state systems
s1 = rss(3, 1, 2);  % 3 states, 1 output, 2 inputs
s2 = rss(2, 3, 1);  % 2 states, 3 outputs, 1 input

% systems in series
stotal = s2 * s1;  % connect the states in series, # outputs1 = # inputs2
% in series, our states will add together (5 total states), input =
% #inputs1 (2 inputs) and outputs = #outputs2 (3 outputs)
% size(stotal)  % says how many outputs, inputs, and states the system has

% systems in parallel
s1 = rss(3, 1, 2);
s2 = rss(2, 1, 2);
stotal = s1 + s2;  % just like irl we simply add systems if in parallel

% feedback loops
% help feedback  % this will print the feedback documentation
a = [0 1 0
    -0.0071 -0.111 0.12
    0 0.07 -0.3];

b = [0
    -0.095
    0.072];

c = [1 0 0
    0 1 0
    0 0 1
    1 0 -1];

d = zeros(4, 1);  % matrix of size 4x1 of zeros (4 rows, 1 col)

sys2 = ss(a,b,c,d);  % creating a state-space system with matrices abcd
% since the matrices A and C have 3 columns, then we must have 3 states
% matrices B and D have 1 column so 1 input
% matrix C and D have 4 rows so 4 outputs

k = [0 -0.67 0 0];  % creating a gain matrix 
% we want to feed sys2 back into itself so that means the outputs then go
% back and become inputs
% with the gain matrix we say which outputs we want to feed back in, in
% this case we only want to feed back in y2 witha gain of -0.67

sclosed = feedback(sys2, k);
% with the feedback loop element x2x2 of A and x2x3 of A were changed
% because we're feedbacking back in y2 (changing the input u)
% WITHOUT FEEDBACK: input u
% WITH FEEDBACK: input -Ky (gain matrix * output vector) --> here that's
% -0.67y2 so only the dynamics of STATE 2 x2 are changed 

% inspecting the systems
% for a transfer function H(s) we can look at its poles (roots of
% denominator)
% for a ss system, the poles are the eigenvalues of matrix A 
% poles must have negative real values for system to be stable

eig(sys2.A);  % getting the eigenvalues of the A matrix of sys2
eig(sclosed.A);
% if an eigenvalue is +0.0000i then its real (no complex component)
% complex eigenvalues ALWAYS come in conjugate pairs a + bi and a - bi
% complex poles dominate osciallatory behaviour 


% question 1 -- yaw response of an aircraft
% states are [beta, phi, p, r] where beta is the side slip angle, phi is
% the roll angle, p is the roll rate and r is the yaw rate
% input vector u is [da dr] for deflection of aileron and deflection of
% rudder
A = [-0.2 0.06 0 -1
    0 0 1 0
    -17 0 -3.8 1
    9.4 0 -0.4 -0.6];
B = [-0.01 0.06
    0 0 
    -32 5.4
    2.6 -7];
% want to find response of the yaw rate to a unit step input in rudder and
% determine the vlaue of the yaw rate in the first peak

% since we only have the rudder input dr then we're only interested in the
% second column of b (no aileron input)
B = B(:,2);  % all rows, second column since only 1 input

% only interested in finding yaw rate r, the 4th state --> this is the
% output so y = r
% since only 1 output, then y is a vector with one value
% C should have 4 columns (state vector) and 1 row (output vector)
C = [0 0 0 1];  % only want output r
D = [0];  % should have 1 column (input vector) and 1 row (output vector)

sys = ss(A,B,C,D);  % creates our state-space system with the matrices
% sys has 1 output (r), 1 input (dr), and 4 states

% step response of the system for a step change in input value
t = linspace(0, 20, 1000);  % just the same as t = np.arange(0, 20.01, 0.01)
[y, t] = step(sys, t);  % step response for system sys with 20 time steps
% y is the step response data as an array, t is an array for with these
% steps are computed at

% plot(t, y);  % plots t against y
min(y(t<1));  % creates a logical vector of all t values for t<1 
% t = [0, 0.5, 1.2, 0.9]; then t < 1 returns: [true, true, false, true]
% y(t<1) is logical indexing so it only takes values of y when t<1 is true
% we find the minimum of y when t<1 is true (aka min(y) in the first second
min(y); % this would also do the same in this case but if the system had some 
% weird behaviour after then we could mess up, we wanted to only find the
% first peak so that's why we specified for the first second


% question 2
% basic aircraft equations
A = [-0.2 0.06 0 -1
    0 0 1 0
    -17 0 -3.8 1
    9.4 0 -0.4 -0.6];
B = [-0.01 0.06
    0 0 
    -32 5.4
    2.6 -7];

C = eye(4);  % output vector is same as state vector so just an identity matrix
D = [0 0
    0 0
    0 0
    0 0];

sys = ss(A,B,C,D);  % open loop system

K = [0 0 0 0 
    0 0 0 -0.55];  % gain matrix

sclosed = feedback(sys, K);


% question 3 -- control with ss systems
eig(sys.A);
eig(sclosed.A);
% when comparing these two matrices, for the complex conjugate pair for the
% closed loop system the real part is more negative = more damping and the
% imaginary part is smaller so slower oscillation hence the yaw damper has
% better dutch roll damping

% response to block-shaped aileron input u1
% calculate response for 1) withoutyaw damper, 2) with yaw damper, 3) with
% modified yaw damper -- washout filter (high pass filter which only allows
% high frequency in, blocks low freqs)

% output: yaw rate r
% inputs: aileron and rudder deflections da dr
% basic aircraft equations
A = [-0.2 0.06 0 -1
    0 0 1 0
    -17 0 -3.8 1
    9.4 0 -0.4 -0.6];
B = [-0.01 0.06
    0 0 
    -32 5.4
    2.6 -7];

% output equation matrices
C = [0 0 0 1];  % only want r output
D = [0 0];

% washout filter
% xdot = [-0.5]x + [0.5]u so A = -0.5, B = 0.5
% y = [-1]x + [1]u  so C = -1, D = 1
% so the ss is ss(-0.5, 0.5, -1, 1) since we do ss(A,B,C,D)

% washout filter is applied IN SERIES with the gain (it's another block
% added in)
Kr = -0.55;  % this is the gain for the yaw rate r
K1 = [0
    Kr];
K2 = [0
    Kr * ss(-0.5, 0.5, -1, 1)];
% we're connecting the gain and washout controllers in series so we
% multiply them

t = 0.1:0.1:20;  % time vector from 0.1 to 20 seconds, take 0.1 s steps

u1 = zeros(length(t), 1);
u1(1:10) = 1; % changing values of u1 from 1 to 10 to 1
u2 = zeros(length(t), 1);  % np.zeros((len(t), 1)) equivalent
u = [u1, u2];  % combining both vectors into a matrix

sys1 = ss(A,B,C,D);
sys2 = feedback(sys1, K1);
sys3 = feedback(sys1, K2);

y1 = lsim(sys1, u, t);
y2 = lsim(sys2, u, t);
y3 = lsim(sys3, u, t);

plot(t, y1, t, y2, t, y3)  % blue orange yellow

damp(sys1);
damp(sys2);

y1(t == 20)
y2(t == 20)
y3(t == 20)