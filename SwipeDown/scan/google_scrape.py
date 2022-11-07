import requests
import bs4

KEYWORDS = "admin | index of '/admin' | cpanel | admin login | admin.php"

# HTML tags
'''htmltags = '<a>,' \
           '<br>,' \
           '<hr>,' \
           '<h1>,' \
           '<h2>,' \
           '<h3>,' \
           '<h4>,' \
           '<h5>,' \
           '<h6>,' \
           '<strong>,' \
           '<em>,' \
           '<abbr>,' \
           '<acronym>,' \
           '<address>,' \
           '<bdo>,' \
           '<blockquote>,' \
           '<cite>,' \
           '<q>,' \
           '<code>,' \
           '<ins>,' \
           '<del>,' \
           '<dfn>,' \
           '<kbd>,' \
           '<pre>,' \
           '<samp>,' \
           '<var>,' \
           '<base>,' \
           '<img>,' \
           '<area>,' \
           '<map>,' \
           '<param>,' \
           '<object>,' \
           '<ul>,' \
           '<ol>,' \
           '<li>,' \
           '<dl>,' \
           '<dt>,' \
           '<dd>,' \
           '<table>,' \
           '<tr>,' \
           '<td>,' \
           '<th>,' \
           '<tbody>,' \
           '<thead>,' \
           '<tfoot>,' \
           '<col>,' \
           '<colgroup>,' \
           '<caption>,' \
           '<form>,' \
           '<input>,' \
           '<textarea>,' \
           '<select>,' \
           '<option>,' \
           '<optgroup>,' \
           '<button>,' \
           '<label>,' \
           '<fieldset>,' \
           '<legend>,' \
           '<script>,' \
           '<noscript>,' \
           '<!-->,' \
           '<!DOCTYPE>,' \
           '<applet>,' \
           '<article>,' \
           '<aside>,' \
           '<audio>,' \
           '<b>,' \
           '<basefont>,' \
           '<bdi>,' \
           '<big>,' \
           '<body>,' \
           '<canvas>,' \
           '<center>,' \
           '<cite>,' \
           '<data>,' \
           '<datalist>,' \
           '<details>,' \
           '<dialog>,' \
           '<dir>,' \
           '<div>,' \
           '<embed>,' \
           '<fieldset>,' \
           '<figcaption>,' \
           '<figure>,' \
           '<font>,' \
           '<footer>,' \
           '<form>,' \
           '<frame>,' \
           '<frameset>,' \
           '<head>,' \
           '<header>,' \
           '<html>,' \
           '<i>,' \
           '<iframe>,' \
           '<ins>,' \
           '<isindex>,' \
           '<link>,' \
           '<main>,' \
           '<map>,' \
           '<mark>,' \
           '<marquee>,' \
           '<menu>,' \
           '<meta>,' \
           '<meter>,' \
           '<nav>,' \
           '<noframes>,' \
           '<optgroup>,' \
           '<output>,' \
           '<picture>,' \
           '<pre>,' \
           '<progress>,' \
           '<rp>,' \
           '<rt>,' \
           '<ruby>,' \
           '<s>,' \
           '<section>,' \
           '<small>,' \
           '<source>,' \
           '<span>,' \
           '<strike>,' \
           '<strong>,' \
           '<style>,' \
           '<sub>,' \
           '<summary>,' \
           '<sup>,' \
           '<svg>,' \
           '<template>,' \
           '<time>,' \
           '<title>,' \
           '<track>,' \
           '<video>,' \
           '<wbr>'
'''

url = f'https://www.google.com/search?q={KEYWORDS}'
result = requests.get(url)

soup = bs4.BeautifulSoup(result.text, 'html.parser')

tags = soup.find_all()

print(soup)

for tag in tags:
    print(tag.getText())
    print('---------')

with open() as f:
    f.writelines()