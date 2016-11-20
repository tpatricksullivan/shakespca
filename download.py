import os
import urllib2
import re
import getPlayMetadata


def main(input_file):
    url_template = 'http://www.folgerdigitaltexts.org/{0}/text'
    play_map = getPlayMetadata.main(input_file)
    for play in play_map['play_code']:
        url = url_template.format(play)
        print('downloading and stripping play {0}: {1}'.format(play, url))
        clean_html(url, play)

    return 0


def clean_html(url, play):
    u = urllib2.urlopen(url)
    if not os.path.exists('data/'):
        raise IOError('./data folder not found')
    f = open('data/{0}.txt'.format(play), 'w')
    for line in u:
        line = re.sub('<br/>', '', line)
        f.write(line)
    f.close()

    return 0


if __name__ == "__main__":
    main("playMetadata.csv")
