# Provisioning 

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

# Auto Deployment
 
## fabric

### in client

```bash
$ fab deploy:host=modo@tdd.aweek-jo.com -i /path/to/ssh-file.pem
```
 
## stream editor

### in server

```bash
$ sed -e "s/SITENAME/tdd.aweek-jo.com/g" -e "s/USERNAME/modo/g" deploy_tool/nginx.template.conf | sudo tee /etc/nginx/sites-available/tdd.aweek-jo.com
$ sed -e "s/SITENAME/tdd.aweek-jo.com/g" -e "s/USERNAME/modo/g" -e "s/PROJECTNAME/superlists/g" deploy_tool/gunicorn.template.service | sudo tee /etc/systemd/system/tdd.aweek-jo.com.service
$ sudo ln -s /etc/nginx/sites-available/tdd.aweek-jo.com /etc/nginx/sites-enabled/tdd.aweek-jo.com
$ sudo service nginx reload
$ sudo systemctl daemon-reload
$ sudo systemctl start tdd.aweek-jo.com
$ sudo systemctl enable tdd.aweek-jo.com
```