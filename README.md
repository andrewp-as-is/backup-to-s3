<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/backup-to-s3.svg?maxAge=3600)](https://pypi.org/project/backup-to-s3/)
[![](https://img.shields.io/npm/v/backup-to-s3.svg?maxAge=3600)](https://www.npmjs.com/package/backup-to-s3)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/backup-to-s3/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/backup-to-s3/actions)

### Installation
```bash
$ [sudo] pip install backup-to-s3
```

```bash
$ [sudo] npm i -g backup-to-s3
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

#### Examples
```bash
$ cd ~
$ backup-to-s3 git
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
