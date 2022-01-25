# Configuring fikkie

## Setting up SSH

You probably already have set this up, so if you can SSH to the host(s) you want to
monitor without using a password, you're fine. If not, please generate a key using
`ssh-keygen` and copy the public key to `~/.ssh/authorized_keys` on the target host(s).


## Adding user

This step is optional. However, it might be a good idea to create a separate
user for fikkie on the target host(s) with limited sudo permissions.

Open the sudoers file with `sudo visudo` and add the following line:

```
fikkie ALL=(ALL) NOPASSWD: /path/to/command1, /path/to/command2
```


## Setting up fikkie

When you run `fikkie init`, a configuration template is placed in
`~/.fikkie/config.yaml`. Edit this file to specify the servers you want to
monitor and which notifiers should be used. Go to the
[API Reference](#api-reference) for more info.

To test the configuration, start fikkie by executing:

```bash
fikkie run
```

When everything works, you can [start a fikkie daemon](#running-fikkie-as-a-daemon).


## Running fikkie as a daemon

When you've configured fikkie and everything works as expected, start a fikkie daemon as
follows:

```bash
fikkie start
```

Stopping the daemon is just as easy:

```bash
fikkie stop
```

The fikkie daemon saves its logs in `~/.fikkie/fikkie.log`.
