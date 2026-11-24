"""Cache original logo assets locally (requires internet). Offline reference artwork is already included."""
import json, pathlib, urllib.request, html
root=pathlib.Path(__file__).resolve().parent
manifest=json.loads((root/'assets/logo-sources.json').read_text())
page=root/'index.html'
content=page.read_text(encoding='utf-8')
for name,item in manifest.items():
    try:
        request=urllib.request.Request(item['url'],headers={'User-Agent':'RasaPortfolio/1.0 (personal portfolio logo retrieval)'})
        with urllib.request.urlopen(request,timeout=20) as response:
            if not response.headers.get_content_type().startswith('image/'):
                raise ValueError('Not an image')
            data=response.read()
        (root/item['file']).write_bytes(data)
        content=content.replace(html.escape(item['url'],quote=True),item['file'])
        print('Saved original:',item['file'])
    except Exception as exc:
        print(name,':',exc,'(reference fallback retained)')
page.write_text(content,encoding='utf-8')
