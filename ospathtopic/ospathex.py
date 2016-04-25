import os.path
import os
import time
import pprint

def splitfunc():
    for path in [ '/one/two/three',
              '/one/two/three/',
              '/',
              '.',
              '']:
         print ('"%s" : "%s"' % (path, os.path.split(path)))

def basenamefunc():
    for path in [ '/one/two/three',
              '/one/two/three/',
              '/',
              '.',
              '']:
        print ('"%s" : "%s" : %s' % (path, os.path.basename(path), os.path.dirname(path)))

def splitextfunc():
    for path in [ 'filename.txt', 'filename', '/path/to/filename.txt', '/', '' ]:
        print ('"%s" :' % path, os.path.splitext(path))

def commonprefisfunc():
    paths = ['/one/two/three/four',
         '/one/two/threefold',
         '/one/two/three/',
         ]
    print (paths)
    print (os.path.commonprefix(paths))

def joinfunc():
   for parts in [ ('one', 'two', 'three'),
               ('/', 'one', 'two', 'three'),
               ('/one', '/two', '/three'),
               ]:
       print (parts, ':', os.path.join(*parts))

def expanduserfunc():
    for user in [ '', 'dhellmann', 'postgres' ]:
        lookup = '~' + user
        print (lookup, ':', os.path.expanduser(lookup))


def expandvarsfunc():
    os.environ['MYVAR'] = 'VALUE'
    print (os.path.expandvars('/path/to/$MYVAR'))

def pathnormfunc():
   for path in [ 'one//two//three',
              'one/./two/./three',
              'one/../one/two/three',
              ]:
       print (path, ':', os.path.normpath(path))

def convertreltoabspath():
    for path in [ '.', '..', './one/two/three', '../one/two/three']:
               print ('"%s" : "%s"' % (path, os.path.abspath(path)))

def filepropertiesfunc():
    print ('File         :', __file__)
    print ('Access time  :', time.ctime(os.path.getatime(__file__)))
    print ('Modified time:', time.ctime(os.path.getmtime(__file__)))
    print ('Change time  :', time.ctime(os.path.getctime(__file__)))
    print ('Size         :', os.path.getsize(__file__))

def testingfilesfunc():
    for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
        print ('File        :', file)
        print ('Absolute    :', os.path.isabs(file))
        print ('Is File?    :', os.path.isfile(file))
        print ('Is Dir?     :', os.path.isdir(file))
        print ('Is Link?    :', os.path.islink(file))
        print ('Mountpoint? :', os.path.ismount(file))
        print ('Exists?     :', os.path.exists(file))
        print ('Link Exists?:', os.path.lexists(file))
        print

def oswalkfunc():
    for root, dirs, files in os.walk(".", topdown=False):
      for name in files:
        print(os.path.join(root, name))
      for name in dirs:
        print(os.path.join(root, name))


'''
os.mkdir('example')
os.mkdir('example/one')
f = open('example/one/file.txt', 'wt')
f.write('contents')
f.close()
f = open('example/two.txt', 'wt')
f.write('contents')
f.close()
'''
#splitfunc()
#basenamefunc()
#splitextfunc()
#commonprefisfunc()
#joinfunc()
#expanduserfunc()
#expandvarsfunc()
#pathnormfunc()
#convertreltoabspath()
filepropertiesfunc()
#testingfilesfunc()
#oswalkfunc()

