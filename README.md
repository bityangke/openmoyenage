```shell

# ssh kbox, /home/cvlab/vadim is our home, password is vadim0317
alias sshkbox='ssh cvlab@141.223.163.143 -p 22365 "cd vadim ; bash"'

# add conda binaries to PATH
source env.sh

# run JLab server
bash jlab.sh

# port forward to JLab client
alias jupyter-lab-start='ssh -N -f -L 8888:localhost:8888 cvlab@141.223.163.143 -p 22365'

# open JLab client
http://localhost:8888
```
