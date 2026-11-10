"""Pull question/answer pairs out of a GHL snippet, word for word."""
import re
from bs4 import BeautifulSoup

Q_RE = re.compile(r"(^|-)faq(__|-)q(uestion)?$|^faq-q$")
A_RE = re.compile(r"(^|-)faq(__|-)(a|answer|body|a-inner)$|^faq-a$")
ITEM_RE = re.compile(r"(^|-)faq(__|-)item$|^faq-item$")

def _clean(el):
    el = BeautifulSoup(str(el), "html.parser")
    for junk in el.select("i, svg, script, style, input, [class*='faq-icon'], [class*='faq-sign'], [class*='q-icon'], [class*='a-divider']"):
        junk.decompose()
    txt = el.get_text(" ", strip=True)
    txt = re.sub(r"\s+", " ", txt)
    txt = re.sub(r"\s+([,.;:!?)])", r"\1", txt)
    txt = re.sub(r"([(])\s+", r"\1", txt)
    return txt.strip()

def _has(el, rx):
    return any(rx.search(c) for c in (el.get("class") or []))

def extract(html):
    soup = BeautifulSoup(html, "html.parser")
    pairs = []
    items = [el for el in soup.find_all(True) if _has(el, ITEM_RE)]
    for it in items:
        q = next((e for e in it.find_all(True) if _has(e, Q_RE)), None)
        a = next((e for e in it.find_all(True) if _has(e, A_RE)), None)
        if q is None and it.find("summary"):
            q = it.find("summary")
        if a is None and q is not None and q.name == "summary":
            a = BeautifulSoup(str(it), "html.parser")
            a.find("summary").decompose()
        if q is not None and a is not None:
            qt, at = _clean(q), _clean(a)
            if qt and at:
                pairs.append((qt, at))
    if not pairs:  # <details> lists without item classes
        for d in soup.find_all("details"):
            s = d.find("summary")
            if not s: continue
            qt = _clean(s)
            rest = BeautifulSoup(str(d), "html.parser"); rest.find("summary").decompose()
            at = _clean(rest)
            if qt and at and "?" in qt:
                pairs.append((qt, at))
    seen, out = set(), []
    for q, a in pairs:
        if q not in seen:
            seen.add(q); out.append((q, a))
    return out
