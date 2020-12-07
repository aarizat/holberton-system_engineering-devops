# Create file

file {'holberton':
    ensure => 'present',
    owner => 'www-data',
    group => 'www-data',
    mode => '0744',
    content => 'I love Puppet',
    path => '/etc/holberton',
}
