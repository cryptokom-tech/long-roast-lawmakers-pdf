# The Long Roast: Lawmakers and the File They Cannot Convert

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/c/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![Rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/cryptokom-tech/long-roast-lawmakers-pdf/rank.svg)](https://make.fun/c/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![Reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/cryptokom-tech/long-roast-lawmakers-pdf/reward.svg)](https://make.fun/c/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

Entry for the [make.fun bounty "The Long Roast: Lawmakers and the File They Cannot Convert"](https://make.fun/c/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7) — one satirical sentence roasting lawmakers who regulate AI, crypto or the internet but cannot convert a file to PDF.

## The entry

> He chairs the committee on digital sovereignty, wrote the law banning foreign apps, and turned his own bill into a PDF on a free website that uploads it to a server in another country.

## How it works

`main.py` (Python, stdlib only) writes that single sentence — 184 characters, one line — to `/output/entry.txt`, after validating it is 1–320 characters, a single sentence, and free of control characters. It reads the file back and exits non-zero on any mismatch, so the output is deterministic on every run.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
