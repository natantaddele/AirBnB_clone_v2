class webserver($number = 0) {
  # Implement the logic to delete out-of-date archives here
  $archives_to_keep = $number + 1

  exec { 'clean_versions_folder':
    command => "ls -1t /path/to/versions | tail -n +${archives_to_keep} | xargs -I {} rm -f /path/to/versions/{}",
    path    => '/usr/bin:/bin',
  }

  exec { 'clean_releases_folder':
    command => "ls -1t /data/web_static/releases | tail -n +${archives_to_keep} | xargs -I {} rm -f /data/web_static/releases/{}",
    path    => '/usr/bin:/bin',
  }
}
