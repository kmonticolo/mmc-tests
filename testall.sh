#!/bin/sh

# appservers
py.test test_MMC_INTEGMMC_APP_common.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.220  -v 

