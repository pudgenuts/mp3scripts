import argparse
from tinytag import TinyTag
import eyed3

parser = argparse.ArgumentParser()
parser.add_argument('--file')
parser.add_argument('--fix')
parser.add_argument('--artist')
args = parser.parse_args()

tag = TinyTag.get(args.file)

if tag.albumartist is None: 
    print("\ttag.albumartist is None")
    AlbumArtist = tag.artist.strip()
    if args.fix is not None:
        print("\t\tupdating album artist to: %s for file: %s" % (AlbumArtist, args.file))
        audiofile = eyed3.load(args.file)
        audiofile.tag.album_artist = AlbumArtist
        audiofile.tag.save() 
        tag = TinyTag.get(args.file)
        if tag.albumartist is None:
            print("\talbumartist updated to: %s" % (tag.albumartist))
        else:
            print("\tERROR updating %s" % (args.file))

else: 
    print("albumartist is set to: %s" % (tag.albumartist))
    