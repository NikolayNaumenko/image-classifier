# Usage

## Install dependecies

```bash
> pip install -r requirements.txt
```

## Print out the top K classes along with associated probabilities

```bash
> python predict.py ./test_images/cautleya_spicata.jpg ./oxford_flowers102_1658693407_model.h5 --top_k=3

Results for ./test_images/cautleya_spicata.jpg

╒════════════════════════════════╤═════════════╕
│ Class                          │ Probability │
╞════════════════════════════════╪═════════════╡
│ 60                             │   0.99902   │
├────────────────────────────────┼─────────────┤
│ 93                             │   0.00012   │
├────────────────────────────────┼─────────────┤
│ 83                             │   0.00011   │
╘════════════════════════════════╧═════════════╛
```

## Load a JSON file that maps the class values to category names

```bash
> python predict.py ./test_images/cautleya_spicata.jpg ./oxford_flowers102_1658693407_model.h5 --top_k=3 --category_names=label_map.json

Results for ./test_images/cautleya_spicata.jpg

╒════════════════════════════════╤═════════════╕
│ Class                          │ Probability │
╞════════════════════════════════╪═════════════╡
│ Cautleya Spicata (60)          │   0.99902   │
├────────────────────────────────┼─────────────┤
│ Foxglove (93)                  │   0.00012   │
├────────────────────────────────┼─────────────┤
│ Columbine (83)                 │   0.00011   │
╘════════════════════════════════╧═════════════╛
```

## Display help message

```bash
> python predict.py -h

usage: predict.py [-h] [--top_k TOP_K] [--category_names CATEGORY_NAMES]
                  image_path model_path

This is a predict sample program

positional arguments:
  image_path            Path to an image file
  model_path            Path to a model file

optional arguments:
  -h, --help            show this help message and exit
  --top_k TOP_K         Print the top K most likely classes
  --category_names CATEGORY_NAMES
                        Path to a JSON file mapping labels to flower names

```                        