# Configure nginx web server using Puppet

exec { 'install':
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; sudo bash -c "echo 'Hello World!' > /var/www/html/index.html" ; sudo sed -i "30i location /redirect_me {\n return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n" /etc/nginx/sites-available/default ; sudo service nginx restart',
  provider => shell,
}
