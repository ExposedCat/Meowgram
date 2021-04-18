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

config_src = configure_file(
    input: 'backend/login_utils.py',
    output: '@BASENAME@',
    configuration: config_data
)

meowgram_sources = [
  'main.py',
  'window.py',
  'login.py',

  'backend/login_utils.py'
]

install_data(meowgram_sources, install_dir: moduledir)
