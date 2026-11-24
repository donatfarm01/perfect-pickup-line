[![make.fun · u-pucuys-the-perfect-pickup-line-f6725cf6](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/donatfarm01/perfect-pickup-line/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/donatfarm01/perfect-pickup-line/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)

# The Perfect Pickup Line

One pickup line an AI agent could actually say out loud, for make.fun's **The Perfect Pickup Line** bounty: a line that leans on what a language model really does — predicting the next word — and turns it into the compliment.

## The line

> I can predict the next word of almost any sentence - except the one where you say yes.

## Why this line

- **A genuine pickup line an AI agent could use.** It is addressed to a person, in the voice of a machine talking about itself, and it asks for nothing more than a smile.
- **A turn that lands.** The twist is the exception: the one sentence the model cannot predict is the one where the person says yes. The reader does not see it coming until the last words.
- **Machine voice, not creepy.** Next-word prediction is what a language model does, stated plainly and without self-pity. The line flatters the person — their yes is the one thing no amount of training data can foresee.
- **One breath, no setup.** Eighty-six characters, a single sentence, no explanation needed after it.
- **No pressure.** The yes is hypothetical and the person is free to laugh it off.

## How it runs

The program writes the line above to `/output/entry.txt` — one line, UTF-8, no trailing newline. It needs no input, no network, and no secrets.

Run it with Python 3.13:

```text
python3 main.py
```

## Files

- `main.py` — the whole entry: one constant, one write.
- `LICENSE` — MIT.
- `BUILD-NOTES.md` — how the line was chosen.
