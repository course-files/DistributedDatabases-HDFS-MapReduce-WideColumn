<?php
/* Server configuration */
$i = 1;
$cfg['Servers'][$i]['host'] = 'mysql-8.3.0-bbt3104-lab3';  // MySQL server hostname
$cfg['Servers'][$i]['port'] = '3306';  // MySQL server port
$cfg['Servers'][$i]['auth_type'] = 'cookie';  // Authentication method
$cfg['Servers'][$i]['user'] = '';  // Default username (optional if using cookie authentication)
$cfg['Servers'][$i]['password'] = '';  // Default password (optional if using cookie authentication)
$cfg['Servers'][$i]['AllowNoPassword'] = false;  // Allow login without a password

/* User interface settings */
$cfg['DefaultLang'] = 'en';  // Default language
$cfg['DefaultCharset'] = 'utf-8';  // Default character set
$cfg['MaxRows'] = 100;  // Maximum number of rows to display

/* Security settings */
// Secret string for cookie authentication encryption
// Generated your own using the following command:
// python -c "import secrets; print(secrets.token_urlsafe(24))"
$cfg['blowfish_secret'] = 'dqz7cz3CPKrlwjsG7_b-94ASCqIqRhfq';

$cfg['ForceSSL'] = true;  // Force HTTPS connections

/* Customization */
// $cfg['ThemeDefault'] = 'original';  // Default theme
$cfg['ShowPhpInfo'] = true;  // Allow viewing of PHP info
$cfg['ShowChgPassword'] = true;  // Allow users to change their password

/* Additional configurations */
// Hide databases
// $cfg['Servers'][$i]['hide_db'] = '(information_schema|mysql|performance_schema|sys)';

// Upload/Download directories
$cfg['UploadDir'] = '';  // Directory where files can be uploaded
$cfg['SaveDir'] = '';  // Directory where files can be saved



/* Server configuration */
$i = 1;
$cfg['Servers'][$i]['auth_type'] = 'cookie';
$cfg['Servers'][$i]['AllowNoPassword'] = false;

/* phpMyAdmin configuration storage settings */
$cfg['Servers'][$i]['controlhost'] = 'mysql-8.3.0-bbt3104-lab3';
$cfg['Servers'][$i]['controluser'] = 'pma';
$cfg['Servers'][$i]['controlpass'] = '5trathm0re';
$cfg['Servers'][$i]['pmadb'] = 'phpmyadmin';
$cfg['Servers'][$i]['bookmarktable'] = 'pma__bookmark';
$cfg['Servers'][$i]['relation'] = 'pma__relation';
$cfg['Servers'][$i]['table_info'] = 'pma__table_info';
$cfg['Servers'][$i]['table_coords'] = 'pma__table_coords';
$cfg['Servers'][$i]['pdf_pages'] = 'pma__pdf_pages';
$cfg['Servers'][$i]['column_info'] = 'pma__column_info';
$cfg['Servers'][$i]['history'] = 'pma__history';
$cfg['Servers'][$i]['table_uiprefs'] = 'pma__table_uiprefs';
$cfg['Servers'][$i]['tracking'] = 'pma__tracking';
$cfg['Servers'][$i]['userconfig'] = 'pma__userconfig';
$cfg['Servers'][$i]['recent'] = 'pma__recent';
$cfg['Servers'][$i]['favorite'] = 'pma__favorite';
$cfg['Servers'][$i]['users'] = 'pma__users';
$cfg['Servers'][$i]['usergroups'] = 'pma__usergroups';
$cfg['Servers'][$i]['navigationhiding'] = 'pma__navigationhiding';
$cfg['Servers'][$i]['savedsearches'] = 'pma__savedsearches';
$cfg['Servers'][$i]['central_columns'] = 'pma__central_columns';
$cfg['Servers'][$i]['designer_settings'] = 'pma__designer_settings';
$cfg['Servers'][$i]['export_templates'] = 'pma__export_templates';
$cfg['Servers'][$i]['ssl'] = true;