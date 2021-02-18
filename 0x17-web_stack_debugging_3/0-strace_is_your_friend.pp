# Fixe php extension

exec { 'wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
