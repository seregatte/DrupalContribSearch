import webbrowser
import sublime, sublime_plugin

class DrupalContribSearchCommand(sublime_plugin.TextCommand):

    def run(self, edit, drupal_version=None):

        selection = ""
        for region in self.view.sel():
            selection += self.view.substr(region)

        webbrowser.open("http://drupalcontrib.org/api/search/%s/%s" % (drupal_version, selection))

    def is_visible(self):

        is_visible = False

        for region in self.view.sel():
            if not region.empty():
                is_visible = True

        return is_visible

    def is_enabled(self):
        return self.is_visible()