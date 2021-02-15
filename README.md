# thebehzo
AWS Ssm Connector to able access EC2 instance without recheck dashboard or connect to vpn

# Usage
Example Usage: 


<img src="./img/demo.gif"></img>
```
    $ thebehzo eu-west-
    > kubernetes-worker-1 , i-INSTANCE_ID
    > kubernetes-master , i-INSTANCE_ID

```

You can select easily with interactive menu


# Setup
You can install python3 dependencies like that :
```
    $ pip3 install -r requirements.txt
```
After than you should specify default AWS_PROFILE, or credential values into your terminal session (I prefer profile usage):

```
    $ export AWS_PROFILE=<MY_ACCOUNT_ID> AWS_DEFAULT_REGION=<REGION> AWS_SDK_LOAD_CONFIG=1
```

Notice : If you want to run this via your shell, you should move somewhere in your $PATH directory:
