# mDNS vulnerabilities
## Introduction
The mDNS protocol does not provide any security services, such as DNSSEC or DNS over TLS for the well-known DNS protocol, since they are difficult to configure in small and simple local area networks. This is why local networks using this protocol may be subject to security threats. 
Analyzing all the vulnerabilities of services/products using the mDNS protocol, can be identified three main types of threats:
- **denial of service attack**: attackers fill the local network nodes (with mDNS enabled) with lots of messages that exploit protocol-specific features. These messages can make nodes unreachable and overload the local network
- **sensitive information leak**: attackers can be able to enter the local network and obtain sensitive information
- **remote code execution**: attackers who can access a computer in the local area networkand can execute system commands, write, modify, delete, or read files
- **Buffer Overflow**: attackers manipulate the software code to carry out malicious actions and compromise the affected system 

## Denial of Service
DoS attacks are caused by both vulnerabilities such as CVE-2022-20682, CVE-2021-1439, CVE-2020-3359 in which insufficient checks are made on incoming mDNS messages. But also by vulnerabilities such as CVE-2017-6520, CVE-2015-2809, CVE-2015-1892 in which devices are misconfigured and inadvertently respond to unicast queries with source addresses that are not link-local.

It should also be added that the nature of the protocol, in which multicast queries are involved, is itself a feature that attackers can exploit to carry out a DoS/DDoS attack on a local network after gaining access to it. 

## Sensitive information leak
In analyzing the vulnerabilities of this protoccol, it is observed that leakage of sensitive information, but more generally of any information one does not want to share, is caused by several factors. Again, the most frequent problem, evidenced by vulnerabilities such as CVE-2015-6586, CVE-2017-6520, CVE-2015-2809, and CVE-2015-1892 is caused by malconfigurations that allow devices to respond to mDNS queries not coming from within the local network. 

Another vulnerability such as CVE-2020-3182 that plagues the protocol configuration of Cisco Webex Meetings Client for macOS, exists because some sensitive information is included in the mDNS replies. Thus an attacker could exploit this vulnerability by making mDNS queries for a particular service against an affected device. A successful exploit could allow the attacker to gain access to sensitive information. A similar problem is highlighted by vulnerability CVE-2020-26966, in which searching for a single word from the address bar causes an mDNS query to be sent on the local network searching for a hostname consisting of that string (only affected Windows operating systems). This vulnerability affects Firefox < 83, Firefox ESR < 78.5, and Thunderbird < 78.5.

## Remote code execution
Remote code execution is a threat highlighted by vulnerabilities such as CVE-2020-6072 and CVE-2014-9378, where in both cases there are errors in checking some return values of certain functions. 

The CVE-2020-6072 vulnerability evinces that the minimal mDNS resolver library named libmicrodns in version 0.1.0, when parsing compressed labels in mDNS messages, does not check the return value of the rr_decode function. 
Similar problem is the one highlighted in vulnerability CVE-2014-9378 in which the free and open source network security tool for man-in-the-middle attacks on a LAN, named Ettercap, does not validate certain return values. 

## Buffer Overflow
A buffer overflow condition exists when a program attempts to put more data in a buffer than it can hold or when a program attempts to put data in a memory area past a buffer. Writing outside the bounds of a block of allocated memory can corrupt data, crash the program, or cause the execution of malicious code. The buffer overflow exploit techniques a hacker uses depends on the architecture and operating system being used by their target. 

There are some vulnerabilities such as CVE-2018-4003, CVE-2017-12087, CVE-2015-7987, and CVE-2007-2386 that highlight buffer overflow problems. In particular, vulnerabilities CVE-2015-7987 and CVE-2007-2386 evince these problems for "mDNSResponder" the core Bonjour's process that regularly scans the local network looking for other Bonjour-enabled devices. Note that Apple's Bonjour service is available for both Mac OS and Windows.  


## Resources
1) https://www.mdpi.com/1999-5903/12/3/55/htm
2) https://nvd.nist.gov/vuln
3) https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/Cisco-SA-20140613-CVE-2014-3290
4) https://security.archlinux.org/CVE-2020-6072
5) https://en.wikipedia.org/wiki/Ettercap_(software)
