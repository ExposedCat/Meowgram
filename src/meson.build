python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'meowgram.in',
  output: 'meowgram',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

config_file = configure_file(
    input: 'config.py.in',
    output: 'config.py',
    configuration: config_data
)

meowgram_sources = [
  config_file,
  'main.py',
  'window.py',
  'login.py',
]

install_data(meowgram_sources, install_dir: moduledir)
install_subdir('backend', install_dir: moduledir)
install_subdir('connectors', install_dir: moduledir)
