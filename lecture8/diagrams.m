% roll control of an aircraft 
s = tf('s');
Ka = 4;
tauA = 0.7;
Kap = 0.9;

% output vector y should be [autopilot output, actuator output, roll angle]
Hact = ss(9/(s^2 + 5*s + 9)); % actuator
Hroll = ss(Ka/((tauA * s + 1) * s));  % roll
sys = append(Kap, Hact, Hroll);  % Combine systems with concatenated input and output vectors
% so the input and output vectors are concatenated for [autopilot,
% actuator, roll]

% input for autopilot is the external input - output of roll
% input for actuator is output of autopilot
% input for roll is output of actuator
Q = [1 -3  % into autopilot is -output of roll
    2 1  % into acutator is autopilot
    3 2];  % into roll is actuator
input = [1];  % only external input goes to component 1 the autopilot
outputs = [1 2 3];  % want to store output of components 1, 2 AND 3

% system with external INPUT going to autopilot, connections between the
% systems Q, and spitting out the outputs of components 1 2 and 3
sys = connect(sys, Q, input, outputs);


% control of moller skycar
s = tf('s');
K = 0.75;
H1 = ss(K * (4*s^2 + 2*s + 1)/(s * (1 + 0.1*s)));
H2 = ss(1/(s^2 *(s^2 + s + 4)));
sys = append(H1, H2);

input = [1];
outputs = [2 1];
Q = [1 -2
    2 1];

sys = connect(sys, Q, input, outputs);


% most systems have either one dominant pole or a complex pair of dominant
% poles ---> dominant poles are closest to the origin in the complex plane
% response for a system with multiple poles is similar to reponse of
% dominant pole alone


