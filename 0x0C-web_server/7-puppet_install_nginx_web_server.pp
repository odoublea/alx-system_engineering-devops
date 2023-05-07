# Install Nginx Server with Puppet

class nginx {
  package { 'nginx':
    ensure => present,
  }

  file { '/etc/nginx/sites-available/default':
    ensure => file,
    content => "
      server {
        listen 80;
        server_name _;
	error_page 404 /404.html
        location / {
          return 200 'Hello World!';
        }
        location /redirect_me {
          return 301 /new_location;
        }
      }
    ",
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure => 'link',
    target => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }
}

include nginx
