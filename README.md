# Sublime text jsonnet formatter package

Sublime text package to format jsonnet files

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

1. Keyboard shortcut: `ctrl+alt+0` (For OSX and Linux)

2. Using Command Palette : `Jsonnet Fmt: Format File`

## Customize

By default the jsonnet formatter runs with the flags `["--string-style", "d", "--comment-style", "s", "--indent", "2"]`.

You can update this by editing the sublime settings file Preferences -> Package Settings -> JsonnetFmt -> Settings User / Settings Default

`Settings Default` contains the default flags. `Settings User` can be used to override the default flags.
