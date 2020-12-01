[![Current PyPI packages](https://badge.fury.io/py/spacy-jptdp.svg)](https://pypi.org/project/spacy-jptdp/)

# spaCy-jPTDP

[jPTDP](https://github.com/datquocnguyen/jPTDP) wrapper for [spaCy](https://spacy.io)

## Basic Usage

```py
>>> import spacy_jptdp
>>> nlp=spacy_jptdp.load("en_ewt")
>>> doc=nlp("We are finished.")
>>> for t in doc:
...   print("\t".join([str(t.i+1),t.orth_,"_",t.pos_,"_","_",str(0 if t.head==t else t.head.i+1),t.dep_,"_","_" if t.whitespace_ else "SpaceAfter=No"]))
...
1	We	_	PRON	_	_	3	nsubj	_	_
2	are	_	AUX	_	_	3	cop	_	_
3	finished	_	ADJ	_	_	0	ROOT	_	SpaceAfter=No
4	.	_	PUNCT	_	_	3	punct	_	SpaceAfter=No
>>> import deplacy
>>> deplacy.render(doc)
We       PRON  <══╗   nsubj
are      AUX   <╗ ║   cop
finished ADJ   ═╝═╝═╗ ROOT
.        PUNCT <════╝ punct
```

`spacy_jptdp.load(treebank)` loads spaCy Language pipeline for jPTDP. Available treebanks are [HERE](https://github.com/KoichiYasuoka/spaCy-jPTDP/tree/master/treebanks).

## Installation

```sh
pip install spacy_jptdp
```

