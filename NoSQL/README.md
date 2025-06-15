# NoSQL

---

This project is all about NoSQL (Not Only SQL) database management.

Installation instructions for Mongodb on Fedora 42:
https://developer.fedoraproject.org/tech/database/mongodb/about.html

Summary:
Open or create `mongodb-org-6.0.repo`
```bash
sudo nano /etc/yum.repos.d/mongodb-org-6.0.repo
```

Add this content to the file and save
```
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/9/mongodb-org/6.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
```

Install `mongodb-org` with `dnf`
```bash
sudo dnf install mongodb-org
```

Enable the service:
```bash
sudo systemctl enable mongod.service
```

To start the service:
```bash
sudo systemctl start mongod.service
```

To stop the service:
```bash
sudo systemctl stop mongod.service
```

To check MongoDB current status:
```bash
sudo systemctl status mongod.service
```

---

Note:  
On Fedora 42 using `mongosh` instead of `mongo`, use this format:
```bash
cat 0-list_databases | OPENSSL_CONF=/dev/null mongosh --quiet
```
instead of this:
```bash
cat 0-list_databases | mongo
```

This will show output like
```
test> show dbs
admin   40.00 KiB
config  12.00 KiB
local   40.00 KiB
test> 
```
instead of
```
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin     0.000GB
config    0.000GB
local     0.000GB
logs      0.005GB
bye
```
