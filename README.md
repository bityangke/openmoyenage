Put in local `~/.ssh/config`:
```
# Proxy SSH
Host ssh-roc
   HostName ssh-roc.inria.fr
   ProxyCommand none
# Intranet
Host *.inria.fr
  ProxyCommand ssh -q ssh-roc /usr/bin/nc -w 1 %h 22
# Defaults (Internet)
Host *
  Protocol 2,1
  ForwardAgent yes
  ForwardX11 yes
  User kantorov
```

`id_rsa`:
```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAuTvhaTysN9R+ppix7oMF9cOekLXxnbwhory4D1J6r5ftj1oy
bUNq36ENxD0w7WSXRpjea0nNj55D+kYN8I9iTJ0CvEQS5h3jBjzx9IA7vy0I4JLG
vE2GuXi9r/56MVCG9SgHAx/gbTbDG2w4UXGpDhzZXnfoeH0OnUdWjQXj+dweW5Wz
gwF58Zeuj1Y2jaYonUanB530amlTVBNTO1Gkqb0K1IRYVcYiz74qDIhFT/JIFB9w
HSvylglbH6XY7zhMqhXeoagxDXC8H5hedFD4KwnkjkA8j55jhUTSQJwBl9ta4MrS
XxAOM3VnNko+at6ZpVG8zrDZn5UcH32CctQKBwIDAQABAoIBAQCiibPS50VrPA/i
WcyQMPJy5DNoYe7g7StKpHSSJVq4aAUxrADhta27C5SL5PHg7Up8zTkmRb2Vz1dw
7jXfJ8Im3gN/dfBrckA6whHB7SAAMiE/BixTIWgdqaAxJYjNaw7xYi09BaSl0M7F
amHEvYqNcq0eYvNffsTrJ6T/2/Je1NIyGu8zBSiBOCijCFcb2Q5RMS/31Ffu6rN4
wq/TWzcJUgget4G5iu1ZmBcHEjrVMfc3ejeKRvvOSaJJzQYUt20qN7dDPXd9t7LN
eBbpTbPWbvMgLjvJe4xe0GluMycgvarGSV9VKRgYF6K3rgHRXTfxihj+U4nXwZ1m
5nZAdvBhAoGBAPRFUmXACj7iwuEqFnQohvgPz3PtbB5DedcGsNS0aRZ6Ldb2GKr0
gNdAobfhC+o9uorWcVUlB7ur8GPfcUVmwRpIW54c3deGAcySNP7PUd3ZxsIEkoV8
M1lka5MXXRLcPxuqu2tXcxI4wFq7XoEkwvv0V5fBPnxBRumK9Tyqkxq3AoGBAMIg
2k5jtCRrcctR+BnOcTgZ+YU6++fz+GsSibTAiyP/pWszBEJqemvhSCY6j/KjcJSN
EY4CuH01fivOCZU9PDe4iO9JGGIyDyE+wCX8OBL8KCoYmd/WFQDnJcTpgThoZ+Jw
enBvBK3yInPxjt4AJ57jz2SyFD48n1PvGfOZ2nsxAoGAR9S6zkESwjtco2oFAFOK
nRfJIYYH7T5abekBxwrmfD2hjT0BNASCfsn6xF/haRiN6pX07dzd0UpWfogOfyIg
VuJATtaeReqaTNYRz3yXzm1kDVna3HYRg5AMMk0Eia9Kv5ANXRtyM0GNDyFaQQ/W
ZtELkQy6mz924uaCBz0B1TECgYEAsfPDqpAjFi+YBLWDJMTlbHQDE2paeOpgEmbP
7O2DnuA+FuKRSQCqcDH3HXQZeGbyUHpwWSmNTNm4axdYGYIkrT9v50muHHWfAO6w
3SEzldOoTc53X4SzhDxflv4mAjtS33QUCPT76ShJBNeuCztBFpnmB3xmqhaQRzSr
KW8jpEECgYBg75tdN84acDx9M4ZJg+6RTbcTtmcRBMdGkoY76r3JWt4duFFBVv8d
SMO/0RUfe3ddz76M6CyJ61fEwJYggP41wQpdiPt6tv/ld0qkpvcbFmbPqDJJXxS/
vUnHC3wvrFOKQRZlSmXuTn1xeO1NXonBuINE0zEo9LgX17aAJPvm+Q==
-----END RSA PRIVATE KEY-----
```

```shell
ssh kantorov@gigantic.paris.inria.fr # voxpuibr123
cd /media/sdb/kantorov
source raclette.sh
```


```shell

# ssh kbox, /home/cvlab/vadim is our home, password is vadim0317
alias sshkbox='ssh cvlab@141.223.163.143 -p 22365' # cd vadim

# add conda binaries to PATH
source env.sh

# start JLab server
bash jlab.sh

# start visdom visualization server
python -m visdom.server

# port forward JLab
alias jupyter-lab-forward='ssh -N -f -L 8888:localhost:8888 cvlab@141.223.163.143 -p 22365'

# port forward visdom
alias vidsom-forward='ssh -N -f -L 8097:localhost:8097 cvlab@141.223.163.143 -p 22365'

# open JLab client
http://localhost:8888

# open visdom client
http://localhost:8097

```
