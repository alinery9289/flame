`crontab` is used for periodic jobs on linux.

# How to write crontab jobs

## 1. write a script for doing your job
e.g, print one sentence to a file:
```shell
# content of my_cron_job.sh
echo "hello from crontab job" >> /tmp/test_cron.txt
```

## 2. create a cron file `task.txt`
The file name and suffix are arbitrary, here is the content:
```shell
* * * * * sh /home/root/my_cron_job.sh
```

## 3. add cron job
```shell
crontab task.txt

# list crontab jobs
crontab -l
```

## 4. restart cron service
```shell
sudo service cron restart
```
the job will be executed every one minute.

## 5. remove crontab jobs
```shell
crontab -r
```

# More information
For more information about `crontab`, type `man crontab` in shell.
