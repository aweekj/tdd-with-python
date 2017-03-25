## Required Packages

```bash
$ sudo apt-get install nginx git python3 python3-pip python3-venv
```

## nginx

```bash
$ sudo ln -s nginx.conf /etc/nginx/sites-enabled/
$ sudo service nginx reload
```

## gunicorn

```bash
$ sudo cp gunicorn.service /etc/systemd/system/
$ sudo systemctl daemon-reload
$ sudo systemctl start gunicorn
$ sudo systemctl enable gunicorn
$ sudo systemctl status gunicorn
``` 
