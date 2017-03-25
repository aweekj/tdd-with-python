## Required Packages

```bash
$ sudo apt-get install nginx git python3 python3-pip python3-venv
```

## nginx

```bash
$ sudo cp nginx.conf /etc/nginx/sites-available/
$ sudo ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/nginx.conf
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

## stream editor

```bash
$ sed "s/SITENAME/tdd.aweek-jo.com/g" deploy_tools/nginx.template.conf
$ sed "s/USERNAME/modo/g" deploy_tools/nginx.template.conf

$ sed "s/SITENAME/tdd.aweek-jo.com/g" deploy_tools/gunicorn.template.service
$ sed "s/USERNAME/modo/g" deploy_tools/gunicorn.template.service
$ sed "s/PROJECTNAME/superlists/g" deploy_tools/gunicorn.template.service

$ sudo cp deploy_tools/nginx.template.conf /etc/nginx/sites-available/tdd.aweek-jo.com
$ sudo ln -s /etc/nginx/sites-available/tdd.aweek-jo.com /etc/nginx/sites-enabled/tdd.aweek-jo.com

$ sudo cp deploy_tools/gunicorn.template.service /etc/systemd/system/tdd.aweek-jo.com

$ sudo service nginx reload

$ sudo systemctl daemon-reload

$ sudo systemctl start tdd.aweek-jo.com
$ sudo systemctl enable tdd.aweek-jo.com

```