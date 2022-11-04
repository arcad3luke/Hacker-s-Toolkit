import requests
from bs4 import BeautifulSoup as bs

KEYWORDS="admin | index of '/admin' | cpanel | admin login | admin.php"

# Init query array
queries = []

# Construct query
query = input("Enter search query: ")

# URL to use
url = f'https://www.google.com/search?&q={query}'

# Fetch the page
req = requests.get(url)

# Yeet HTTP data from the interwebs and parse
pull = bs(req.text, "html.parser")

# Init HTML regex
htmltags = '<a>,' \
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

pull.find_all(htmltags)
pull.encode('utf-8')

# Append to query list
search = queries.append(pull)

# Print to array
print(queries)

# add to scraping.txt
with open('scraping.txt', 'a') as f:
    f.writelines(str(queries).encode('utf-8'))
    f.close()
