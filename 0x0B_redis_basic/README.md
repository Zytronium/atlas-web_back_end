# Redis basic

---

This project is all about basic Redis. Redis is a database system like MongoDB,
MySQL, or Firebase Firestore. On my computer, I was unable to install Redis
itself since Linux Fedora 42 downloads Valkey instead of Redis when you try
to install it with `dnf`, however, Valkey seems similar enough to work
the same for these tasks. If required, Fedora users can still download Redis
from online instead of through `dnf`.

---

## How to install Redis for this project:

### Linux Ubuntu (20.04) (Or WSL):
```bash
sudo apt-get -y install redis-server
pip3 install redis
sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

### Linux Fedora (42):
```bash
sudo dnf install redis  # Actually installs valkey
pip3 install redis
sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/valkey/valkey.conf  # This step may not be needed
```

## How to start the server:

### Linux Ubuntu (20.04) (Or WSL):
```bash
service redis-server start
```

### Linux Fedora (42):
```bash
sudo systemctl start redis
```
(even if you have Valkey instead of Redis)

