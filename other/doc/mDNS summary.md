# mDNS explanation
## Introduction
Multicast DNS (mDNS) is a service that aims to solve name resolution in **smaller networks**. It takes a different approach than the well-known DNS: instead of sending requests to a name server, the network participants are all contacted directly.  
The corresponding client sends a multicast into the network and asks which network participant the host name corresponds to.   
In this way, the request also reaches the member of the group that has the searched hostname. This responds to the entire network, again via multicast. In this way, all participants are informed about the name and IP address connection and can make a corresponding entry in their mDNS cache.

Multicast DNS causes relatively **high traffic**, but actively tries to conserve network resources: to this end, the requesting client sends the correct response according to its opinion (i.e. according to the current cache entry). Only if this is no longer correct, or if the entry is about to expire, does the recipient have to respond.

In general, only hostnames ending with **.local** can be used with Multicast DNS.   
The mDNS was developed in the context of **Zeroconf** (Zero Configuration Networking) using essentially the same programming interfaces, packet formats, and operating semantics as the unicast Domain Name Service (DNS). The idea behind Zero Configuration Networking is to allow computers to communicate with each other without the need for prior configuration. 

It makes use of **UDP packets** and its implementation is described in [RFC 6762](https://www.rfc-editor.org/rfc/rfc6762.html).

A popular implementation of mDNS is Bonjour by Apple, also the open source software Avahi can now be used as an mDNS service. As of Windows 10, mDNS is also available in Microsoft's operating system.

### Advantages
* Since all devices share their IP addresses, there is no need to configure a server or directory. This makes it possible to add additional devices very dynamically and quickly.

### Disadvantages
* One problem lies in the Multicast procedure itself. Although the protocol tries to keep network traffic low, participating computers must constantly monitor the network and process incoming messages. This requires computing power.

* Assigning host names is problematic: since you can freely choose a name for each device, as long as it ends in .local., this can (at least theoretically) lead to two network devices with the same host name.  
The developers of mDNS have deliberately not proposed a solution to this problem. On the one hand, it is assumed that the case rarely occurs; on the other hand, the double naming may be intentional.
Also, by default, mDNS only resolves hostnames that end with the .local top-level domain. This can cause problems if .local includes hosts that do not implement mDNS but can be found via a conventional unicast DNS server. Resolving such conflicts requires network configuration changes that mDNS is designed to avoid.

* In some cases, mDNS is open. This means that it also responds to requests from outside (the Internet). Attackers can find such open services and use them for DDoS attacks, using network devices improperly and targeting a server. In addition, in a DNS Multicast even sensitive data can be detected (cleartext). This allows attackers to know information about connected devices and use it for further attacks.

## Packets structure
An mDNS message is a UDP packet sent in multicast using the following addressing:

* IPv4 address 224.0.0.251 or IPv6 address ff02::fb
* UDP port 5353
* When using Ethernet frames, the standard IP multicast MAC address 01:00:5E:00:00:FB (for IPv4) or 33:33:00:00:FB (for IPv6)

The payload structure is based on the unicast DNS packet format, which consists of two parts: the header and the data.

The header is identical to the one found in the unicast DNS, as are the subsections in the data part: queries, responses, authoritative-nameservers, and additional records. The number of records in each subsection corresponds to the value of the corresponding *COUNT field in the header.

### Queries
The format of the records in the query section is a bit different from that of classic DNS by adding a single-bit UNICAST-RESPONSE field.

Field  | Description | Length
----- | ---- | -----
QNAME  		  | Name of the node to which the query pertains | Variable
QTYPE		  | The type of the query  | 16
UNICAST-RESPONSE  | Boolean flag indicating whether a unicast-response is desired  | 1
QCLASS 		  | "IN"  | 15

The *UNICAST-RESPONSE* field is used to minimize unnecessary transmissions over the network: if the bit is set, responders SHOULD send a direct-unicast response directly to the requesting node rather than broadcasting the response to the entire network.

The *QCLASS* field is identical to that found in unicast DNS (IN class).

### Resource records
All records in the answers, authoritative-nameservers, and additional records sections have the same format and are known collectively as *Resource Records* (RR).

The general format of RRs in mDNS is slightly different from classic DNS and is as follows:

Field | Description | Length
----- | ---- | -----
RRNAME	|Name of the node to which the record pertains	|Variable
RRTYPE	|The type of the Resource Record	|16
CACHE-FLUSH	|Boolean flag indicating whether outdated cached records should be purged	|1
RRCLASS		|Class code, 1 a.k.a. "IN" for the Internet and IP networks	|15
TTL	|Time interval (in seconds) that the RR should be cached	|32
RDLENGTH	|Integer representing the length (in octets) of the RDATA field		|16
RDATA	|Resource data; internal structure varies by RRTYPE	|Variable

The *CACHE-FLUSH* bit is used to instruct neighboring nodes that the record should overwrite, rather than be added to any existing cache entry for this RRNAME and RRTYPE.

## DDoS attacks
### Problem
An Openly Accessible Multicast DNS server that is misconfigured and responds to unicast queries from sources outside of the local area network, may be abused for a *Distributed Denial-of-Service (DDoS) Reflection/Amplification attack* against a third party. Information returned in a mDNS response to a unicast query may also disclose potentially sensitive information of the devices on the network.

DoS attacks can be divided into direct and reflection attacks. 
* Direct attacks involve traffic sent directly to the victim from some infrastructure controlled by a malicious actor. 
* In reflection attacks, third party servers are involuntarily used to reflect attack traffic towards the victim. An Amplified mDNS Distributed Denial of Service (DDoS) Reflection Attack consist of a number of separate components and utilise certain features.

### Reflection/Amplification attack
Steps performed to carry out the attack:
1. A malicious actor will scan and probe the Internet searching for an Internet connected Multicast DNS server, which has been misconfigured and that responds to a unicast query from a source outside of its local area network. Once a vulnerable mDNS server has been identified, the malicious actor will seek to exploit it.
2. In a reflection attack, Internet connected third party servers that provide a service and are openly accessible, are involuntarily used to reflect attack traffic towards the victim, through the use of IP Spoofing. Reflection also serve to obscure the source of the attack traffic and to hide the identity of the malicious actor.  
IP Spoofing is the creation of a Internet Protocol (IP) packet and modifying it, replacing its genuine source address with a forged source address. By masquerading as a different host, a malicious actor can hide his or her true identity and location.
3. Many protocols that allow for reflection also add amplification, resulting in the amount of attack traffic sent to the victim to be many times greater than that sent to the reflector initially.  
Multicast DNS devices advertise information about network services they provide. Defined in [RFC6763](https://www.rfc-editor.org/rfc/rfc6763.html), the service enumeration query which will return all advertised service type on a network.   
The largest mDNS response payload recorded in a DoS attack contained 428 bytes of data, that responded to a query of 45 bytes in size, an **amplification factor of 9.51**.

### Verification of available of openly accessible service
To establish if a host has an openly accessible service on the Internet, simple utility programs or tools included with the standard Linux/Ubuntu distribution can be used. 

#### Dig
You can send a mDNS request for an arbitrary domain name to the IP address of the mDNS server, an openly accessible mDNS service will return a response similar to the example below::
```console
$ dig +short -p 5353 -t ptr _services._dns-sd._udp.local @ xxx.xxx.xxx.xxx
DiG 9.10.31-P4-Ubuntu <<>> TARGET @ xxx.xxx.xxx.xxx
_workstation._tcp.local.
_udisks-ssh._tcp.local.:
```

Otherwise, the request will timeout:
```console
;; connection timed out; no servers could be reached.
```

### Solution
* If mDNS services are not required, disable mDNS services in devices that allow it or block inbound and outbound mDNS traffic on port 5353/UDP.
* If mDNS services are required, restrict access of mDNS services to authorised or specific IP addresses.

## References
1. [IONOS Guide - Multicast DNS: una risoluzione del nome alternativa](https://www.ionos.it/digitalguide/server/know-how/multicast-dns/)
2. [Wikipedia - Multicast DNS](https://en.wikipedia.org/wiki/Multicast_DNS)
3. [NCSC - Openly Accessible mDNS Servers](https://www.ncsc.gov.ie/emailsfrom/DDoS/mDNS/)
