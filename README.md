# restart_cloudera_manager
Even though there are api functions to play around with the services of the clusters managed by cloud era, I did not find a way to restart the cloudera manager using the api or remotely. This script will restart the cloudera manager.


This script will: 

1. SSH into the cloudera instance where the Cloud era manager is hosted 
2. Restart the instance
