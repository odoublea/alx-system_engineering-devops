# Fix typo in WordPress settings file to allow Apache listen on port 500
exec { 'Fix typo in filename':
	command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
	provider => shell,
}
