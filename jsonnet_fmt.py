import tempfile
from subprocess import call

import sublime
import sublime_plugin


def get_setting(key, default_value=None):
  settings = sublime.active_window().active_view().settings()
  settings = sublime.load_settings("JsonnetFmt.sublime-settings")
  return settings.get(key, default_value)


class JsonnetFmtCommand(sublime_plugin.TextCommand):
  view = None

  def get_region(self, view):
    return sublime.Region(0, view.size())

  def get_buffer_contents(self, view):
    return view.substr(self.get_region(view))

  def set_view(self):
    self.view = sublime.active_window().active_view()
    return self.view

  def get_view(self):
    if self.view is None:
      return self.set_view()

    return self.view

  def set_cursor_back(self, begin_positions):
    this_view = self.get_view()
    for pos in begin_positions:
      this_view.sel().add(pos)

  def get_positions(self):
    pos = []
    for region in self.get_view().sel():
      pos.append(region)
    return pos

  def get_settings(self):
    profile = sublime.active_window().active_view().settings().get(
      'jsonnet_fmt')
    return profile or {}

  def run(self, edit):
    this_view = self.get_view()
    this_contents = self.get_buffer_contents(this_view)

    new_contents = this_contents
    with tempfile.NamedTemporaryFile('r+') as temp:
      temp.write(this_contents)
      temp.flush()
      try:
        flags = get_setting(
          "jsonnet_fmt_flags",
          ["--string-style", "d", "--comment-style", "s", "--indent", "2"])
        retcode = call(["jsonnet", "fmt", temp.name, "-i"] + flags)
        if retcode > 0:
          sublime.error_message(
            "jsonnet fmt failed. Make sure your jsonnet is valid")
          return
        with open(temp.name) as f:
          new_contents = f.read()
      except Exception as e:
        sublime.error_message(
          "Make sure that jsonnet binary is installed and is executable")
    if new_contents != this_contents:
      this_view.replace(edit, self.get_region(this_view), new_contents)

class EventListener(sublime_plugin.EventListener):

  def on_pre_save(self, view):  # pylint: disable=no-self-use
    file_name = view.file_name()
    if file_name and (file_name.endswith(".jsonnet") or
                      file_name.endswith(".libsonnet")) and get_setting(
                        'jsonnet_fmt_run_on_save', False):
      view.run_command('jsonnet_fmt')
