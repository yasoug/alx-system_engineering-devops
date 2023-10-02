# update package
exec { 'update':
  command     => 'sudo apt-get -y update',
}

# instal and configure nginx
-> exec { 'install':
  command => 'sudo apt-get -y install nginx',
}

# add the custom HTTP header
-> file_line { 'add custom header':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  line   => "\n\t\tadd_header X-Served-By \"$(hostname)\";",
  after  => 'location / {',
}

-> exec { 'restart':
  command => 'sudo service nginx restart',
}
