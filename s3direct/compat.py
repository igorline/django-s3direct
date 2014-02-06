import sys
PY3 = sys.version_info[0] > 2

if PY3:
    def u(s):
        return s
else:
    def u(s):
        return s.encode('utf8')