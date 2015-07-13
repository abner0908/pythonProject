from re_test_patterns import test_patterns

test_patterns('A prime #1 example!',
                [ ('\d+', 'sequence of digits'),
                  ('\D+', 'sequence of nondigits'),
                  ('\s+', 'sequence of whitespace'),
                  ('\S+', 'sequence of nonwhitespace'),
                  ('\w+', 'alphanumeric characters'),
                  ('\W+', 'nonalphanumeric'),
                ])