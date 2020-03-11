#!/bin/bash
#Install the module

pip install requests -t src
pip install requests_aws4auth -t src

#Call the zip module to create a ZIP
python zipmodule.py