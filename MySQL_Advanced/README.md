# MySQL advanced

---
SQL (usually pronounced "sequal") is a common language/format used for
managing databases. Though most new database systems today use non-SQL,
SQL is the backbone of most commonly used databases today, and is important
to learn if you are ever going into an industry where managing databases
is important.

This project focuses on more advanced usage of SQL, using MySQL.

Note: On Fedora 42, at least with how my device is set up, you must do
`sudo mysql` instead of `mysql`, otherwise access for `root@localhost` will
be denied. The password is just the enter key. (Obviously not recomended for
sensitive info or a production database)

Project setup:
```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
echo "CREATE DATABASE holberton;" | mysql -uroot -p
```
Expected output after inputting password:
```
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
```
