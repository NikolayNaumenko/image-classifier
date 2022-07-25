def _print_header():
    print('╒{:═^32}╤{:═^13}╕'.format('', ''))
    print('│ \033[1m{:<30}\033[0m │ \033[1m{: ^11}\033[0m │'.format('Class', 'Probability'))
    print('╞{:═^32}╪{:═^13}╡'.format('', ''))


def _print_footer():
    print('╘{:═^32}╧{:═^13}╛\n'.format('', ''))


def _print_body(results):
    last_label = results[-1][0]

    for label, prediction in results:
        print('│ {:<30} │ {: ^11} │'.format(label, '{:0.5f}'.format(prediction)))
        if last_label != label:
            print('├{:─^32}┼{:─^13}┤'.format('', ''))


def print_results(image_path, results):
    print('\nResults for {}\n'.format(image_path))

    _print_header()
    _print_body(results)
    _print_footer()
