# update package
exec { 'update':
  command => 'sudo apt-get -y update',
  provider => shell,
}

# instal and configure nginx
-> exec { 'install':
  command => 'sudo apt-get -y install nginx',
  provider => shell,
}

# add the custom HTTP header
-> exec { 'replace':
  command => 'sudo sed -i "/server_name _;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default',
  provider => shell,
}

-> exec { 'restart':
  command => 'sudo service nginx restart',
  provider => shell,
}
