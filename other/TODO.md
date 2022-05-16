# PLAN OF ACTION

Title: DDoS simulation (mDNS)

# Ideas from 16-05-2022:

## Measure time to reach server (latency) during an attack:

  * pyhton resolver scrypton
  
  * avahi (mdns) 
	
  ### Other services
  
  * ping (weeee juuust diiiid iiiit)
  
  * iperf
		
    ```bash
    iperf -s # on server
    iperf -c $SERVERS_IP -f M  # on client
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


-----------------------------

# Interesting Links/Papers
* https://www.mdpi.com/1999-5903/12/3/55


