# mDNS DoS Project
![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)
[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://forthebadge.com)
<br>
![](https://komarev.com/ghpvc/?username=mDNS&color=green&style=for-the-badge&label=REPO+VIEWS)

## Introduction
A project with the aim to simulate (and try to prevent/mitigate) a DoS attack on a target server, relying on the mDNS protocol. 
<br>
If interested on more details, a link to the whole report is here provided: 
[.pdf report](https://drive.google.com/file/d/12v0-ll2ct8fnayhuDUyt1tBUqrDQh2AT/view?usp=sharing).

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
