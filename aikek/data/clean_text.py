import html
import re


def cleanText(article: str = None) -> str:
    """
    clean text from trash

    Parameters
    ----------
        input_text: str
            input article aka from page
    Returns
    -------
        clean str
    """

    if type(article) != str:
        raise AssertionError('input value isn`t string')

    text = html.unescape(article)

    text = re.sub('\d{2}.\d{2}.\d{2}, \d{2}:\d{2}:\d{2}', '', text)
    text = re.sub('\d{2}.\d{2} \d{2}:\d{2}', '', text)

    # remove all between <a & /?a> also <span & /?span>
    text = re.sub(r'(<span.*?\/?span>)|(<a.*?\/?a>)', '', text)
    text = re.sub(r'<strong>|<\/strong>', '', text)
    # remove all between <a & a>
    text = re.sub(r'<\/?b>|<\/?em>|<\/?i>', '', text)

    text = re.sub('(\|\s*\S*)$', '', text)  # del all end of string after '|'
    # del first char '-' & ':'
    # text = re.sub('(^\s*-)|(^-)|(-\s*$)|(-$)|(:$)|(:\s*$)|(\-\s*.$)|[\]|[]', '', text)
    text = re.sub(' : ', '', text)  # replace ':'
    # replace all kind apostrophe to one
    text = re.sub(r"\ ́|\’|\‘|\'|\”", '', text)

    text = re.sub('[/\\\\]', '', text)  # remove '\'

    # strip to remote whitespaces before and behind the word
    text = re.sub('-\s\r\n\|-\s\r\n|\r\n|[><]"[\[]]|//"', '', text)
    text = re.sub('[><]"[\[]]"', '', text)
    text = re.sub('[♛☄_…©*@^•·\|]|[=]|[/]', ' ', text)
    text = re.sub('—|–', '-', text)

    # text = re.sub(r'\r\n\t|\n|\r\t|\\n|&gt', ' ', text)
    text = re.sub('(\xa0)', ' ', text)
    text = re.sub('(\s\s\s*)', ' ', text)  # del long whitespaces
    text = re.sub('^(!(!?)\s)', '', text)  # remove start !
    text = re.sub('|\/||@|\|~|>|<|=', '', text)  # remove some punctuations
    text = re.sub('\.(.*)$', '', text)  # del last ...

    return text.strip()
