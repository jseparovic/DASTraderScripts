import re
import importlib
from os.path import join

SCRIPT_DIR = 'scripts'
LIB_DIR = 'lib'
GLOBALS = 'globals.py'

DAS_SCRIPT = "def das_script():"

def remove_comments(string):
    string = re.sub(re.compile("\"\"\".*?\"\"\"", re.DOTALL), "", string)
    string = re.sub(re.compile("'''.*?\'''", re.DOTALL), "", string)
    string = re.sub(re.compile("\\s*#.*?\n", re.DOTALL), "\n", string)
    return string


def remove_non_das(string):
    string = re.sub(re.compile("^(.*\n)+def das_script.*\n", re.MULTILINE), "", string)
    string = remove_comments(string)
    string = re.sub(re.compile("print\\(.*?\n", re.DOTALL), "", string)
    string = re.sub(re.compile("global.*?\n", re.DOTALL), "", string)
    string = ''.join(line.strip(' \t') for line in string.splitlines(True))
    string = string.replace("\"", "")
    string = re.sub(re.compile("^(?imu)^\\s*\n", re.DOTALL), '', string, re.MULTILINE)
    return string


def split_and_strip(line):
    (const_name, const_value) = line.split('=')
    return const_name.strip(), const_value.strip()


def map_constants(constants_map, string):
    contents = remove_comments(string)
    # Search for INT_ or FLOAT_ STRING_ constant defs
    for line in contents.splitlines():
        if re.compile("INT_.+=.+").match(line):
            (const_name, const_value) = split_and_strip(line)
            constants_map[const_name] = int(const_value)
        elif re.compile("FLOAT_.+=.+").match(line):
            (const_name, const_value) = split_and_strip(line)
            constants_map[const_name] = float(const_value)
        elif re.compile("STRING_.+=.+").match(line):
            (const_name, const_value) = split_and_strip(line)
            constants_map[const_name] = const_value

    return constants_map


def replace_constants(constants_map, string):
    contents = string
    for name, value in constants_map.items():
        contents = contents.replace(name, value.__str__()).replace("\"", "")
    return contents


def format_das_script(script):
    with open(join(SCRIPT_DIR, script)) as fp:
        contents = fp.read()
        constants_map = map_constants({}, contents)

        global_constants = open(join(LIB_DIR, GLOBALS)).read()
        constants_map = map_constants(constants_map, global_constants)

        contents = remove_non_das(contents)
        contents = replace_constants(constants_map, contents)
        contents = re.sub(re.compile("\n", re.DOTALL), "; ", contents)

        return contents


def test(script):
    module = SCRIPT_DIR + "." + script
    script_module = importlib.import_module(module, SCRIPT_DIR)
    script_module.das_script()
