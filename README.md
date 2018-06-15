```shell

alias sshtitanxp='ssh cvlab@141.223.163.143 -p 22365 "cd vadim ; bash"'

source env.sh

bash jlab.sh

alias jupyter-lab-start='ssh -N -f -L 8888:localhost:8888 cvlab@141.223.163.143 -p 22365'
```
