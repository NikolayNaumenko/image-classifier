from src.args import get_arguments
from src.print_utils import print_results
from src.utils import predict, load_model, get_class_name_by_label_fn

arguments = get_arguments()

try:
    get_class_name_by_label = get_class_name_by_label_fn(arguments.category_names)
    loaded_model = load_model(arguments.model_path)
    predictions = predict(arguments.image_path, loaded_model, arguments.top_k, get_class_name_by_label)

    print_results(arguments.image_path, predictions)
except IOError as error:
    print('Error reading file: {}'.format(error))
except Exception as exception:
    print('Something went wrong: {}'.format(exception))
