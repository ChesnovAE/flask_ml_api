import argparse

from app import app


def run(arguments):
    app.run(host=arguments.host,
            port=arguments.port,
            debug=arguments.debug)


def setup_parser(parser):
    parser.add_argument(
        '--host',
        help='Host',
        dest='host',
        default='0.0.0.0',
        type=str
    )
    parser.add_argument(
        '--port',
        help='Port',
        dest='port',
        default=5000,
        type=int
    )
    parser.add_argument(
        '--debug',
        help='Debug',
        dest='debug',
        default=True,
        type=bool
    )
    parser.set_defaults(callback=run)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'Flask application'
    )
    setup_parser(parser)
    arguments = parser.parse_args()
    arguments.callback(arguments)
