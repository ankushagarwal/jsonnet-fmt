# Sublime text jsonnet formatter package

Sublime text package to format jsonnet files.

Jsonnet and Libsonnet files can be quite complicated to write for a human. This package aims to help a user write jsonnet by formatting their jsonnet files using [jsonnet fmt](http://jsonnet.org/learning/tools.html).

## Prerequisites

[jsonnet](https://github.com/google/jsonnet) binary is required for this to work. To build it, you can clone the [jsonnet repo](https://github.com/google/jsonnet) and run

```
make
sudo mv jsonnet /usr/local/bin/jsonnet
sudo chmod +x /usr/local/bin/jsonnet
```

## Install

1. cd to Packages directory. The location of your Sublime Text Packages directory can be found by clicking the menu: `Preferences` > `Browse Packages...`.

2. Run `git clone https://github.com/ankushagarwal/jsonnet-fmt`


## Use Formatter

Open a jsonnet / libsonnet file. There are two ways to format the file:

1. Keyboard shortcut: `ctrl+alt+0` (For OSX and Linux)

2. Using Command Palette : `Jsonnet Fmt: Format File`

## Customize

1. By default the jsonnet formatter runs with the flags `["--string-style", "d", "--comment-style", "s", "--indent", "2"]`. You can update the `jsonnet_fmt_flags` setting to change these flags. Run `jsonnet fmt --help` to view more info about these flags.

2. By default `jsonnet_fmt_run_on_save` is set to false. Set it to true if you want the formatter to run automatically on saving a jsonnet / libsonnet file.

You can update these settings by editing the sublime settings file Preferences -> Package Settings -> JsonnetFmt -> Settings User / Settings Default. `Settings Default` contains the default flags. `Settings User` can be used to override the default flags.
