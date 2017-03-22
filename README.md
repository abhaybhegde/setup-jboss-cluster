# setup-jboss-cluster

# What is this ?
* Utililty scripts which will hep you configure a cluster setup on JBoss 7.0.0 EAP

![pythonpath](https://cloud.githubusercontent.com/assets/5040809/24194892/bc656e8c-0f1d-11e7-88cd-a25ea6273bcd.png)

# What do i require to use this?
* Python 2.6 or above
* Paramiko module for python - http://www.paramiko.org/
* Java 8
* Linux OS ( Windows not supported )
* JBoss 7.0.0 EAP - https://developers.redhat.com/products/eap/download/
* Atleast 3 Phyiscal machines or VMs having linux on them. 1 for master and 2 for slaves. All the machines must have the above pre-requisites.

# How do i use this ?
* Clone  the *master* branch into a suitable directory
* Download JBoss 7.0.0 EAP.zip and extract into Master and Slave machines
* Before running the main script, you will have to configure the details of Slaves and Master.Below steps explain how you have to
* **Configuring Slaves**
  * Open *slaves.properties* file located in cloned directory and fill in the following based on your configuration
  
  
  ![slaves_properties](https://cloud.githubusercontent.com/assets/5040809/24194306/96726092-0f1b-11e7-8d40-e6d2740d7c0d.png)

  * <Slave_IP> -  IP address of the Slave machine
  * JBOSS_HOME - path to the directory where you have extracted jboss-7-eap in slave machine
  * USER_NAME - Slave user, HOST_PASSWORD - password that will get converted to bas64 string 
  
  * **Configuring Master**
    * Open master.properties file located in cloned directory and fill in the following based on your configuration
    * *JBOSS_HOME* - path to where you have extracted jboss7.zip in master machine, *ADMIN_USERNAME* & *ADMIN_PASSWORD* = user name and password in-order to login to jboss admin console , once the setup is up.
  
* **Starting the script**
* Assuming you have all the pre-requisites in place and after you have configured the master and slaves according to above steps, you can start the script as following:

* cd to the directory where you have cloned the repo
* Execute the following:
  > python setup-jboss-cluster.py -m=<ip_address_of_the_master> -s=<comma_separated_ip_addresses_of_the_slaves>
  
 * Example
  > python setup-jboss-cluster.py -m=192.168.1.2 -s=192.168.1.3,192.168.1.4 
