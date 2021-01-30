import argparse
from tinytag import TinyTag
import eyed3

parser = argparse.ArgumentParser()
parser.add_argument('--file')
parser.add_argument('--fix')
parser.add_argument('--debug')
parser.add_argument('--artist')
args = parser.parse_args()


if args.artist is not None:
    tag = TinyTag.get(args.file)
    if args.debug is not None: 
        print(tag);
    AlbumArtist = args.artist
    print("\t\tupdating artist and album artist to: %s for file: %s" % (AlbumArtist, args.file))
    if args.fix is not None: 
        audiofile = eyed3.load(args.file)
        audiofile.tag.album_artist = AlbumArtist
        audiofile.tag.artist = AlbumArtist
        audiofile.tag.save() 
        tag = TinyTag.get(args.file)
        if tag.albumartist is None:
            print("\talbumartist updated to: %s" % (tag.albumartist))
            print("\talbumartist updated to: %s" % (tag.artist))
        else:
            print("\tERROR updating %s" % (args.file))
else: 
    print("missing parameter --artist ")
    