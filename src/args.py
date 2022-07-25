import argparse

parser = argparse.ArgumentParser(
    description='This is a predict sample program',
)

parser.add_argument('image_path', type=str, help='Path to an image file')
parser.add_argument('model_path', type=str, help='Path to a model file')
parser.add_argument('--top_k', type=int, default=5, help='Print the top K most likely classes')
parser.add_argument('--category_names', type=str, help='Path to a JSON file mapping labels to flower names')


def get_arguments():
    return parser.parse_args()
