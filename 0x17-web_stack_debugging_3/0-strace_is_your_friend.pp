# This script fixes Apache error 500

exec { 'fix typo':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/bin/',
}
