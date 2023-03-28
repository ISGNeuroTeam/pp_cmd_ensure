# pp_cmd_ensure
Postprocessing command "ensure"
## Description
Command adds columns with specified names if columns not exist

### Arguments
- columns - positional infinite argument, text. Columns names 

### Usage example
```
query: readFile a.csv
          a         b         c
0  0.438921  0.118680  0.863670
1  0.138138  0.577363  0.686602
2  0.595307  0.564592  0.520630
3  0.913052  0.926075  0.616184
```
```
query: readFile a.csv | ensure c,d,f
          a         b         c   d   f
0  0.438921  0.118680  0.863670 NaN NaN
1  0.138138  0.577363  0.686602 NaN NaN
2  0.595307  0.564592  0.520630 NaN NaN
3  0.913052  0.926075  0.616184 NaN NaN

```

## Getting started
### Installing
1. Create virtual environment with post-processing sdk 
```bash
    make dev
```
That command  
- downloads [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates link to current command in postprocessing `pp_cmd` directory 

2. Configure `otl_v1` command. Example:  
```bash
    vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/otl_v1/config.ini
```
Config example:  
```ini
[spark]
base_address = http://localhost
username = admin
password = 12345678

[caching]
# 24 hours in seconds
login_cache_ttl = 86400
# Command syntax defaults
default_request_cache_ttl = 100
default_job_timeout = 100
```

3. Configure storages for `readFile` and `writeFile` commands:  
```bash
   vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/readFile/config.ini
   
```
Config example:  
```ini
[storages]
lookups = /opt/otp/lookups
pp_shared = /opt/otp/shared_storage/persistent
```

### Run ensure
Use `pp` to run ensure command:  
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | otl_v1 <# makeresults count=100 #> |  ensure a,b,c
```
## Deploy
Unpack archive `pp_cmd_ensure` to postprocessing commands directory