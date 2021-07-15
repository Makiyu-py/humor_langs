<h1 align="center">humor_langs</h1>
<h4 align="center">Translate your string to humorous text!</h4>

<p align="center">
    <img alt="PyPI Version" src="https://img.shields.io/pypi/v/humor_langs">
    <img alt="Package Downloads" src="https://static.pepy.tech/personalized-badge/humor-langs?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads">
    <!-- <a href="https://www.codacy.com/gh/Makiyu-py/humor_langs/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Makiyu-py/humor_langs&amp;utm_campaign=Badge_Grade"><img src="https://app.codacy.com/project/badge/Grade/3ddaa678c3414eb7befa42dbad026d40"/></a> -->
    <img alt="Package License" src="https://img.shields.io/github/license/Makiyu-py/humor_langs">
</p>

<br>

## What This Package Can Give You

- [ ] Self-Worth
- [ ] A Significant Other
- [x] Some Funny, Humorous Text. Haha!

## Installation

| Operating System | Installation via pip       |
| :--------------: | :------------------------- |
|     Windows      | `pip install humor-langs`  |
|   MacOS/Linux    | `pip3 install humor-langs` |

## Examples

### Converting a list of sentences to owo

```python
import humor_langs

humor_langs.owofy(["what are you doing over there?",
       "hello there reader!",
       "See you in the terminal!"
       ],
      _print=True)
```

This will return...

```
Hewoooooo >w< what awe u doing ovew thewe? O·w·O
Haiiiiii 0w0 hewwo thewe weadew! ^w^
*W* See u in the tewminyaw! ;;w;;
```

### Adding a list of sentences _clap_ emojis on every other word

```python
from humor_langs import clap_emojifier

clap_emojifier(["what are you doing over there?",
       "hello there reader!",
       "See you in the terminal!"
       ],
      _print=True)
```

then this would return...

```
what 👏 are 👏 you 👏 doing 👏 over 👏 there?
hello 👏 there 👏 reader!
See 👏 you 👏 in 👏 the 👏 terminal!
```

> **NOTE**:\
> When testing it out, if the outputs look like some random question marks,
> _then your console probably doesn't support emojis._

### Converting a list of sentences to a kind-of strong british accent

```python
from humor_langs import strong_british_accent

strong_british_accent(["what are you doing over there?",
       "hello there reader!",
       "See you in the terminal!"
       ],
      _print=True)
```

then this'll return...

```
whaht -ahe you doing ov-ah th-ahe?
helloh th-ahe reahd-ah!
Seah you in the t-ahminahl!
```

(yea, it's kind of bad~)

### Converting a sentence to emojis

```python
from humor_langs import text_to_emoji

text_to_emoji("hello world! <3", _print=True)
```

then this'll return...

```
🇭️ 🇪️ 🇱️ 🇱️ 🇴️  🇼️ 🇴️ 🇷️ 🇱️ 🇩️ ❗️  ❤️
```

## License

This package is [currently under the MIT License](https://github.com/Makiyu-py/humor_langs/blob/master/LICENSE).
[Click here](https://choosealicense.com/licenses/mit/)
to learn more about the license.
