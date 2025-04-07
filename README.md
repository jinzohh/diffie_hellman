# Diffie-Hellman Key Exchange
To be able to share the private key so that the two parties can encrypt and decrypt messages while concealing them from everybody else, the Diffie-Hellman Key Exchange is used.

1. Alice chooses a random value $p$ and $g$, where $p$ is a large prime number and $g$ is a generator of $p$.
2. Alice chooses a private key, $A$, that is between 1 \le $A$ \le $p - 2$.
3. Alice creates a public key, $A_pub$ = $g^A$ mod $p$.
4. Alice sends ($A_pub$, $g$, $p$) to Bob.
5. Bob chooses a private key, $B$, that is also between 1 \le $B$ \le $p - 2$.
6. Bob create a public key, $B_pub$ = $g^B$ mod $p$.
7. Bob sends $B_pub$ to Alice.
8. Alice generates a shared private key, $K_shared$ = $B_pub^A$ mod $p$.
9. Bob generates a shared private key, $K_shared$ = $A_pub^B$ mod $p$.

A shared private key is generated that that both Alice and Bob can use to decrypt messages from each other without ever sharing their individual private keys.
