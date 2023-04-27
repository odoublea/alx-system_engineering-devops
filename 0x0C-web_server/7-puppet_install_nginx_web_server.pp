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
        server_name localhost;
        location / {
          return 200 'Hello World!';
        }
        location /redirect_me {
          return 301 /new_location;
        }
        location /new_location {
          return 200 'You have been redirected!';
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
