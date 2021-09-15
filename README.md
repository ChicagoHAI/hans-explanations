# hans-explanations

This repository contains code to generate HANS explanation data and some generated datasets.

To generate HANS explanation data:

```
python generate_examples.py SPLIT_TYPE
```

`SPLIT_TYPE` can be take different values, corresponding to different ways to split the original dataset to in-domain and out-of-domain datasets.

Some generated datasets can be found in the `split_abundant_words_templates` folder. There are 118 templates in HANS, so it is split into 5 partitions. Each partition contains 4/5th training/dev templates and 1/5th test templates. The number of examples per template are reflected in the file names. 