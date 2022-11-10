#This manifest execute a commannd
exec { 'pkill':
  command   => '/usr/bin/pkill killmenow',
  provider  => shell,
  returns   => [0, 1],
}
