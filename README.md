# setup-jboss-cluster

# What is this ?
* Utililty scripts which will hep you configure a cluster setup on JBoss 7.0.0 EAP

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
* Configuring Slaves
  * Open slaves.properties file located in cloned directory and fill in the following based on your configuration

