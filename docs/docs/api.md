# API reference

## CLI flags

| fikkie init                     |
|:--------------------------------|
| Set up the ~/.fikkie directory. |

| fikkie run [-l/--loglevel {DEBUG,INFO,WARNING,ERROR,CRITICAL,FAILURE}] |
|:-----------------------------------------------------------------------|
| Start fikkie.                                                          |

| fikkie start [-l/--loglevel {DEBUG,INFO,WARNING,ERROR,CRITICAL,FAILURE}] |
|:-------------------------------------------------------------------------|
| Start a fikkie daemon.                                                   |

| fikkie stop             |
|:------------------------|
| Stop the fikkie daemon. |

| fikkie status [-f/--format {YAML,JSON,JSON-PRETTY}] |
|:----------------------------------------------------|
| Get status from all servers.                        |

| fikkie -h/--help          |
|:--------------------------|
| Show the help/usage text. |

## Environment variables

| FIKKIE_BASE_DIR *(default: "~/.fikkie")* |
|:-----------------------------------------|
| Fikkie's working directory.              |

| FIKKIE_CONFIG *(default: "~/.fikkie/config.yaml")* |
|:---------------------------------------------------|
| The configuration file.                            |

| FIKKIE_BROKER_DIR *(default: "~/.fikkie/broker")* |
|:--------------------------------------------------|
| Celery broker data directory.                     |

| FIKKIE_DB_FILENAME *(default: "~/.fikkie/db.json")* |
|:----------------------------------------------------|
| The database file.                                  |

| FIKKIE_LOG_FILE *(default: "~/.fikkie/db.json")* |
|:-------------------------------------------------|
| The daemon log file.                             |

| FIKKIE_PID_FILE *(default: "~/.fikkie/fikkie.pid")* |
|:----------------------------------------------------|
| The PID file.                                       |

## Configuration options

| heartbeat.enable *(default: True)* |
|:-----------------------------------|
| Heartbeat is enabled if True.      |

| heartbeat.timezone *(default: "UTC")* |
|:--------------------------------------|
| The schedule timezone.                |

| heartbeat.schedule.minute *(default: 0)*    |
|:--------------------------------------------|
| Minute on which the heartbeat is triggered. |

| heartbeat.schedule.hour *(default: 12)*   |
|:------------------------------------------|
| Hour on which the heartbeat is triggered. |

| heartbeat.schedule.day_of_week *(default: '*')*                                    |
|:-----------------------------------------------------------------------------------|
| Day(s) of the week (0 = Sunday, 6 = Saturday) on which the heartbeat is triggered. |

| heartbeat.schedule.day_of_month *(default: '*')*                |
|:----------------------------------------------------------------|
| Day(s) of the month (0-31) on which the heartbeat is triggered. |

Example:

```yaml
heartbeat:
  timezone: 'Europe/Amsterdam'
  schedule:
    hour: 13
    minute: 37
```

| ssh.username *(default: "fikkie")* |
|:-----------------------------------|
| The SSH login username.            |

Example:

```yaml
ssh:
  username: fikkie
```

| servers.HOSTNAME.description               |
|:-------------------------------------------|
| A human-readable description of the check. |

| servers.HOSTNAME.command |
|:-------------------------|
| The command to execute.  |

| servers.HOSTNAME.expected   |
|:----------------------------|
| The expected stdout output. |

Example:

```yaml
servers:
  primary.foo.com:
    - description: 'MariaDB'
      command: 'sudo systemctl status mariadb | grep "Active: active" -c'
      expected: '1'
    - description: 'HTTP code foo.com'
      command: 'curl -s -o /dev/null -w "%{http_code}" foo.com'
      expected: '200'
```

| notifiers                                                   |
|:------------------------------------------------------------|
| A list of notifier objects. Parameters differ per notifier. |

Example:

```yaml
notifiers:
  - type: telegram
    token: '1234:abcd'
    chat_id: 1234
```

| [`type = discord`] notifiers.token |
|:-----------------------------------|
| The Discord bot token.             |

| [`type = discord`] notifiers.channel_id          |
|:-------------------------------------------------|
| The Discord channel ID to post notifications to. |

Example:

```yaml
notifiers:
  - type: discord
    token: 'foobarbaz'
    channel_id: 1234
```

| [`type = email`] notifiers.recipient         |
|:---------------------------------------------|
| The e-mail address to send notifications to. |

| [`type = email`] notifiers.email              |
|:----------------------------------------------|
| The e-mail address which fikkie uses to send. |

| [`type = email`] notifiers.password              |
|:-------------------------------------------------|
| The password needed to login to the SMTP server. |

| [`type = email`] notifiers.smtp_server |
|:---------------------------------------|
| The SMTP server.                       |

| [`type = email`] notifiers.smtp_port *(default: 465)* |
|:------------------------------------------------------|
| The port on which the SMTP server listens.            |

Example:

```yaml
notifiers:
  - type: email
    recipient: 'foo@hotmail.com'
    email: 'foo@gmail.com'
    password: 'v3rys3cr3t'
    smtp_server: 'smtp.gmail.com'
```

| [`type = slack`] notifiers.token |
|:---------------------------------|
| The Slack bot token.             |

| [`type = slack`] notifiers.channel_id                  |
|:-------------------------------------------------------|
| The channel ID that fikkie sends its notifications to. |

Example:

```yaml
notifiers:
  - type: slack
    token: 'xoxb-foobarbaz'
    channel_id: 'C0*******'
```

| [`type = telegram`] notifiers.token |
|:------------------------------------|
| The Telegram bot token.             |

| [`type = telegram`] notifiers.chat_id               |
|:----------------------------------------------------|
| The chat ID that fikkie sends its notifications to. |

Example:

```yaml
notifiers:
  - type: telegram
    token: '1234:abcd'
    chat_id: 1234
```
