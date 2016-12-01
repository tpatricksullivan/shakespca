import os
import urllib2
import re
import getTextMetadata


def shakespeare_plays(input_file):
    """Download the plays"""
    url_template = 'http://www.folgerdigitaltexts.org/{0}/text'
    text_map = getTextMetadata.main(input_file)
    play_map = text_map[ (text_map["First_Folio_category"] != "Other")]
    for play in play_map['text_code']:
        url = url_template.format(play)
        print('downloading and stripping play {0}: {1}'.format(play, url))
        download_clean_play(url, play)

    return 0


def download_clean_play(url, play):
    """Clean non-text elements from Folger download"""
    u = urllib2.urlopen(url)
    if not os.path.exists('data/'):
        os.mkdir('data/')
    f = open('data/{0}.txt'.format(play), 'w')
    for line in u:
        line = re.sub('<br/>', '', line)
        f.write(line)
    f.close()

    return 0


def shakespeare_sonnets():
    """Download and clean non-text elements from the Sonnets"""
    url = 'http://www.folgerdigitaltexts.org/download/txt/Son.txt'
    u = urllib2.urlopen(url)
    if not os.path.exists('data/'):
        os.mkdir('data/')
    f = open('data/Son.txt', 'w')
    while True:
        l = u.next()
        if l == '1\r\n':
            break
    while True:
        l = u.next()
        if bool(re.match('[0-9]', l)):
            continue
        if 'water cools not love' in l.lower():
            f.write(l)
            break
        f.write(l)
    f.close()

    return 0


def gutenberg_texts(texts):
    """Download all texts from the input list from Gutenberg"""
    for t in texts:
        gutenberg_text(t[0], t[1])

    return 0


def gutenberg_text(friendly_name, url):
    """Download and clean non-text elements from Gutenberg project text"""
    u = urllib2.urlopen(url)
    print('downloading text {0}: {1}'.format(friendly_name, url) )
    if not os.path.exists('data/'):
        os.mkdir('data/')
    f = open('data/{0}.txt'.format(friendly_name), 'w')
    while True:
        l = u.next()
        if re.match('chapter 1|chapter i', l.lower()):
            break
    while True:
        l = u.next()
        if re.match('chapter [0-9]+', l.lower()):
            continue
        if 'End of the Project Gutenberg EBook' in l:
            break
        f.write(l)
    f.close()

    return 0

if __name__ == "__main__":
    shakespeare_plays("textMetadata.csv")
    shakespeare_sonnets()
    gutenberg_texts([('Pride and Prejudice', 'http://www.gutenberg.org/files/1342/1342-0.txt'),
                      ('Leviathan', 'http://www.gutenberg.org/cache/epub/3207/pg3207.txt')]
                     )
