#!/bin/sh

# delete all images whose last modification time > 10 minutes
find /home/medialab/ftpfolder/ -mmin +30 -regex '.*\.jpg\|.*\.png\|.*\.gif' | xargs rm -f

# delete all files whose last modification time > 1*24 hours
#find /home/medialab/ftpfolder/ -mtime +1 | xargs rm -rf
