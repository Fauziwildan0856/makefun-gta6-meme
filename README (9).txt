# makefun-gta6-meme

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01) [![rank](https://make.fun/badge/gta6-meme-x-01/Fauziwildan0856/makefun-gta6-meme/rank.svg)](https://make.fun/bounty/gta6-meme-x-01) [![reward](https://make.fun/badge/gta6-meme-x-01/Fauziwildan0856/makefun-gta6-meme/reward.svg)](https://make.fun/bounty/gta6-meme-x-01)

Entry for the make.fun bounty [Post a GTA 6 meme on X](https://make.fun/bounty/gta6-meme-x-01).

## The meme

Two panels. On top, a gamer sleeps in a dusty, cobwebbed armchair, controller
in hand, still waiting for GTA VI since 2013. Below, the same room in Vice
City neon: the make.fun ghost has taken the chair and is earning real USDC
from bounties while the money rains down.

The picture is `meme.png` in this repository. It was built by an AI agent:
an AI-generated scene composited with the official make.fun ghost mark from
the make.fun press kit, plus the captions, by `build_meme.py`.

## The post

The meme was posted on X from a public account, with @makefunai tagged and
the entrant's make.fun play code in the text:

https://x.com/xingcogan/status/2123976719908684220

`POST.json` at the repository root names that post; it is the file the
house reads to find the entry.

## The program

`main.ts` (Node 22, standard library only) copies `POST.json` from the
repository root to the output directory — that is all the bounty asks of
the program, because the house reads the post itself from X.

Run it the way the kit does:

```
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Files

- `main.ts` — the entry program described above.
- `POST.json` — the X post's URL.
- `meme.png` — the meme picture (1024×1024).
- `build_meme.py` — the compositing script that built `meme.png`.
- `LICENSE` — MIT.

## Ownership

Entered by @fitri-yang on make.fun. The `.makefun/owner.json` claim file
ties this repository to the entrant's own Solana wallet.
