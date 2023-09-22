# Creates a manifest that kills a process named killmenow, using Puppet

exec { 'killaprocess':
  command => '/usr/bin/pkill -f killmenow',
}
