#Create a file using manifest
node default {

file { '/tmp/school':
  # path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}

}
