__author__ = 'Samuel Gratzl'
import os
import configparser

_c = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

def __getattr__(item):
  return get(item)

def _expand(section=None):
  return 'DEFAULT' if section is None else section

def get(item, section=None):
  return _c[_expand(section)][item]

def set(item, value, section=None):
  _c[_expand(section)][item]=value

def getint(item, section=None):
  return _c[_expand(section)].getint(item)

def getfloat(item, section=None):
  return _c[_expand(section)].getfloat(item)

def getboolean(item, section=None):
  return _c[_expand(section)].getboolean(item)

def getlist(item, section=None, separator='\n'):
  v = _c[_expand(section)][item].strip()
  return v.split(separator)

def view(section):
  return CaleydoConfigSection(section)

class CaleydoConfigSection(object):
  def __init__(self, section):
    self._section = section

  def __getattr__(self, item):
    return self.get(item)

  def _expand(self, section=None):
    if self._section is None:
      return section if section is not None else 'DEFAULT'
    return self._section+('.'+section if section is not None else '')

  def get(self, item, section=None):
    return get(item, self._expand(section))

  def getint(self, item, section=None):
    return getint(item, self._expand(section))

  def getfloat(self, item, section=None):
    return getfloat(item, self._expand(section))

  def getboolean(self, item, section=None):
    return getboolean(item, self._expand(section))

  def getlist(self, item, section=None, separator='\n'):
    return getlist(item, self._expand(section), separator)

  def view(self, section):
    return CaleydoConfigSection(self._expand(section))


if os.path.exists('config.ini'):
  _c.read('config.ini')

def _merge_config(config_file, plugin_id):
  c = configparser.ConfigParser(interpolation=configparser.Interpolation())
  c.read(config_file)
  for section in c.sections():
    #magic name 'module' like a top level section
    fullname = plugin_id+'.'+section if section != 'module' else plugin_id
    if fullname not in _c:
      _c.add_section(fullname)
    sec = _c[fullname]
    for k,v in c.items(section):
      if k not in sec: #update with defaults
        sec[k] = v

_own_config = os.path.dirname(os.path.abspath(__file__)) + '/config.ini'
if os.path.exists(_own_config):
  _merge_config(_own_config, 'caleydo_server')

_web_config = os.path.dirname(os.path.abspath(__file__)) + '/../caleydo_web/config.ini'
if os.path.exists(_web_config):
  _merge_config(_web_config, 'caleydo_web')

def merge_plugin_configs(plugins):
  for plugin in plugins:
    config_file = os.path.join(plugin.folder, 'config.ini')
    if os.path.exists(config_file):
      _merge_config(config_file, plugin.id)