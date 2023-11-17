# Change the OS configuration to login with the holberton user and open a file without any error message
exec { 'hard lim':
  command => "sed -i '/holberton hard nofile 5/d' /etc/security/limits.conf",
  path    => '/bin/',
}

exec { 'soft lim':
  command => "sed -i '/holberton soft nofile 4/d' /etc/security/limits.conf",
  path    => '/bin/',
}
