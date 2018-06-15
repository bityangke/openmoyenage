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
