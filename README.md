# Zabbix Lat Long Extractor
This script extracts the Lat/Long data from a hosts Inventory in Zabbix and transforms it into a JSON blob that can be used by Grafana's Worldmap plugin to plot points on a map.

It also generates a 'data.json' file which, when the script is run via cron task, can be used to provide up/down info for hosts based on the icmpping data found in Zabbix.

### Caveats
This module doesn't allow querying for particular data (yet). It just provides all hosts that have lat/long data as locations and returns their icmp status.

## Deployment
Just setup a virtualenv for the scripts to live in, install required packages using `pip install -r requirements.txt` and edit `config.ini` to suit your requirements. Then setup cron to call `run.py` within the virtualenv.

### Serving Files
To use with Grafana you'll need to deploy the generated JSON files (`location.json` and `data.json`) via a webserver. We use the 'Simple JSON Datasource' plugin and publish the two files inside an Apache VirtualHost.

Here is an extract of sample config for Apache that is working for us:
```
DocumentRoot "/var/www/*path*"
...
<Directory /var/www/*path*>
        Require all granted
        RewriteEngine On
        RewriteBase "/"
        RewriteRule "^zabbix_latlong/query" "zabbix_latlong/data.json"
        Header set Access-Control-Allow-Origin "*"
</Directory>

<Location /zabbix_latlong>
        Header set Access-Control-Allow-Origin "*"
        Header set Access-Control-Allow-Headers "Origin, X-Requested-With, Content-Type, Accept"
</Location>
```

### Credits
This project is maintained by me, @jameskirsop and time to create it was provided by my employer, [Daraco IT Services](https://www.daraco.com.au).