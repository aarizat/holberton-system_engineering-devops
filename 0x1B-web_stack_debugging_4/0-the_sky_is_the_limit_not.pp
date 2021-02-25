# Fix request limits

exec { 'fix-limits':
  command => 'sed -i s/15/4096/g /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'restart':
  command => 'service nginx restart',
  path    => '/usr/local/bin/:/bin/'
}
