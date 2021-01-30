from tinytag import TinyTag
import eyed3
import argparse
import glob, os


def recurseDirectory():
    pritn("recurseDirectory")

parser = argparse.ArgumentParser()
parser.add_argument('--dir')
args = parser.parse_args()

os.chdir(args.dir)
for file in glob.glob("*", recursive=True):
    if os.path.isdir(file):        
        print("%s is a directorty" % (file))
    if os.path.isfile(file):
        print("%s is a file" % (file))
        if "mp3" in file:
            tag = TinyTag.get(file)
            print(tag)
    
    
    
    
    
    
