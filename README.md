
# Haroopad Markdown - Sublime Text 3

Adds a handy command and menu item to open your current file with [Haroopad](http://pad.haroopress.com/).

The implementation is borrowed from [mou.app markdown](https://github.com/rwoody/mou-markdown-sublime), and adds Windows/Linux support.

## Installation Instructions

**Package Installer**

* Install [Sublime Package Control](http://wbond.net/sublime_packages/package_control)
* Select "Package Control: Install Package" from the Command Palette (`super+shift+p`)
* Find "Haroopad Markdown" and select

**Git clone**
* Enter directory through "Browse Packages..." in Sublime Text "Preferences"
* Run
    ```
    git clone https://github.com/liuhewei/haroopad-markdown-sublime.git
    ```
* Restart Sublime Text 3

## Configure
* Add Haroopad binary's directory into System PATH on Windows and Linux
* In Haroopad's Preferences, de-activate the "file auto-recovery" in "General" tab.

## Usage

With the view selected containing the file you wish to preview in Marked:

**Command Palette:**

* Select "Markdown: Open with Haroopad" from the Command Palette (`super+shift+p`)

**Menus:**

* Select Tools → Open with Haroopad

