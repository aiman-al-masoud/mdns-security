# Implementation of a DoS attack exploiting mDNS
![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)
[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://forthebadge.com)
<br>
![](https://komarev.com/ghpvc/?username=mDNS&color=blueviolet&style=for-the-badge&label=REPO+VIEWS)

## Introduction
A project with the aim to simulate (and try to prevent/mitigate) a DoS attack on a target server, relying on the mDNS protocol. 
<br>
For those who are interested, some useful link are provided here: 
- [report](https://drive.google.com/file/d/1m9wcIoehp-8j94YtZVLqQ6uMdboXcVQx/view?usp=sharing)
- [presentation](https://docs.google.com/presentation/d/e/2PACX-1vRfwAXhF4uzpBDhDH4H6qtqoLw_fc7zNCnQxCCPjKftBt_16lgaCxAhHpVus5NeNmy3IR1pVxBT7dXj/pub?start=false&loop=false&delayms=3000)

***
## Other details

<details>
<summary><b>How to use it</b></summary>

```
python3 src/scripton.py -t $TARGET(.local) -rr $RR_TYPE -i $SPOOFED_IP -n $NUM_THREADS 
```

Only ```-t (target)``` is mandatory

</details>

<details>
<summary><b>Citation</b></summary>

Please remember to cite this repository, whenever you have taken some parts, or the whole project.

</details>
