import youtube_dl
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.properties import ObjectProperty

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '200')

class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 1
		self.add_widget(Label(text="URL: "))
		self.url = TextInput(multiline=False)
		self.add_widget(self.url)

		self.download_a = Button(text="Download audio", font_size=20)
		self.download_a.bind(on_press=self.pressed_audio)
		self.add_widget(self.download_a)

		self.download_v = Button(text="Download video", font_size=20)
		self.download_v.bind(on_press=self.pressed_video)
		self.add_widget(self.download_v)

	def pressed_audio(self, instance):
		download_url = self.url.text
		format = 'm4a'
		ydl_opts = {'noplaylist' : True}
		ydl_opts['format'] = format
		ydl_opts['outtmpl'] = f'~/Downloads/%(title)s.{format}'
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			print(f'DOWNLOADING... {format} format')
			ydl.download([download_url])
		self.url.text = "                           Download Finished."
		print('')

	def pressed_video(self, instance):
		download_url = self.url.text
		format = 'mp4'
		ydl_opts = {'noplaylist' : True}
		ydl_opts['format'] = format
		ydl_opts['outtmpl'] = f'~/Downloads/%(title)s.{format}'
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			print(f'DOWNLOADING... {format} format')
			ydl.download([download_url])
		self.url.text = "                           Download Finished."
		print('')

class MyApp(App):
	def build(self):
		self.title = 'Youtube Downloader'
		return MyGrid()

if __name__ == "__main__":
	MyApp().run()