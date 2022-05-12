# PLAN OF ACTION

Title: DDoS simulation (mDNS)


## Settimana in corso
* creare il codice per l'attacco
* creare la rete locale sul Cloud AWS 
* fare una primo test

-----------------------------

## Ideas and useful links

### RFC 6762 (Multicast DNS)
https://datatracker.ietf.org/doc/html/rfc6762

### Interesting Paper
https://www.mdpi.com/1999-5903/12/3/55


```
python3 src/attacker/attacker.py  -t 1.1.1.1 -k A -i 1.1.1.1
```