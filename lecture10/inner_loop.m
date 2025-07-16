% base system ss
clear
s = tf('s');
zeta = 2/sqrt(13);
omega = sqrt(13);
Kq = -24;
Ttheta = 1.4;
Vtas = 160
Hq = Kq * (1 + Ttheta * s)/(s^2 + 2 * zeta * omega * s + omega^2);

H = [Hq
    (1/s) * Hq
    (1/(s*(1 + Ttheta * s))) * Hq
    (Vtas / (s^2 * (1 + Ttheta * s))) * Hq];

Hss = minreal(ss(H))