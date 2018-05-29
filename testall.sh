#!/bin/sh

# appservers
#py.test test_MMC_INTEGMMC_APP_common.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.220  -v 
py.test test_MMC_INTEGMMC_APP_common.py test_MMC_APP_packages.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.220  -v -n4
#py.test test_MMC_INTEGMMC_APP_common.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.222  -v 
py.test test_MMC_INTEGMMC_APP_common.py test_MMC_APP_packages.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.222  -v -n4

