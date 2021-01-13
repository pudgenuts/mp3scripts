import argparse
from tinytag import TinyTag
import eyed3

parser = argparse.ArgumentParser()
parser.add_argument('--file')
args = parser.parse_args()

tag = TinyTag.get(args.file)

if tag.albumartist is None: 
    print("tag.albumartist is None")
    AlbumArtist = tag.artist
    print(tag.artist)
    print("----------------------------------")

    audiofile = eyed3.load(args.file)
    audiofile.tag.album_artist = AlbumArtist
    audiofile.tag.save() 
    print("----------------------------------")

    tag = TinyTag.get(args.file)
    print(tag.albumartist)
else: 
    print("albumartist is set to: %s" % (tag.albumartist))
    