#!/usr/bin/env bash

mkdir -p data/preprocessed
mkdir -p data/raw

# preprocessed data (tsv files)
wget "https://www.dropbox.com/scl/fi/lflt1yiqoppc39fv5zfk1/train_vg.tsv?rlkey=yhzphxx599r6ke17y7pf8eiom&dl=0" -O data/preprocessed/train_vg.tsv
wget "https://www.dropbox.com/scl/fi/er0pwtp1g50nya5mpbsab/train_questioner.tsv?rlkey=r1ka8t5t83vvj3vaa90n1h3ug&dl=0" -O data/preprocessed/train_questioner.tsv
wget "https://www.dropbox.com/scl/fi/81hl70ebztdtpqreijecz/train_answerer.tsv?rlkey=dj5247k7ho1u3spor9a2jq30d&dl=0" -O data/preprocessed/train_answerer.tsv
wget "https://www.dropbox.com/scl/fi/bk3v9bux7ll2o4w8q88pp/val_common.tsv?rlkey=kbjsnumf5vgzrc2krxsqhmr3w&dl=0" -O data/preprocessed/val_common.tsv
wget "https://www.dropbox.com/scl/fi/8hmcbexm1uagrmem3nhw8/test_seen_common.tsv?rlkey=46dkp0wp0jrxovges28l9hmxn&dl=0" -O data/preprocessed/test_seen_common.tsv
wget "https://www.dropbox.com/scl/fi/96yu9oiog07o2ih4zfx5g/test_seen_cluttered_common.tsv?rlkey=zsgfrkjw85z31lddbxfs1zi1h&dl=0" -O data/preprocessed/test_seen_cluttered_common.tsv
wget "https://www.dropbox.com/scl/fi/vifuzcfowk9rhoc2ygegc/test_unseen_common.tsv?rlkey=a31qshsnyb548zl9kt07b9fo2&dl=0" -O data/preprocessed/test_unseen_common.tsv
wget "https://www.dropbox.com/scl/fi/cgaowetz0tuvku30kmq43/val_vg.tsv?rlkey=p7jbd6t638qcq2ckdioq3ubhp&dl=0" -O data/preprocessed/val_vg.tsv
wget "https://www.dropbox.com/scl/fi/jtsdyauxavd8k9g0rrz0s/val_questioner.tsv?rlkey=tadwzc8tfwo3xx0gadtinznnu&dl=0" -O data/preprocessed/val_questioner.tsv
wget "https://www.dropbox.com/scl/fi/czirmetlsvf11i7c8gi3c/val_answerer.tsv?rlkey=55wm3xn2x2sxbzxxv85l9zm69&dl=0" -O data/preprocessed/val_answerer.tsv

# raw data
wget "https://www.dropbox.com/scl/fi/qluzyyez6wujql4qeal31/im-dial.zip?rlkey=4v38dgncwi5yrvc4cr9wn2vky&dl=0" -O data/raw/raw.zip
