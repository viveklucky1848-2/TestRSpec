import sublime_plugin, sys, os.path, imp

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path += [BASE_PATH]

# Make sure all dependencies are reloaded
if 'plugin_helpers.reloader' in sys.modules:
  imp.reload(sys.modules['plugin_helpers.reloader'])
import plugin_helpers.reloader

from rspec.rspec_print import rspec_print
from rspec.execute_spec import ExecuteSpec
from rspec.task_context import TaskContext
from rspec.switch_between_code_and_test import SwitchBetweenCodeAndTest
from rspec.create_spec_file import CreateSpecFile

class TestCurrentLineCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    rspec_print("Running rspec")
    context = TaskContext(self, edit)
    ExecuteSpec(context).current()

class TestCurrentFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    rspec_print("Running rspec")
    context = TaskContext(self, edit, spec_target_is_file = True)
    ExecuteSpec(context).current()

class RunLastSpecCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    rspec_print("Running last rspec command")
    context = TaskContext(self, edit)
    ExecuteSpec(context).last_run()

class DisplayOutputPanelCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    rspec_print("Displaying output panel")
    context = TaskContext(self, edit)
    context.display_output_panel()

class SwitchBetweenCodeAndTestCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    rspec_print("Switching between code and test")
    context = TaskContext(self, edit)
    SwitchBetweenCodeAndTest(context).run()

class CreateSpecFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    rspec_print("Creating sepc file")
    context = TaskContext(self, edit)
    CreateSpecFile(context).run()
