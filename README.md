<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/backup-to-s3.svg?maxAge=3600)](https://pypi.org/project/backup-to-s3/)
[![](https://img.shields.io/npm/v/backup-to-s3.svg?maxAge=3600)](https://www.npmjs.com/package/backup-to-s3)
[![Travis](https://api.travis-ci.org/looking-for-a-job/backup-to-s3.svg?branch=master)](https://travis-ci.org/looking-for-a-job/backup-to-s3/)

#### Installation
```bash
$ [sudo] npm i -g backup-to-s3
```
```bash
$ [sudo] pip install backup-to-s3
```

#### How it works
```
<s3-bucket-name>/<slug>/<year>/<year-month>/<year-month-day>/name-<datetime>.tar.gz
```

#### Config
environment variables (optional):

variable|description|default value
-|-|-
`BACKUP_TO_S3_BUCKET`|s3 bucket name| `backup-to-s3-<account-id>`
`BACKUP_TO_S3_EXCLUDE_FROM`|exclude patterns|`$XDG_CONFIG_HOME/backup-to-s3/exclude.txt`, e.g. `~/.config/backup-to-s3/exclude.txt`

#### CLI
```bash
usage: backup-to-s3 path ...
```

#### Examples
```bash
$ cd ~
$ backup-to-s3 git
```

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>