# connect
AWS Ssm Connector to able access EC2 instance without access to AWS dashboard.This tools presents a simple menu for that purposes.

# Usage
Example Usage:

```
    $ connect --region eu-west-1
    > kubernetes-worker-1 , i-INSTANCE_ID
    > kubernetes-master , i-INSTANCE_ID
```

You can set the specified tags for your EC2 instances like that ;

```
   $ connect.py --region eu-west-2 --tag Name --value asg-development
```

<img src="./img/demo.gif"></img>

For more details 

```
python3 connect.py --help
Usage: connect.py [options]

Options:
  -h, --help            show this help message and exit
  -r REGION, --region=REGION
                        Region name of the aws account
  -t TAG, --tag=TAG     Tag of the EC2 instance
```


You can select easily with interactive menu

# Setup
You can install python3 dependencies like that :
```
    $ pip3 install -r requirements.txt
```

To connect your instance over ssm client you have to install this plugin following to this documents of AWS:
<a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html">Session Manager Plugin Installation</a>

After than you should specify default AWS_PROFILE, or credential values into your terminal session (I prefer profile usage):

```
    $ export AWS_PROFILE=<MY_ACCOUNT_ID> AWS_DEFAULT_REGION=<REGION> AWS_SDK_LOAD_CONFIG=1
```

Notice : If you want to run this via your shell, you should move somewhere in your $PATH directory:
