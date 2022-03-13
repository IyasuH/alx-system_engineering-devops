# execute ssh ciet configuration to use ~/.ssh/school and refuse to autheticate using password
file_line {'private file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '~/.ssh/school',
}
file_line {'password off':
  ensure => 'present',
  path   => 'etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication yes',
}
