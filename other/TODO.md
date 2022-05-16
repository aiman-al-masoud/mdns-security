# PLAN OF ACTION

Title: DDoS simulation (mDNS)

# Ideas from 16-05-2022:

## Measure time to reach server (latency) during an attack:

  * pyhton resolver scrypton
	* avahi (mdns) 
	
  ### Other services
	* ping (weeee juuust diiiid iiiit)
	
	* iperf
		
    ```
    iperf -s
		iperf -c 192.168.1.128 -f M 
		```

## Correlate query type with:
	* num devices connected to network 
	* traffic	
	* latency
	* queries per second /num of crit. threads 
	
## Measure the impact of an attack on:
	* target
	* router (eg: ping router)
  * "Collateral": other users on the network 


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
