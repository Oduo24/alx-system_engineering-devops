# kills the killmenow process
exec { 'kill_proc':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin']
}
