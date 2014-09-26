import sublime, sublime_plugin, subprocess

class UploadtoserverCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		print("Running Uploadtoserver...")

		settings = sublime.load_settings("Upload to Server.sublime-settings")

		project_dir = settings.get("local_directory");
		upload_path = settings.get("host") + ":" + settings.get("remote_directory")
		path_to_scp = settings.get("path_to_scp", "/usr/bin/scp")
		file_path = self.view.file_name().replace(project_dir, '')

		sublime.status_message("Uploading " + file_path + "...")

		self.view.run_command("save")
		print(path_to_scp + " " + self.view.file_name() + " " + upload_path + file_path)
		scp_output = subprocess.check_output(path_to_scp + " " + self.view.file_name() + " " + upload_path + file_path, shell=True)
		print(scp_output)

		sublime.status_message(file_path + " uploaded!")
 