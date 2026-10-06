"""Check the generated site's indexability and metadata before deployment."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import json
import xml.etree.ElementTree as ET

ROOT = Path('site')
ORIGIN = 'https://llama-lovers.org/'


class Head(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {}
        self.canonicals = []
        self.title = ''
        self.h1_count = 0
        self.in_title = False
        self.in_json = False
        self.json_data = ''
        self.structured = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta':
            self.meta[attrs.get('name', attrs.get('property'))] = attrs.get('content')
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs['href'])
        if tag == 'title':
            self.in_title = True
        if tag == 'h1':
            self.h1_count += 1
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.in_json = True
            self.json_data = ''

    def handle_data(self, value):
        if self.in_title:
            self.title += value
        if self.in_json:
            self.json_data += value

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if tag == 'script' and self.in_json:
            self.structured.append(json.loads(self.json_data))
            self.in_json = False


def main():
    sitemap = ET.parse(ROOT / 'sitemap.xml')
    urls = [e.text for e in sitemap.findall('{*}url/{*}loc')]
    descriptions, titles = set(), set()
    assert len(urls) == len(set(urls)), 'Duplicate sitemap URLs'
    for url in urls:
        assert url.startswith(ORIGIN), url
        path = ROOT / urlparse(url).path.lstrip('/') / 'index.html'
        head = Head()
        head.feed(path.read_text())
        assert head.canonicals == [url], (path, head.canonicals)
        assert head.h1_count == 1, (path, head.h1_count)
        assert head.title and head.title not in titles, path
        titles.add(head.title)
        desc = head.meta.get('description')
        assert desc and desc not in descriptions, path
        descriptions.add(desc)
        assert 'noindex' not in head.meta.get('robots', ''), path
        assert head.meta.get('og:url') == url, path
        assert head.meta.get('og:description') == desc, path
        assert head.meta.get('twitter:card') == 'summary_large_image', path
        image_url = head.meta['og:image']
        assert image_url.startswith(ORIGIN)
        assert (ROOT / urlparse(image_url).path.lstrip('/')).exists()
        assert len(head.structured) == 1, path
        graph = head.structured[0]['@graph']
        assert {x['@type'] for x in graph} == {'Organization', 'WebSite', 'WebPage'}
        webpage = next(x for x in graph if x['@type'] == 'WebPage')
        assert webpage['url'] == url and webpage['description'] == desc
    robots = (ROOT / 'robots.txt').read_text()
    assert 'Allow: /' in robots and 'Disallow: /\n' not in robots
    assert f'Sitemap: {ORIGIN}sitemap.xml' in robots
    missing = Head()
    missing.feed((ROOT / '404.html').read_text())
    assert missing.meta.get('robots') == 'noindex'
    print(f'PASS: {len(urls)} pages with unique titles/descriptions, canonical URLs, share metadata, JSON-LD and one H1; sitemap, robots.txt and 404 checked.')


if __name__ == '__main__':
    main()
