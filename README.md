Description
===========
Install and configure Mesos cluster with Marathon framework  support

Version 1.1-43p
-------------

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.tonomi.com/applications/upload?metadataUrl=https://raw.github.com/qubell-bazaar/component-mesos/1.1-43p/meta.yml)

Attributes
----------

Configurations
--------------
 - Mesos 0.22.0  Ubuntu 14.04 (us-east-1/ami-d85e75b0), AWS EC2 m1.small, ubuntu

Pre-requisites
--------------
 - Configured Cloud Account a in chosen environment
 - Either installed Chef on target compute OR launch under root
 - Internet access from target compute:
  - S3 bucket with Chef recipes: ** (TBD)
  - If Chef is not installed: ** (TBD)

Implementation notes
--------------------
 - Installation is based on Chef recipes
 - Uses mesos-dns for service discovery
    * mesos-dns  on master hosts 
    * resolv.conf entries on all nodes pointed to master hosts
    * access to cluster services avilable via hostnames 'app-name.marathon.mesos'
 - Uses haproxy-marathon-bridge for load balancing
    * haproxy-marathon-bridge script run by cron. It parse marathon api and configure local haproxy
    * SERVICE_PORT may be configured by user, used in haproxy frontend part
    * HOST_PORT allocated by mesos, used in backend part

