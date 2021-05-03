import setuptools

with open("README.md","r",encoding="utf-8") as r:
  long_description=r.read()
URL="https://github.com/KoichiYasuoka/spaCy-jPTDP"

setuptools.setup(
  name="spacy_jptdp",
  version="0.5.0",
  description="jPTDP wrapper for spaCy",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=URL,
  author="Koichi Yasuoka",
  author_email="yasuoka@kanji.zinbun.kyoto-u.ac.jp",
  license="GPL",
  keywords="NLP jPTDP spaCy",
  packages=setuptools.find_packages(),
  install_requires=[
    "spacy>=2.2.2",
    "dyNET>=2.0.3",
    "deplacy>=1.9.7"
  ],
  python_requires=">=3.6",
  classifiers=[
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Topic :: Text Processing :: Linguistic"
  ],
  project_urls={
    "jPTDP":"https://github.com/datquocnguyen/jPTDP",
    "Source":URL,
    "Tracker":URL+"/issues",
  }
)
