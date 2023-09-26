package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'Add redirection, 301':
  path   => '/etc/nginx/sites-available/default',
  ensure => 'present',
  line   => '/redirect_me {\n return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
