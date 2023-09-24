# Make changes to the configuration file using Puppet 
# SSH client configuration to use the private key ~/.ssh/school
# SSH client configuration to refuse to authenticate using a password

file_line { 'Turn off passwd auth':
  ensure => present,
  line   => '    PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
}

file_line { 'Declare identity file':
  ensure => present,
  line   => '    IdentityFile ~/.ssh/school',
  path   => '/etc/ssh/ssh_config',
}
